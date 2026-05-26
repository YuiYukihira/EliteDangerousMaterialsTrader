import argparse
from collections import defaultdict
import json
import os
import re
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


import pandas as pd
import pulp
import tksheet

from constants import ALL_MATERIALS, ENCODED_MATERIALS, GRADE_CAPACITIES, MANUFACTURED_MATERIALS, MATERIAL_GRADES, MATERIAL_NAME_TO_ID, MATERIALS, RAW_MATERIALS, TRADE_ACTION_COST, TRADES, WINDOW_SIZE

def _make_acquire_vars(*materials_sets):
    acquire_vars = {}

    for materials in materials_sets:
        for category in materials:
            for grade in range(len(category)):
                material = category[grade]
                acquire_vars[material] = {
                    "cost": 30 + (5 * (5 - grade)),
                    "var": pulp.LpVariable(f"acquire_{material}", lowBound=0, cat="Integer"),
                }

    return acquire_vars

def get_wishlist(filename):
    df = pd.read_fwf(
        filename,
            colspecs=[
            (0, 45),     # Material
            (45, 57),    # Available S
            (57, 75),    # Available FC
            (75, 93),    # Available Total
            (93, 107),   # Required min
            (107, 121),  # Required cur
            (121, 135),  # Required max
            (135, 149),  # Need
        ],
        names=["Material", "Available S", "Available FC", "Available Total",
            "Required min", "Required cur", "Required max", "Need"],
        skiprows=1,  # skip the original header row
    )

    required = df[["Material", "Required cur"]].dropna().set_index("Material")["Required cur"].to_dict()
    required = {MATERIAL_NAME_TO_ID[key]: value for key, value in required.items() if key in MATERIAL_NAME_TO_ID}

    return required

def get_journal_dir():
    if sys.platform == 'win32':
        user_path = os.environ.get('USERPROFILE')
        journal_dir = os.path.join(user_path, 'Saved Games', 'Frontier Developments', 'Elite Dangerous')
    else:
        user_path = os.path.expanduser('~')
        journal_dir = os.path.join(user_path, '.local', 'share', 'Steam', 'steamapps', 'compatdata', '359320', 'pfx', 'drive_c', 'users', 'steamuser', 'Saved Games', 'Frontier Developments', 'Elite Dangerous')
    return journal_dir

def get_newest_journal_file(journal_directory):
    r = r'^Journal\.\d{4}-\d{2}-\d{2}T\d{6}\.\d{2}\.log$'
    files = os.listdir(journal_directory)
    journal_files = sorted([ i for i in files if re.fullmatch(r, i)], reverse=True)
    journals = [os.path.join(journal_directory, i) for i in journal_files]
    newest_journal = journals[0]
    return newest_journal

def get_current(journal_filename):
    inventory = defaultdict(int)
    with open(journal_filename) as journal:
        while line := journal.readline():
            record = json.loads(line)
            if record["event"] == "Materials":
                for material in record["Raw"]:
                    inventory[material["Name"]] += material["Count"]
                for material in record["Encoded"]:
                    if material["Name"].startswith("tg_") or material["Name"] == "unknownshipsignature":
                        continue
                    inventory[material["Name"]] += material["Count"]
                for material in record["Manufactured"]:
                    if material["Name"].startswith("guardian_") or material["Name"] == "unknownenergysource":
                        continue
                    inventory[material["Name"]] += material["Count"]
                break
            elif record["event"] == "MaterialTrade":
                inventory[record["Paid"]["Material"]] -= record["Paid"]["Quantity"]
                inventory[record["Received"]["Material"]] += record["Received"]["Quantity"]
            elif record["event"] == "MaterialCollected":
                inventory[record["Name"]] += record["Count"]
            elif record["event"] == "MaterialDiscarded":
                inventory[record["Name"]] -= record["Count"]

    return inventory

def solve(wishlist):
    problem = pulp.LpProblem(
        "MaterialTrading",
        pulp.LpMinimize,
    )

    trade_vars = {
        name: pulp.LpVariable(name, lowBound=0, cat="Integer")
        for name in TRADES
    }

    acquire_vars = _make_acquire_vars(RAW_MATERIALS, ENCODED_MATERIALS, MANUFACTURED_MATERIALS)

    problem += pulp.lpSum(
        trade_vars[name] * (TRADES[name]["cost"] + TRADE_ACTION_COST)
        for name in TRADES
    ) + pulp.lpSum(
        acquire_vars[material]["var"] * acquire_vars[material]["cost"]
        for material in acquire_vars.keys()
    )

    for material in ALL_MATERIALS:
        produced = pulp.lpSum(
            trade_vars[t] * TRADES[t]["produce"].get(material, 0)
            for t in TRADES
        )

        consumed = pulp.lpSum(
            trade_vars[t] * TRADES[t]["consume"].get(material, 0)
            for t in TRADES
        )

        current = current_materials.get(material, 0)
        need = wishlist.get(material, 0)

        # Minimum, need at least this
        problem += (
            current + acquire_vars[material]["var"] + produced - consumed >= need, #+ surplus_vars[material],
            f"balance_{material}"
        )

        # Maximum, bins can't exceed this
        grade = MATERIAL_GRADES.get(material, 0)
        cap = GRADE_CAPACITIES[grade]
        problem += (
            current + acquire_vars[material]["var"] + produced - consumed <= cap,
            f"cap_{material}"
        )

    print("Cronching the numbers...")

    problem.solve(pulp.PULP_CBC_CMD(
        timeLimit=30,
        options=["feasibilityPump", "greedyHeuristic"],
    ))

    print(f"Status: {pulp.LpStatus[problem.status]}")

    new_trades_data = []
    new_acquisitions_data = []

    for name, var in trade_vars.items():
        if var.value() > 0:
            items = name.split('_')
            source = MATERIALS[items[0]]
            target = MATERIALS[items[2]]

            print(f"  {source} -> {target} x{var.value()}")
            new_trades_data.append([source, target, var.value()])
    

    for name, var in acquire_vars.items():
        if var["var"].value() > 0:
            print(f"  {MATERIALS[name]} x{var["var"].value()}")
            new_acquisitions_data.append([MATERIALS[name], int(var["var"].value())])
    return new_trades_data, new_acquisitions_data


current_materials = {}

def open_wishlist():
    file_path = filedialog.askopenfilename(
        title="Open EDOMH Wishlist",
        filetypes=[("Text File", ('*.txt')), ("All Files", '*.*')]
    )
    if not file_path:
        return

    wishlist = get_wishlist(file_path)

    trades_frame.grid_remove()
    acquisitions_frame.grid_remove()
    status_label.grid(column=0, row=2, columnspan=2, pady=40)
    status_var.set("Cronching the numbers...")
    root.update_idletasks()

    new_trades_data, new_acquisitions_data = solve(wishlist)

    trades_sheet.set_sheet_data(new_trades_data)
    acquisitions_sheet.set_sheet_data(new_acquisitions_data)

    status_label.grid_remove()
    trades_frame.grid(row=1, column=0, sticky='nswe')
    acquisitions_frame.grid(row=1, column=1, sticky='nswe')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                prog="ED Mat Trader",
                description="Calculates optimal material trades"
             )
    parser.add_argument("-j", "--journals")

    args = parser.parse_args()

    if args.journals is not None:
        journal_dir = args.journals
    else:
        journal_dir = get_journal_dir()

    current_materials = get_current(get_newest_journal_file(journal_dir))

    root = tk.Tk()

    root.title("Elite Dangerous Materials Trader")
    root.geometry(WINDOW_SIZE)

    style = ttk.Style()
    style.layout("Tab",
                 [("Notebook.tab", {'sticky': 'nswe', 'children':
                    [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                        [('Notebook.label', {'side': 'top', 'sticky': ''})],
                    })],
                  })]
                )

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    
    ttk.Button(frm, text="Open Wishlist", command=open_wishlist).grid(column=0, row=0)
    
    status_var = tk.StringVar(value="Open a wishlist to calculate trades")
    status_label = ttk.Label(frm, textvariable=status_var, justify='center', font=('TkDefaultFont', 11))
    status_label.grid(column=0, row=1, columnspan=2, pady=40)


    trades_frame = tk.Frame(frm)
    trades_frame.grid_columnconfigure(0, weight=1)
    trades_frame.grid_rowconfigure(0, weight=1)
    
    ttk.Label(trades_frame, text='Trades', justify='left').grid(column=0, row=0)
    trades_sheet = tksheet.Sheet(
        trades_frame,
        data=[],
        headers=["From", "To", "Amount"],
    )
    trades_sheet.enable_bindings()
    trades_sheet.grid(row=1, column=0, sticky='nswe')


    acquisitions_frame = tk.Frame(frm)
    acquisitions_frame.grid_columnconfigure(0, weight=1)
    acquisitions_frame.grid_rowconfigure(0, weight=1)

    ttk.Label(acquisitions_frame, text='Acqusitions', justify='left').grid(column=0, row=0)
    acquisitions_sheet = tksheet.Sheet(
        acquisitions_frame,
        data=[],
        headers=["Commodity", "Amount"],
    )
    acquisitions_sheet.enable_bindings()
    acquisitions_sheet.grid(row=1, column=0, sticky='nswe')

    root.mainloop()