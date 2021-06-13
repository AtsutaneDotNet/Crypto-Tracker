# Crypto Tracker 2.0
Simple Bot to track balances, profit and performance using Python, SQLite, &amp; Flask

![tracker](https://user-images.githubusercontent.com/6040550/121795775-77864f80-cc46-11eb-8d59-a3d10dddc120.PNG)

# Crypto Tracker 2.0 Setup Guide

## Install Python:

https://www.python.org/downloads/

## Clone or Download Zip File Below:

https://github.com/AtsutaneDotNet/Crypto-Tracker/archive/master.zip

## Install Requirements via Windows Command Prompt:

```bash
pip install -r requirements.txt
```

## Edit Accounts to match Exchanges & Keys using a text editor

```
accounts.json
```
Currently tracking data from :-
- [x] Binance
- [x] Bybit
- [ ] Binance Smart Chain

UID will be insert automatically when script process the account list.

```json
[
    {
        "enable": "false",
        "exchange": "binance",
        "key": "",
        "secret": "",
        "uid": ""
    },
    {
        "enable": "false",
        "exchange": "bybit",
        "key": "",
        "secret": "",
        "uid": ""
    }
]
```

## Run tracker.py & Visit http://localhost:8000/ to view UI

open CMD prompt
cd C:path/toyour/directory
tracker.py

To view from outside source you must edit the tracker.py file to match your public IP & set a custom port using the code below, you then must open the port to outside traffic.

```python
app.run(host="0.0.0.0", port=8000)
```

## Credits
- [https://github.com/CryptoGnome/Crypto-Tracker] for The Orginal Crypto Tracker
- [https://github.com/ScavengerBot/CryptoFont] for Cryptocurrency Icon Font

## Donate To Crypto Tracker 2.0 Development
- ETH/USDT/ERC20: 0x4EF84bB3908EE77EA0B1f5BECB185804beC5352d
- BSC 0xaD687b24852Ae916Cfb740871768E7b214175729

## Donate to CryptoGnome - https://github.com/CryptoGnome
- ETH/USDT/ERC20: 0x647556545e529114B30E708dea09d64652e3c490
