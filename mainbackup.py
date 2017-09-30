import DHT22
import pigpio     #YOU NEED TO START PIGPIO SERVICE WITH 'SUDO PIGPIOD'
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import sqlite3

import bme280

db = sqlite3.connect('data/data.db')

cursor = db.cursor()

#Try to create new table if one doesnt exist
try:
    cursor.execute('CREATE TABLE data(time text, temperature real, humidity real, air_quality real, light_level real, BMP280temperature, BMP280pressure)')
    db.commit()
except:
    "operationalError"

#ADC setup
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#DHT22 setup
pi = pigpio.pi()
dht22 = DHT22.sensor(pi, 4)

print("AIRPI SYSTEM")
def getDHT22Temperature():
    dht22.trigger()
    time.sleep(0.01)
    return dht22.temperature()
   
def getDHT22Humidity():
    dht22.trigger()
    return dht22.humidity()

def writetoSQLite():
    while True:
        DHT22temperature = getDHT22Temperature()
        DHT22humidity = getDHT22Humidity()
        light = mcp.read_adc(0)
        airquality = mcp.read_adc(1)
        BMP280temperature,pressure, humiditybmp280 = bme280.readBME280All()

        dataArray = ["data",DHT22temperature,DHT22humidity,airquality,light,BMP280temperature,pressure]
        
        cursor.execute("INSERT INTO {0} VALUES (datetime('now'),{1},{2},{3},{4},{5},{6})".\
                               format(*dataArray))

        cursor.execute("SELECT * FROM data ORDER BY time DESC LIMIT 1")
        lastrow = cursor.fetchone()
        print (dataArray)
        
        db.commit()
        time.sleep(1)
        
writetoSQLite()
