import DHT22
import pigpio     
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import sqlite3

import bme280

#ADC setup
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

lightADCChannel = 0
AirQualityADCChannel = 1

#DHT22 setup
pi = pigpio.pi()
dht22 = DHT22.sensor(pi, 4)

#LDR setup
LDRMIN = 200
LDRMAX = 820
LDRdiff = LDRMAX-LDRMIN

#DataBase setup
db = sqlite3.connect('data/data.db')

cursor = db.cursor()

#Try to create new table if one doesnt exist
try:
    cursor.execute('CREATE TABLE data(time text, temperature real, humidity real, air_quality real, light_level real, BMP280temperature, BMP280pressure)')
    db.commit()
except:
    "operationalError"

