# -*- coding: utf-8 -*-

import sys
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from mainwindow import Ui_MainWindow

import requests
import json
import os
from datetime import datetime


def from_ts_to_time_of_day(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%I%p").lstrip("0")



class Weather_worker(QMainWindow):
    def __init__(self, title="Default", parent=None):
        super(Weather_worker, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.title = title
        self.ui.setupUi(self)
        self.setWindowTitle(self.title)
        self.api_key = ""
        self.lon = 0
        self.lat = 0
        self.ui.pushButton.setIcon(QIcon('images/arrow-circle-225.png'))
        self.threadpool = QThreadPool()
        self.ui.pushButton.clicked.connect(self.location)

    def entry(self):
        var = self.ui.lineEdit_2.text()
        return var


    def test(self):
        rec = self.entry()
        url = "http://api.openweathermap.org/data/2.5/weather?q=%s&lang=fr&units=metric&appid=%s" % (rec,self.api_key)
        content = requests.get(url)
        data = content.json()
        meteo = json.dumps(data)
        t = data['main']['temp']
        print("La témpérature est de {} degrés C".format(t))
        self.lat = data['main']['pressure']
        self.lon = data['main']['humidity']
        contry = data['sys']['country']
        city = data['name']
        wind = data['wind']['speed']
        description = data['weather'][0]['description']
        self.ui.temperature.setText(str(t )+"°C\n\n"+str(description))
        self.ui.temperature.setMaximumSize(200, 100)
        img = data['weather'][0]['icon']
        self.ui.image.setPixmap(
            QPixmap(os.path.join('images', "%s.png"%img )))
        self.ui.label_5.setText(contry+"/"+city)
        self.ui.longitude.setText(str(self.lat))
        self.ui.latitude.setText(str(self.lon)+ " %")
        self.ui.vent.setText(str(wind)+ " Km/h")
        print(data)
        with open('temps.json', 'w') as m:
            m.write(meteo)
        return data

    def location(self):
        lond = self.test()
        lon = lond['coord']['lon']
        lat = lond['coord']['lat']
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=munitely&units=metric&appid=%s" % (lat, lon, self.api_key)
        content = requests.get(url)
        data = content.json()
        meteo = json.dumps(data)
        hourly = data['hourly'][0]['temp']
        hourly2 = data['hourly'][1]['temp']
        hourly3 = data['hourly'][2]['temp']
        hourly4 = data['hourly'][3]['temp']
        hourly5 = data['hourly'][4]['temp']
        #dt = datetime.fromtimestamp(data['hourly'][0]['dt'])
        #s =dt.strftime("%I%p").lstrip("0")
        s=from_ts_to_time_of_day(data['hourly'][0]['dt'])
        self.ui.hour_1.setText(str(s)+"H")
        fc = str(hourly) + '°C'
        self.ui.label_13.setText(str(fc))
        img = data['hourly'][0]['weather'][0]['icon']
        print(img)
        urls = "http://openweathermap.org/img/wn/%s@2x.png" %(img)
        cont = requests.get(urls).content
        print(cont)
        #self.ui.label_8.setPixmap(QPixmap(str(cont)))
        self.ui.label_8.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 img
                                 )))

        f = str(hourly2) +'°C'
        self.ui.label_14.setText(f)
        imgs = data['hourly'][1]['weather'][0]['icon']
        urlss = "http://openweathermap.org/img/wn/%s@2x.png" % (imgs)
        conts = requests.get(urlss).content
        print(conts)
        #dts = datetime.fromtimestamp(data['hourly'][1]['dt'])
        #n = dts.strftime("%I%p").lstrip("0")
        n= from_ts_to_time_of_day(data['hourly'][1]['dt'])
        self.ui.hour_2.setText(str(n) + "H")
        self.ui.label_9.setPixmap(QPixmap(str(conts)))
        self.ui.label_9.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 imgs
                                 )))


        bc = str(hourly3) + '°C'
        self.ui.label_15.setText(bc)
        self.ui.label_14.setText(f)
        #dte = datetime.fromtimestamp(data['hourly'][3]['dt'])
        #ns = dte.strftime("%I%p").lstrip("0")
        ns = from_ts_to_time_of_day(data['hourly'][2]['dt'])
        self.ui.hour_3.setText(str(ns) + "H")
        imgss = data['hourly'][2]['weather'][0]['icon']
        urlsss = "http://openweathermap.org/img/wn/%s@2x.png" % (imgss)
        contss = requests.get(urlsss).content
        self.ui.label_10.setPixmap(QPixmap(str(cont)))
        self.ui.label_10.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 imgss
                                 )))



        sc = str(hourly4) + '°C'
        self.ui.label_16.setText(sc)
        self.ui.label_14.setText(f)
        #dtc = datetime.fromtimestamp(data['hourly'][4]['dt'])
        #se = dtc.strftime("%I%p").lstrip("0")
        se = from_ts_to_time_of_day(data['hourly'][3]['dt'])
        self.ui.hour_4.setText(str(se) + "H")
        imgse = data['hourly'][4]['weather'][0]['icon']
        urlsse = "http://openweathermap.org/img/wn/%s@2x.png" % (imgse)
        contse = requests.get(urlsse).content
        self.ui.label_11.setPixmap(QPixmap(str(contse)))
        self.ui.label_11.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 imgse
                                 )))

        fcc = str(hourly5) + '°C'
        self.ui.label_17.setText(fcc)
        self.ui.label_14.setText(f)
        #dtv = datetime.fromtimestamp(data['hourly'][5]['dt'])
        #si = dtv.strftime("%I%p").lstrip("0")
        si = from_ts_to_time_of_day(data['hourly'][5]['dt'])
        self.ui.hour_5.setText(str(si) + "H")
        im = data['hourly'][4]['weather'][0]['icon']
        ur = "http://openweathermap.org/img/wn/%s@2x.png" % (im)
        cons = requests.get(ur).content
        self.ui.label_12.setPixmap(QPixmap(str(cont)))
        self.ui.label_12.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 im
                                 )))
        print(hourly)
        #self.ui.hour_1.setText(str(time))
        print(data)
        with open('meteo.json', 'w') as m:
            m.write(meteo)




if  __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Weather_worker('weaher')
    style = """
         QWidget{
            
           
            background:  #262D37;
        }
         QPushButton
        {
            color: white;
            background: #0577a8;
            border: 1px #DADADA solid;
            padding: 5px 10px;
            border-radius: 2px;
            font-weight: bold;
            font-size: 9pt;
            outline: none;
        }

        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #0892D0;
            }
        QLabel{
            color: orange;
        }
           QLabel#label_2{
           
        }
         QLabel#label_3{
            
        }
        
         QLabel#label_4{
    
        }
          QLabel#hour_1{
            background: yellow;
            color: blue;
        }
          QLabel#hour_2{
            background: yellow;
            color: blue;
        }
          QLabel#hour_3{
            background: yellow;
            color: blue;
        }
          QLabel#hour_4{
            background: yellow;
            color: blue;
        }
          QLabel#hour_5{
            background: yellow;
            color: blue;
        }

         QLabel#temperature{
            color: orange;
    
            
            
        }
        
        QLabel#label{
            background: gray;
            color: greenyellow;
            font-family:sans-serif;
 
        }
          QLabel#label_5{
            padding: 40px
 
        }
        QLabel#longitude{
           color: yellow;
        }
        QLabel#latitude{
           color: yellow;
        }
        QLabel#vent{
           color: yellow;
        }
          QLineEdit {
            padding: 1px;
            color: #fff;
            border-style: solid;
            border: 2px solid #fff;
            border-radius: 8px;
        }

        
         

    """
    app.setStyleSheet(style)
    window.show()
    sys.exit(app.exec_())
