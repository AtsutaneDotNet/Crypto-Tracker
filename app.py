from flask import Flask, render_template, jsonify, Markup
import sqlite3
import datetime
from accounts import *

app = Flask(__name__)

@app.route("/")
def index():
    try:
        print("Checking for Todays Data")
        #Account 1
        if use_account1 == True:
            #statistic
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account1')
            datas = c.fetchall()
            data = datas[-1]
            today = round(data[2], 4)
            pnl = round(data[3], 4)
            daily = round(data[4], 2)
            nickname1 = data[6]
            spnl = round(today - start1, 4)
            spct = round(data[5], 2)
            conn.commit()
            conn.close()
            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlAllData1 = c.execute('SELECT today FROM account1 WHERE rowid > 1').fetchall()
            pctAllData1 = c.execute('SELECT overall FROM account1 WHERE rowid > 1').fetchall()
            dailyAllData1 = c.execute('SELECT pnl FROM account1 WHERE rowid > 1').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account1 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account1 WHERE rowid > 1').fetchall()
            apnl = round(averagePNL[0], 4)
            apct = round(averagePCT[0], 2)
            dateData = c.execute('SELECT date FROM account1 WHERE rowid > 1')
            dates1 = c.fetchall()
            conn.commit()
            conn.close()
            panel1 = ''
        else:
            today1 = 0
            pnl1 = 0
            daily1 = 0
            nickname1 = 'EMPTY'
            pnlAllData1  = [0,]
            pctAllData1  = [0,]
            dailyAllData1  = [0,]
            dates1 = ['NO_DATA']
            values1 = [0,]
            spnl = 0
            spct = 0
            apnl = 0
            apct = 0
            panel1 = 'w3-hide'

        #Account 2
        if use_account2 == True:
            #statistic
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account2')
            datas2 = c.fetchall()
            data2 = datas2[-1]
            today2 = round(data2[2], 4)
            pnl2 = round(data2[3], 4)
            daily2 = round(data2[4], 2)
            nickname2 = data2[6]
            spnl2 = round(today2 - start2, 4)
            spct2 = round(data2[5], 2)
            conn.commit()
            conn.close()
            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlAllData2 = c.execute('SELECT today FROM account2 WHERE rowid > 1').fetchall()
            pctAllData2 = c.execute('SELECT overall FROM account2 WHERE rowid > 1').fetchall()
            dailyAllData2 = c.execute('SELECT pnl FROM account2 WHERE rowid > 1').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account2 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account2 WHERE rowid > 1').fetchall()
            apnl2 = round(averagePNL[0], 4)
            apct2 = round(averagePCT[0], 2)
            dates2 = c.execute('SELECT date FROM account2 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()
            panel2 = ''
        else:
            today2 = 0
            pnl2 = 0
            daily2 = 0
            nickname2 = 'EMPTY'
            pnlAllData2  = [0,]
            pctAllData2  = [0,]
            dailyAllData2  = [0,]
            dates2 = ['NO_DATA']
            values2 = [0,]
            spnl2 = 0
            spct2 = 0
            apnl2 = 0
            apct2 = 0
            panel2 = 'w3-hide'

        #Account 3
        if use_account3 == True:
            #statistic
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account3')
            datas3 = c.fetchall()
            data3 = datas3[-1]
            today3 = round(data3[2], 4)
            pnl3 = round(data3[3], 4)
            daily3 = round(data3[4], 2)
            nickname3 = data3[6]
            spnl3 = round(today3 - start3, 4)
            spct3 = round(data3[5], 2)
            conn.commit()
            conn.close()
            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlAllData3 = c.execute('SELECT today FROM account3 WHERE rowid > 1').fetchall()
            pctAllData3 = c.execute('SELECT overall FROM account3 WHERE rowid > 1').fetchall()
            dailyAllData3 = c.execute('SELECT pnl FROM account3 WHERE rowid > 1').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account3 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account3 WHERE rowid > 1').fetchall()
            apnl3 = round(averagePNL[0], 4)
            apct3 = round(averagePCT[0], 2)
            dates3 = c.execute('SELECT date FROM account3 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()
            panel3 = ''
        else:
            today3 = 0
            pnl3 = 0
            daily3 = 0
            nickname3 = 'EMPTY'
            pnlAllData3  = [0,]
            pctAllData3  = [0,]
            dailyAllData3  = [0,]
            dates3 = ['NO_DATA']
            values3 = [0,]
            spnl3 = 0
            spct3 = 0
            apnl3 = 0
            apct3 = 0
            panel3 = 'w3-hide'

        #Account 4
        if use_account4 == True:
            #statistic
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account4')
            datas4 = c.fetchall()
            data4 = datas4[-1]
            today4 = round(data4[2], 4)
            pnl4 = round(data4[3], 4)
            daily4 = round(data4[4], 2)
            nickname4 = data4[6]
            spnl4 = round(today4 - start4, 4)
            spct4 = round(data4[5], 2)
            conn.commit()
            conn.close()
            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlAllData4 = c.execute('SELECT today FROM account4 WHERE rowid > 1').fetchall()
            pctAllData4 = c.execute('SELECT overall FROM account4 WHERE rowid > 1').fetchall()
            dailyAllData4 = c.execute('SELECT pnl FROM account4 WHERE rowid > 1').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account4 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account4 WHERE rowid > 1').fetchall()
            apnl4 = round(averagePNL[0], 4)
            apct4 = round(averagePCT[0], 2)
            dates4 = c.execute('SELECT date FROM account4 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()
            panel4 = ''
        else:
            today4 = 0
            pnl4 = 0
            daily4 = 0
            nickname4 = 'EMPTY'
            pnlAllData4  = [0,]
            pctAllData4  = [0,]
            dailyAllData4  = [0,]
            dates4 = ['NO_DATA']
            values4 = [0,]
            spnl4 = 0
            spct4 = 0
            apnl4 = 0
            apct4 = 0
            panel4 = 'w3-hide'

        #Account 5
        if use_account5 == True:
            #statistic
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account5')
            datas5 = c.fetchall()
            data5 = datas5[-1]
            today5 = round(data5[2], 4)
            pnl5 = round(data5[3], 4)
            daily5 = round(data5[4], 2)
            nickname5 = data5[6]
            spnl5 = round(today5 - start5, 4)
            spct5 = round(data5[5], 2)
            conn.commit()
            conn.close()
            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlAllData5 = c.execute('SELECT today FROM account5 WHERE rowid > 1').fetchall()
            pctAllData5 = c.execute('SELECT overall FROM account5 WHERE rowid > 1').fetchall()
            dailyAllData5 = c.execute('SELECT pnl FROM account5 WHERE rowid > 1').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account5 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account5 WHERE rowid > 1').fetchall()
            apnl5 = round(averagePNL[0], 4)
            apct5 = round(averagePCT[0], 2)
            dates5 = c.execute('SELECT date FROM account5 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()
            panel5 = ''
        else:
            today5 = 0
            pnl5 = 0
            daily5 = 0
            nickname5 = 'EMPTY'
            pnlAllData5  = [0,]
            pctAllData5  = [0,]
            dailyAllData5  = [0,]
            dates5 = ['NO_DATA']
            values5 = [0,]
            spnl5 = 0
            spct5 = 0
            apnl5 = 0
            apct5 = 0
            panel5 = 'w3-hide'

        #Account 6
        if use_account6 == True:
            #statistic
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account6')
            datas6 = c.fetchall()
            data6 = datas6[-1]
            today6 = round(data6[2], 4)
            pnl6 = round(data6[3], 4)
            daily6 = round(data6[4], 2)
            nickname6 = data6[6]
            spnl6 = round(today6 - start6, 4)
            spct6 = round(data6[5], 2)
            conn.commit()
            conn.close()
            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlAllData6 = c.execute('SELECT today FROM account6 WHERE rowid > 1').fetchall()
            pctAllData6 = c.execute('SELECT overall FROM account6 WHERE rowid > 1').fetchall()
            dailyAllData6 = c.execute('SELECT pnl FROM account6 WHERE rowid > 1').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account6 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account6 WHERE rowid > 1').fetchall()
            apnl6 = round(averagePNL[0], 4)
            apct6 = round(averagePCT[0], 2)
            dates6 = c.execute('SELECT date FROM account6 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()
            panel6 = ''
        else:
            today6 = 0
            pnl6 = 0
            daily6 = 0
            nickname6 = 'EMPTY'
            pnlAllData6  = [0,]
            pctAllData6  = [0,]
            dailyAllData6  = [0,]
            dates6 = ['NO_DATA']
            values6 = [0,]
            spnl6 = 0
            spct6 = 0
            apnl6 = 0
            apct6 = 0
            panel6 = 'w3-hide'

        return render_template('index.html',
                panel1=panel1, start=start1, today=today, pnl=pnl, daily=daily, nickname1=nickname1, allpnl=spnl, allpct=spct, avgpnl=apnl, avgpct=apct,
                panel2=panel2, start2=start2, today2=today2, pnl2=pnl2, daily2=daily2, nickname2=nickname2, allpnl2=spnl2, allpct2=spct2, avgpnl2=apnl2, avgpct2=apct2,
                panel3=panel3, start3=start3, today3=today3, pnl3=pnl3, daily3=daily3, nickname3=nickname3, allpnl3=spnl3, allpct3=spct3, avgpnl3=apnl3, avgpct3=apct3,
                panel4=panel4, start4=start4, today4=today4, pnl4=pnl4, daily4=daily4, nickname4=nickname4, allpnl4=spnl4, allpct4=spct4, avgpnl4=apnl4, avgpct4=apct4,
                panel5=panel5, start5=start5, today5=today5, pnl5=pnl5, daily5=daily5, nickname5=nickname5, allpnl5=spnl5, allpct5=spct5, avgpnl5=apnl5, avgpct5=apct5,
                panel6=panel6, start6=start6, today6=today6, pnl6=pnl6, daily6=daily6, nickname6=nickname6, allpnl6=spnl6, allpct6=spct6, avgpnl6=apnl6, avgpct6=apct6,
                labels1=dates1, values1=pnlAllData1, values1a=pctAllData1, values1b=dailyAllData1,
                labels2=dates2, values2=pnlAllData2, values2a=pctAllData2, values2b=dailyAllData2,
                labels3=dates3, values3=pnlAllData3, values3a=pctAllData3, values3b=dailyAllData3,
                labels4=dates4, values4=pnlAllData4, values4a=pctAllData4, values4b=dailyAllData4,
                labels5=dates5, values5=pnlAllData5, values5a=pctAllData5, values5b=dailyAllData5,
                labels6=dates6, values6=pnlAllData6, values6a=pctAllData6, values6b=dailyAllData6)

    except TypeError as missing_data:
        print(missing_data)
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)

#heroku login
#cd C:\Users\oimap\Desktop\whalebotgui
#git add .
#git commit -m "note here"
#git push heroku master
