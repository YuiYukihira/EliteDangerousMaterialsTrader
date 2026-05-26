# Elite Dangerous Materials Trader (EDMT)

![GitHub Release](https://img.shields.io/github/v/release/YuiYukihira/EliteDangerousMaterialsTrader) ![GitHub Release Date](https://img.shields.io/github/release-date/YuiYukihira/EliteDangerousMaterialsTrader) ![GitHub License](https://img.shields.io/github/license/YuiYukihira/EliteDangerousMaterialsTrader) ![GitHub Download Count](https://img.shields.io/github/downloads/YuiYukihira/EliteDangerousMaterialsTrader/total)

EDMT is a third-party tool that helps you calculate what the optimal materials are to trade to reach specific targets in Elite Dangerous.

## Installation

### Windows

Download the EDMT-setup-x.x.x.exe file from the [releases page](https://github.com/YuiYukihira/EliteDangerousMaterialsTrader/releases/latest). Run the installer and follow the prompts to install EDMT.

### Linux

#### Debian based distros

Download the EDMT-x.x.x.deb file from the [releases page](https://github.com/YuiYukihira/EliteDangerousMaterialsTrader/releases/latest).

#### Other distros

See [running from the source](#Running-from-the-source).

## How to use

1. Export a wishlist from EDOMH.
2. Start EDMT.
3. Click the "open wishlist" button and select your exported wishlist.
4. Wait for EDMT to do it's calculations
5. The left table is the trades to perform and the amount to do. The right table is any materials that EDMT thinks you'll need to complete your wishlist.

NOTE: EDMT does not currently automatically update your materials stock. to recalculate, please restart the application.

## Launch arguments

You can pass the following arguments when launching EDMT:

- `-j <path>`: Specify a custom path to the journal folder
  
## Running from the source

1. Install Python
2. Clone the repository (Python **3.12** is recommended):

```shell
git clone https://github.com/YuiYukihira/EliteDangerousMaterialsTrader
cd EliteDangerousMaterialsTrader
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Launch EDMT:

```
python main.py
```
