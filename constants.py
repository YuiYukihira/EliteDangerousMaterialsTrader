GRADE_CAPACITIES = [ 300, 250, 200, 150, 100 ]

MATERIALS = {
    # Raw
    "carbon": "Carbon",
    "vanadium": "Vanadium",
    "niobium": "Niobium",
    "yttrium": "Yttrium",
    "phosphorus": "Phosphorus",
    "chromium": "Chromium",
    "molybdenum": "Molybdenum",
    "technetium": "Technetium",
    "sulphur": "Sulphur",
    "manganese": "Manganese",
    "ruthenium": "Ruthenium",
    "cadmium": "Cadmium",
    "iron": "Iron",
    "zinc": "Zinc",
    "tin": "Tin",
    "selenium": "Selenium",
    "nickel": "Nickel",
    "germanium": "Germanium",
    "tungsten": "Tungsten",
    "tellurium": "Tellurium",
    "rhenium": "Rhenium",
    "arsenic": "Arsenic",
    "mercury": "Mercury",
    "polonium": "Polonium",
    "lead": "Lead",
    "zirconium": "Zirconium",
    "boron": "Boron",
    "antimony": "Antimony",

    # Encoded
    "bulkscandata": "Anomalous Bulk Scan Data",
    "emissiondata": "Unexpected Emission Data",
    "shieldsoakanalysis": "Inconsistent Shield Soak Analysis",
    "archivedemissiondata": "Irregular Emission Data",
    "shielddensityreports": "Untypical Shield Scans",
    "disruptedwakeechoes": "Atypical Disrupted Wake Echoes",
    "shieldcyclerecordings": "Distorted Shield Cycle Recordings",
    "wakesolutions": "Strange Wake Solutions",
    "fsdtelemetry": "Anomalous FSD Telemetry",
    "shieldpatternanalysis": "Aberrant Shield Pattern Analysis",
    "scanarchives": "Unidentified Scan Archives",
    "scandatabanks": "Classified Scan Databanks",
    "decodedemissiondata": "Decoded Emission Data",
    "shieldfrequencydata": "Peculiar Shield Frequency Data",
    "classifiedscandata": "Classified Scan Fragment",
    "hyperspacetrajectories": "Eccentric Hyperspace Trajectories",
    "dataminedwake": "Datamined Wake Exceptions",
    "legacyfirmware": "Specialised Legacy Firmware",
    "scrambledemissiondata": "Exceptional Scrambled Emission Data",
    "encryptioncodes": "Tagged Encryption Codes",
    "encryptionarchives": "Atypical Encryption Archives",
    "symmetrickeys": "Open Symmetric Keys",
    "adaptiveencryptors": "Adaptive Encryptors Capture",
    "compactemissionsdata": "Abnormal Compact Emissions Data",
    "industrialfirmware": "Cracked Industrial Firmware",
    "consumerfirmware": "Modified Consumer Firmware",
    "modifiedembeddedfirmware": "Modified Embedded Firmware",
    "unusualencryptedfiles": "Unusual Encrypted Files",
    "divergentscandata": "Divergent Scan Data",
    "securityfirmwarepatch": "Secutiry Firmware Patch",

    # Manufactured
    "chemicaldistillery": "Chemical Distillery",
    "focuscrystals": "Focus Crystals",
    "highdensitycomposites": "High Density Composites",
    "chemicalstorageunits": "Chemical Storage Units",
    "hybridcapacitors": "Hybrid Capacitors",
    "chemicalprocessors": "Chemical Processors",
    "configurablecomponents": "Configurable Components",
    "mechanicalscrap": "Mechanical Scrap",
    "conductiveceramics": "Conductive Ceramics",
    "polymercapacitors": "Polymer Capacitors",
    "refinedfocuscrystals": "Refined Focus Crystals",
    "shieldemitters": "Shield Emitters",
    "imperialshielding": "Imperial Shielding",
    "exquisitefocuscrystals": "Exquisite Focus Crystals",
    "mechanicalequipment": "Mechanical Equipment",
    "mechanicalcomponents": "Mechanical Components",
    "improvisedcomponents": "Improvised Components",
    "protoheatradiators": "Proto Heat Radiators",
    "militarysupercapacitors": "Military Supercapacitors",
    "biotechconductors": "Biotech Conductors",
    "protoradiolicalloys": "Proto Radiolic Alloys",
    "galvanisingalloys": "Galvanising Alloys",
    "compactcomposites": "Compact Composites",
    "compoundshielding": "Compound Shielding",
    "uncutfocuscrystals": "Flawed Focus Crystals",
    "gridresistors": "Grid Resistors",
    "heatresistantceramics": "Heat Resistant Ceramics",
    "precipitatedalloys": "Precipitated Alloys",
    "shieldingsensors": "Shielding Sensors",
    "thermicalloys": "Thermic Alloys",
    "fedproprietarycomposites": "Proprietary Composites",
    "phasealloys": "Phase Alloys",
    "heatconductionwiring": "Heat Conduction Wiring",
    "basicconductors": "Basic Conductors",
    "militarygradealloys": "Military Grade Alloys",
    "coredynamicscomposites": "Core Dynamics Composites",
    "conductivepolymers": "Conductive Polymers",
    "pharmaceuticalisolators": "Pharmaceutical Isolators",
    "electrochemicalarrays": "Electrochemical Arrays",
    "heatdispersionplate": "Heat Dispersion Plate",
    "heatexchangers": "Heat Exchangers",
    "heatvanes": "Heat Vanes",
    "temperedalloys": "Tempered Alloys",
    "conductivecomponents": "Conductive Components",
    "wornshieldemitters": "Worn Shield Emitters",
    "filamentcomposites": "Filament Comoisites",
    "crystalshards": "Crystal Shards",
    "salvagedalloys": "Salvaged Alloys",
    "protolightalloys": "Proto Light Alloys",
    "chemicalmanipulators": "Chemical Manipulators",
}

MATERIAL_NAME_TO_ID = { value: key for key,value in MATERIALS.items() }

RAW_MATERIALS = [
    [ "carbon", "vanadium", "niobium", "yttrium" ],
    [ "phosphorus", "chromium", "molybdenum", "technetium" ],
    [ "sulphur", "manganese", "cadmium", "ruthenium" ],
    [ "iron", "zinc", "tin", "selenium" ],
    [ "nickel", "germanium", "tungsten", "tellurium" ],
    [ "rhenium", "arsenic", "mercury", "polonium" ],
    [ "lead", "zirconium", "boron", "antimony" ]
]
for row in RAW_MATERIALS:
    for material in row:
        try:
            assert(material in MATERIALS.keys())
        except AssertionError:
            raise AssertionError(f"{material} is missing")

ENCODED_MATERIALS = [
    [ "scrambledemissiondata", "archivedemissiondata", "emissiondata", "decodedemissiondata", "compactemissionsdata" ],
    [ "disruptedwakeechoes", "fsdtelemetry", "wakesolutions", "hyperspacetrajectories", "dataminedwake" ],
    [ "shieldcyclerecordings", "shieldsoakanalysis", "shielddensityreports", "shieldpatternanalysis", "shieldfrequencydata" ],
    [ "unusualencryptedfiles", "encryptioncodes", "symmetrickeys", "encryptionarchives", "adaptiveencryptors" ],
    [ "bulkscandata", "scanarchives", "scandatabanks", "divergentscandata", "classifiedscandata" ],
    [ "legacyfirmware", "consumerfirmware", "industrialfirmware", "securityfirmwarepatch", "modifiedembeddedfirmware" ]
]
for row in ENCODED_MATERIALS:
    for material in row:
        try:
            assert(material in MATERIALS.keys())
        except AssertionError:
            raise AssertionError(f"{material} is missing")

MANUFACTURED_MATERIALS = [
    [ "chemicalstorageunits", "chemicalprocessors", "chemicaldistillery", "chemicalmanipulators", "pharmaceuticalisolators" ],
    [ "temperedalloys", "heatresistantceramics", "precipitatedalloys", "thermicalloys", "militarygradealloys" ],
    [ "heatconductionwiring", "heatdispersionplate", "heatexchangers", "heatvanes", "protoheatradiators" ],
    [ "basicconductors", "conductivecomponents", "conductiveceramics", "conductivepolymers", "biotechconductors" ],
    [ "mechanicalscrap", "mechanicalequipment", "mechanicalcomponents", "configurablecomponents", "improvisedcomponents" ],
    [ "gridresistors", "hybridcapacitors", "electrochemicalarrays", "polymercapacitors", "militarysupercapacitors" ],
    [ "wornshieldemitters", "shieldemitters", "shieldingsensors", "compoundshielding", "imperialshielding" ],
    [ "compactcomposites", "filamentcomposites", "highdensitycomposites", "fedproprietarycomposites", "coredynamicscomposites" ],
    [ "crystalshards", "uncutfocuscrystals", "focuscrystals", "refinedfocuscrystals", "exquisitefocuscrystals" ],
    [ "salvagedalloys", "galvanisingalloys", "phasealloys", "protolightalloys", "protoradiolicalloys" ]
]
for row in MANUFACTURED_MATERIALS:
    for material in row:
        try:
            assert(material in MATERIALS.keys())
        except AssertionError:
            raise AssertionError(f"{material} is missing")

def _compute_materials_grades(*materials_sets):
    material_grades = {}
    for materials in materials_sets:
        for row in materials:
            for i in range(len(row)):
                material_grades[row[i]] = i
    return material_grades
MATERIAL_GRADES = _compute_materials_grades(RAW_MATERIALS, ENCODED_MATERIALS, MANUFACTURED_MATERIALS)

def _compute_trades(*materials_sets):
    trades = {}
    for materials in materials_sets:
        # same category trades
        for category in materials:
            for source_grade in range(len(category)):
                for target_grade in range(len(category)):
                    if source_grade == target_grade:
                        continue

                    source = category[source_grade]
                    target = category[target_grade]

                    grade_delta = target_grade - source_grade

                    if grade_delta > 0:
                        amount = 6 ** grade_delta

                        trades[f"{source}_to_{target}"] = {
                            "consume": {
                                source: amount,
                            },
                            "produce": {
                                target: 1,
                            },
                            "cost": grade_delta,
                        }
                    else:
                        amount = 3 ** (-grade_delta)

                        trades[f"{source}_to_{target}"] = {
                            "consume": {
                                source: 1,
                            },
                            "produce": {
                                target: amount,
                            },
                            "cost": -grade_delta
                        }

        for source_category_index in range(len(materials)):
            for target_category_index in range(len(materials)):
                if source_category_index == target_category_index:
                    continue
                
                source_category = materials[source_category_index]
                target_category = materials[target_category_index]

                for source_grade in range(len(source_category)):
                    for target_grade in range(len(target_category)):
                        source = source_category[source_grade]
                        target = target_category[target_grade]

                        grade_delta = target_grade - source_grade

                        if grade_delta >= 0:
                            amount = 6 ** (grade_delta + 1)

                            #if amount > GRADE_CAPACITIES[source_grade]:
                            #    continue

                            trades[f"{source}_to_{target}"] = {
                                "consume": {
                                    source: amount,
                                },
                                "produce": {
                                    target: 1
                                },
                                "cost": 10 + grade_delta,
                            }
                        else:
                            amount = 3 ** (grade_delta - 1)

                            #if amount > GRADE_CAPACITIES[target_grade]:
                            #    continue

                            trades[f"{source}_to_{target}"] = {
                                "consume": {
                                    source: 2,
                                },
                                "produce": {
                                    target: amount
                                },
                                "cost": 10 - grade_delta
                            }
    return trades
TRADES = _compute_trades(RAW_MATERIALS, ENCODED_MATERIALS, MANUFACTURED_MATERIALS)

ALL_MATERIALS = set([mat for category in RAW_MATERIALS for mat in category]) | set([mat for category in ENCODED_MATERIALS for mat in category]) | set([mat for category in MANUFACTURED_MATERIALS for mat in category])


WINDOW_SIZE = "1080x420"

TRADE_ACTION_COST = 1