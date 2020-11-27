from flask import Flask, render_template, jsonify, Markup
import sqlite3
import datetime
from accounts import *


app = Flask(__name__)



@app.route("/")
def index():

    try:
        print("Checking for Todays Data")

        if use_account1 == True:
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account1')
            datas = c.fetchall()
            data = datas[-1]
            today = round(data[2], 2)
            pnl = round(data[3], 2)
            daily = round(data[4], 2)
            nickname1 = data[5]
            conn.commit()
            conn.close()


            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlData = c.execute('SELECT sum(pnl) FROM account1 WHERE rowid > 1').fetchall()
            spnl = round(pnlData[0], 2)
            pnlAllData1 = c.execute('SELECT today FROM account1 WHERE rowid > 1').fetchall()
            percentData = c.execute('SELECT sum(daily) FROM account1 WHERE rowid > 1').fetchall()
            spct = round(percentData[0], 2)
            percentAllData = c.execute('SELECT daily FROM account1 ').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account1 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account1 WHERE rowid > 1').fetchall()
            apnl = round(averagePNL[0], 2)
            apct = round(averagePCT[0], 2)
            dateData = c.execute('SELECT date FROM account1 WHERE rowid > 1')
            dates1 = c.fetchall()
            conn.commit()
            conn.close()

        else:
            today1 = 0
            pnl1 = 0
            daily1 = 0
            nickname1 = 'EMPTY'
            pnlAllData1  = [0,]
            dates1 = ['NO_DATA']
            values1 = [0,]
            spnl = 0
            spct = 0
            apnl = 0
            apct = 0

        if use_account2 == True:
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account2')
            datas2 = c.fetchall()
            data2 = datas2[-1]
            today2 = round(data2[2], 2)
            pnl2 = round(data2[3], 2)
            daily2 = round(data2[4], 2)
            nickname2 = data2[5]
            conn.commit()
            conn.close()

            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlData = c.execute('SELECT sum(pnl) FROM account2 WHERE rowid > 1').fetchall()
            spnl2 = round(pnlData[0], 2)
            pnlAllData2 = c.execute('SELECT today FROM account2 WHERE rowid > 1').fetchall()
            percentData = c.execute('SELECT sum(daily) FROM account2 WHERE rowid > 1').fetchall()
            spct2 = round(percentData[0], 2)
            percentAllData = c.execute('SELECT daily FROM account2').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account2 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account2 WHERE rowid > 1').fetchall()
            apnl2 = round(averagePNL[0], 2)
            apct2 = round(averagePCT[0], 2)
            dates2 = c.execute('SELECT date FROM account2 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()

        else:
            today2 = 0
            pnl2 = 0
            daily2 = 0
            nickname2 = 'EMPTY'
            pnlAllData2  = [0,]
            dates2 = ['NO_DATA']
            values2 = [0,]
            spnl2 = 0
            spct2 = 0
            apnl2 = 0
            apct2 = 0

        if use_account3 == True:
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account3')
            datas3 = c.fetchall()
            data3 = datas3[-1]
            today3 = round(data3[2], 2)
            pnl3 = round(data3[3], 2)
            daily3 = round(data3[4], 2)
            nickname3 = data3[5]
            conn.commit()
            conn.close()

            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlData = c.execute('SELECT sum(pnl) FROM account3 WHERE rowid > 1').fetchall()
            spnl3 = round(pnlData[0], 2)
            pnlAllData3 = c.execute('SELECT today FROM account3 WHERE rowid > 1').fetchall()
            percentData = c.execute('SELECT sum(daily) FROM account3 WHERE rowid > 1').fetchall()
            spct3 = round(percentData[0], 2)
            percentAllData = c.execute('SELECT daily FROM account3').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account3 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account3 WHERE rowid > 1').fetchall()
            apnl3 = round(averagePNL[0], 2)
            apct3 = round(averagePCT[0], 2)
            dates3 = c.execute('SELECT date FROM account3 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()

        else:
            today3 = 0
            pnl3 = 0
            daily3 = 0
            nickname3 = 'EMPTY'
            pnlAllData3  = [0,]
            dates3 = ['NO_DATA']
            values3 = [0,]
            spnl3 = 0
            spct3 = 0
            apnl3 = 0
            apct3 = 0

        if use_account4 == True:
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account4')
            datas4 = c.fetchall()
            data4 = datas4[-1]
            today4 = round(data4[2], 2)
            pnl4 = round(data4[3], 2)
            daily4 = round(data4[4], 2)
            nickname4 = data4[5]
            conn.commit()
            conn.close()

            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlData = c.execute('SELECT sum(pnl) FROM account4 WHERE rowid > 1').fetchall()
            spnl4 = round(pnlData[0], 2)
            pnlAllData4 = c.execute('SELECT today FROM account4 WHERE rowid > 1').fetchall()
            percentData = c.execute('SELECT sum(daily) FROM account4 WHERE rowid > 1').fetchall()
            spct4 = round(percentData[0], 2)
            percentAllData = c.execute('SELECT daily FROM account4').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account4 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account4 WHERE rowid > 1').fetchall()
            apnl4 = round(averagePNL[0], 2)
            apct4 = round(averagePCT[0], 2)
            dates4 = c.execute('SELECT date FROM account4 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()

        else:
            today4 = 0
            pnl4 = 0
            daily4 = 0
            nickname4 = 'EMPTY'
            pnlAllData4  = [0,]
            dates4 = ['NO_DATA']
            values4 = [0,]
            spnl4 = 0
            spct4 = 0
            apnl4 = 0
            apct4 = 0

        if use_account5 == True:
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account5')
            datas5 = c.fetchall()
            data5 = datas5[-1]
            today5 = round(data5[2], 2)
            pnl5 = round(data5[3], 2)
            daily5 = round(data5[4], 2)
            nickname5 = data5[5]
            conn.commit()
            conn.close()

            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlData = c.execute('SELECT sum(pnl) FROM account5 WHERE rowid > 1').fetchall()
            spnl5 = round(pnlData[0], 2)
            pnlAllData5 = c.execute('SELECT today FROM account5 WHERE rowid > 1').fetchall()
            percentData = c.execute('SELECT sum(daily) FROM account5 WHERE rowid > 1').fetchall()
            spct5 = round(percentData[0], 2)
            percentAllData = c.execute('SELECT daily FROM account5').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account5 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account5 WHERE rowid > 1').fetchall()
            apnl5 = round(averagePNL[0], 2)
            apct5 = round(averagePCT[0], 2)
            dates5 = c.execute('SELECT date FROM account5 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()
        else:
            today5 = 0
            pnl5 = 0
            daily5 = 0
            nickname5 = 'EMPTY'
            pnlAllData5  = [0,]
            dates5 = ['NO_DATA']
            values5 = [0,]
            spnl5 = 0
            spct5 = 0
            apnl5 = 0
            apct5 = 0

        if use_account6 == True:
            conn = sqlite3.connect('tracker.db')
            c = conn.cursor()
            c.execute('SELECT * FROM account6')
            datas6 = c.fetchall()
            data6 = datas6[-1]
            today6 = round(data6[2], 2)
            pnl6 = round(data6[3], 2)
            daily6 = round(data6[4], 2)
            nickname6 = data6[5]
            conn.commit()
            conn.close()

            #charts
            conn = sqlite3.connect('tracker.db')
            conn.row_factory = lambda cursor, row: row[0]
            c = conn.cursor()
            pnlData = c.execute('SELECT sum(pnl) FROM account6 WHERE rowid > 1').fetchall()
            spnl6 = round(pnlData[0], 2)
            pnlAllData6 = c.execute('SELECT today FROM account6 WHERE rowid > 1').fetchall()
            percentData = c.execute('SELECT sum(daily) FROM account6 WHERE rowid > 1').fetchall()
            spct6 = round(percentData[0], 2)
            percentAllData = c.execute('SELECT daily FROM account6').fetchall()
            averagePNL = c.execute('SELECT avg(pnl) FROM account6 WHERE rowid > 1').fetchall()
            averagePCT = c.execute('SELECT avg(daily) FROM account6 WHERE rowid > 1').fetchall()
            apnl6 = round(averagePNL[0], 2)
            apct6 = round(averagePCT[0], 2)
            dates6 = c.execute('SELECT date FROM account6 WHERE rowid > 1').fetchall()
            conn.commit()
            conn.close()
        else:
            today6 = 0
            pnl6 = 0
            daily6 = 0
            nickname6 = 'EMPTY'
            pnlAllData6  = [0,]
            dates6 = ['NO_DATA']
            values6 = [0,]
            spnl6 = 0
            spct6 = 0
            apnl6 = 0
            apct6 = 0



        return render_template('index.html', today=today, pnl=pnl, daily=daily, nickname1=nickname1, today2=today2, pnl2=pnl2, daily2=daily2, nickname2=nickname2,today3=today3, pnl3=pnl3, daily3=daily3,
                                nickname3=nickname3, today4=today4, pnl4=pnl4, daily4=daily4, nickname4=nickname4, today5=today5, pnl5=pnl5, daily5=daily5, nickname5=nickname5,
                                today6=today6, pnl6=pnl6, daily6=daily6, nickname6=nickname6,
                               max1=(pnlAllData1[-1] * 2), labels1=dates1, values1=pnlAllData1, allpnl=spnl, allpct=spct, avgpnl=apnl, avgpct=apct,
                               max2=(pnlAllData2[-1] * 2), labels2=dates2, values2=pnlAllData2, allpnl2=spnl2, allpct2=spct2, avgpnl2=apnl2, avgpct2=apct2,
                               max3=(pnlAllData3[-1] * 2), labels3=dates3, values3=pnlAllData3, allpnl3=spnl3, allpct3=spct3, avgpnl3=apnl3, avgpct3=apct3,
                               max4=(pnlAllData4[-1] * 2), labels4=dates4, values4=pnlAllData4, allpnl4=spnl4, allpct4=spct4, avgpnl4=apnl4, avgpct4=apct4,
                               max5=(pnlAllData5[-1] * 2), labels5=dates5, values5=pnlAllData5, allpnl5=spnl5, allpct5=spct5, avgpnl5=apnl5, avgpct5=apct5,
                               max6=(pnlAllData6[-1] * 2), labels6=dates6, values6=pnlAllData6, allpnl6=spnl6, allpct6=spct6, avgpnl6=apnl6, avgpct6=apct6)




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
