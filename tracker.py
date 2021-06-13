import sqlite3
import ccxt
import datetime
from sqlite3 import OperationalError
from time import sleep
from colorama import init
from colorama import Fore,Style,Back
import uuid
import json
import threading
from flask import Flask, render_template, jsonify, Markup, redirect, url_for, request
from urllib.request import urlopen
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

init(autoreset=True)

#Tracker Core
def createTrackerDB():
    print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Creating " + Fore.GREEN + "Data Tracking" + Fore.WHITE + " Table")
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    c.execute('CREATE TABLE income (date text, wallet integer, wallet_usd integer, income integer, income_usd integer, pnl integer, commision integer, funding integer, cumulative integer, cumulative_usd integer, type text, exchange text, timestamp integer, uuid text)')
    conn.commit()
    conn.close()

def readTrackerDB():
    print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Reading " + Fore.GREEN + "Data Tracking" + Fore.WHITE + " Table")
    try:
        conn = sqlite3.connect('crypto.db')
        c = conn.cursor()
        c.execute('SELECT * FROM income')
        data = c.fetchall()
    except OperationalError as e:
        createTrackerDB()
        conn.commit()
        conn.close()

def getJsonFile(file):
    with open(file) as f:
        data = json.load(f)
    return data

def writeJsonFile(file,data):
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def getNowTimes():
    now = datetime.datetime.now()
    times = now.strftime("%m/%d/%Y %H:%M:%S")
    return times

def getSeperator():
    print("")
    print("========================== [" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] ==========================")

def getAccountInfo():
    print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Initiate " + Fore.GREEN + "Data Tracking" + Fore.WHITE + " Process")
    try:
        account = getJsonFile("accounts.json")
        info = []
        for data in account:
            if data['uid'] == '':
                data['uid'] = str(uuid.uuid1())[:8]
            if data['exchange'] == 'binance' and data['enable'] == 'true':
                getBinanceData(data['key'],data['secret'],data['uid'])
            elif data['exchange'] == 'bybit' and data['enable'] == 'true':
                getBybitData(data['key'],data['secret'],data['uid'])
            elif data['exchange'] == 'bsc' and data['enable'] == 'true':
                getBscData(data['key'],data['secret'],data['uid'])
            else:
                pass
            info.append(data)
        writeJsonFile("accounts.json",info)
        print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Complete " + Fore.GREEN + "Data Tracking" + Fore.WHITE + " Process")
    except Exception as e:
        print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] " + Fore.RED + "Warning!" + Fore.WHITE + " Data Tracking Error! "+str(e))

def getBinanceData(key,secret,uid):
    # https://binance-docs.github.io/apidocs/futures/en/#get-income-history-user_data
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    timestamp = datetime.datetime.now().timestamp() * 1000
    print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Process Binance Data: " + Fore.GREEN + uid)
    exchange_id = 'binance'
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'apiKey': key,
        'secret': secret,
        'timeout': 30000,
        'enableRateLimit': True,
        'option': {'defaultMarket': 'futures'}
    })
    accountInfo = exchange.fapiPrivateGetAccount()
    incomeInfo = exchange.fapiPrivateGetIncome({ 'limit': '1000' })
    wallet = float(accountInfo['totalWalletBalance'])
    income_value = 0
    pnl_value = 0
    comm_value = 0
    funding_value = 0
    cum_pnl = 0
    for profit in incomeInfo:
        time = datetime.datetime.fromtimestamp(int(profit['time']) / 1000).strftime("%d/%m/%Y")
        type = profit['asset']
        if time == today and profit['incomeType'] != 'TRANSFER':
            income_value = income_value + float(profit['income'])
            if profit['incomeType'] == 'REALIZED_PNL':
                pnl_value = pnl_value + float(profit['income'])
            elif profit['incomeType'] == 'COMMISSION':
                comm_value = comm_value + float(profit['income'])
            elif profit['incomeType'] == 'FUNDING_FEE':
                funding_value = funding_value + float(profit['income'])
            else:
                pass
    #Try to process cum pnl
    conn = sqlite3.connect('crypto.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    try:
        cum_data = c.execute('SELECT sum(income) FROM income WHERE type = ?',(type,)).fetchone()
        if cum_data[0] != None:
            cum_pnl = cum_data[0]
        else:
            pass
    except OperationalError as e:
        createTrackerDB()
        return
    except Exception as e:
        cum_data = c.execute('SELECT sum(income) FROM income WHERE type = ?',(type,)).fetchone()
        if cum_data[0] != None:
            cum_pnl = cum_data[0]
        else:
            pass
    conn.commit()
    conn.close()
    #Key In New Data
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM income')
        c.execute('DELETE FROM income WHERE date = ? AND uuid = ? AND type = ?', (today,uid,type,))
        c.execute('INSERT INTO income VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                  (today, round(wallet,2), round(wallet,2), round(income_value,2), round(income_value,2), round(pnl_value,2), round(comm_value,2), round(funding_value,2), round(cum_pnl,2), round(cum_pnl,2), type, exchange_id, timestamp, uid))
    except OperationalError as e:
        createTrackerDB()
        return
    except IndexError as e:
        c.execute('SELECT * FROM income')
        c.execute('DELETE FROM income WHERE date = ? AND uuid = ? AND type = ?', (today,uid,type,))
        c.execute('INSERT INTO income VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                  (today, round(wallet,2), round(wallet,2), round(income_value,2), round(income_value,2), round(pnl_value,2), round(comm_value,2), round(funding_value,2), round(cum_pnl,2), round(cum_pnl,2), type, exchange_id, timestamp, uid))
    conn.commit()
    conn.close()
    print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Complete " + Fore.GREEN + "Binance" + Fore.WHITE + " Data Tracking")

def getBybitData(key,secret,uid):
    # https://bybit-exchange.github.io/docs/inverse/#t-walletrecords
    timestamp = datetime.datetime.now().timestamp() * 1000
    print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Process Bybit Data: " + Fore.GREEN + uid)
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    exchange_id = 'bybit'
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'apiKey': key,
        'secret': secret,
        'timeout': 30000,
        'enableRateLimit': True
    })
    accountInfo = exchange.v2PrivateGetPositionList()
    getTickers = exchange.fetchTickers(['BTC/USD','ETH/USD','EOS/USD','XRP/USD'])
    incomeInfo = exchange.v2PrivateGetWalletFundRecords({ 'limit': '50' })
    income_type = ["RealisedPNL","Commission","Refund","Prize"]
    for account in accountInfo['result']:
        wallet = float(account['data']['wallet_balance'])
        type = account['data']['symbol'].replace("USD","")
        income_value = 0
        pnl_value = 0
        comm_value = 0
        funding_value = 0
        cum_pnl = 0
        for profit in incomeInfo['result']['data']:
            time = datetime.datetime.fromisoformat(profit['exec_time'].replace("Z", "+00:00")).strftime("%d/%m/%Y")
            if time == today and profit['coin'] == type and profit['type'] in income_type:
                income_value = income_value + float(profit['amount'])
                if profit['type'] == 'RealisedPNL':
                    pnl_value = pnl_value + float(profit['amount'])
                elif profit['type'] == 'Commission':
                    comm_value = comm_value + float(profit['amount'])
                elif profit['type'] == 'Refund':
                    funding_value = funding_value + float(profit['amount'])
                else:
                    pass
        ticker_symbol = type+"/USD"
        income_usd = income_value * getTickers[ticker_symbol]['last']
        wallet_usd = wallet * getTickers[ticker_symbol]['last']
        #Try to process cum pnl
        conn = sqlite3.connect('crypto.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        try:
            cum_data = c.execute('SELECT sum(income) FROM income WHERE type = ?',(type,)).fetchone()
            if cum_data[0] != None:
                cum_pnl = cum_data[0]
            else:
                pass
        except OperationalError as e:
            createTrackerDB()
            return
        except Exception as e:
            cum_data = c.execute('SELECT sum(income) FROM income WHERE type = ?',(type,)).fetchone()
            if cum_data[0] != None:
                cum_pnl = cum_data[0]
            else:
                pass
        cum_pnlusd = cum_pnl * getTickers[ticker_symbol]['last']
        conn.commit()
        conn.close()
        #Key In New Data
        conn = sqlite3.connect('crypto.db')
        c = conn.cursor()
        try:
            c.execute('SELECT * FROM income')
            c.execute('DELETE FROM income WHERE date = ? AND uuid = ? AND type = ?', (today,uid,type,))
            c.execute('INSERT INTO income VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                      (today, round(wallet,4), round(wallet_usd,2), round(income_value,4), round(income_usd,2), round(pnl_value,4), round(comm_value,4), round(funding_value,4), round(cum_pnl,4), round(cum_pnlusd,2), type, exchange_id, timestamp, uid))
        except OperationalError as e:
            createTrackerDB()
            return
        except IndexError as e:
            c.execute('SELECT * FROM income')
            c.execute('DELETE FROM income WHERE date = ? AND uuid = ? AND type = ?', (today,uid,type,))
            c.execute('INSERT INTO income VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                      (today, round(wallet,4), round(wallet_usd,2), round(income_value,4), round(income_usd,2), round(pnl_value,4), round(comm_value,4), round(funding_value,4), round(cum_pnl,4), round(cum_pnlusd,2), type, exchange_id, timestamp, uid))
        conn.commit()
        conn.close()
    print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Complete " + Fore.GREEN + "Bybit" + Fore.WHITE + " Data Tracking")
#Tracker Core

#Journal Core
# trade_id = https://binance-docs.github.io/apidocs/futures/en/#get-income-history-user_data
# order_id = https://binance-docs.github.io/apidocs/futures/en/#account-trade-list-user_data
# trade_entry_point = https://binance-docs.github.io/apidocs/futures/en/#all-orders-user_data

#flask Core
@app.route("/")
def index():
    data_output = []
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    conn = sqlite3.connect('crypto.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    data = c.execute('SELECT * FROM income WHERE date = ?',(today,)).fetchall()
    dates = c.execute('SELECT date FROM income GROUP BY date ORDER BY date LIMIT 30').fetchall()
    usdt = c.execute('SELECT cumulative_usd FROM income WHERE type = ? ORDER BY date LIMIT 30',("USDT",)).fetchall()
    btc = c.execute('SELECT cumulative_usd FROM income WHERE type = ? ORDER BY date LIMIT 30',("BTC",)).fetchall()
    eth = c.execute('SELECT cumulative_usd FROM income WHERE type = ? ORDER BY date LIMIT 30',("ETH",)).fetchall()
    eos = c.execute('SELECT cumulative_usd FROM income WHERE type = ? ORDER BY date LIMIT 30',("EOS",)).fetchall()
    xrp = c.execute('SELECT cumulative_usd FROM income WHERE type = ? ORDER BY date LIMIT 30',("XRP",)).fetchall()
    sum_cum = c.execute('SELECT sum(cumulative_usd) FROM income GROUP BY date ORDER BY date LIMIT 30').fetchall()
    sum_all = c.execute('SELECT sum(wallet_usd) FROM income WHERE date = ?',(today,)).fetchone()
    sum_pnl = c.execute('SELECT sum(income_usd) FROM income WHERE date = ?',(today,)).fetchone()
    conn.commit()
    conn.close()
    return render_template('tracker.html',data=data,dates=dates,usdt=usdt,btc=btc,eth=eth,eos=eos,xrp=xrp,sum_all=sum_all,sum_pnl=sum_pnl,sum_cum=sum_cum)
#flask Core

def tracker_worker():
    sleep(3)
    while True:
        getSeperator()
        getAccountInfo()
        print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Complete " + Fore.GREEN + "Data Tracking" + Fore.WHITE + " Sleep For 60 Seconds")
        sleep(60)

#Main Apps
if __name__ == '__main__':
    try:
        worker_thread = threading.Thread(target=tracker_worker, name='myworker', daemon=True)
        worker_thread.start()
        app.run(host="localhost", port=8000)
    except KeyboardInterrupt:
        print("[" + Fore.CYAN + getNowTimes() + Fore.WHITE + "] Stopping " + Fore.GREEN + "Data Tracking")
