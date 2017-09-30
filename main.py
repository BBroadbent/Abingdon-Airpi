# -*- coding: utf-8 -*-

#YOU NEED TO START PIGPIO SERVICE WITH 'SUDO PIGPIOD'

from AbAirpiSetup import *

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
        lightRaw = mcp.read_adc(lightADCChannel)
        lightCalculated = (lightRaw - LDRMIN)*100 / LDRdiff
        airqualityRaw = mcp.read_adc(AirQualityADCChannel)
        BMP280temperature,pressure, humiditybmp280 = bme280.readBME280All()

        dataArray = ['data',DHT22temperature,DHT22humidity,airqualityRaw,lightCalculated,BMP280temperature,pressure]
        
        cursor.execute("INSERT INTO {0} VALUES (datetime('now'),{1},{2},{3},{4},{5},{6})".\
                               format(*dataArray))
        
        cursor.execute("SELECT * FROM data ORDER BY time DESC LIMIT 1")
        lastrow = cursor.fetchone()
        print ("Temprerature: {5:0.1f}°C Humidity: {2}% Air Quality: {3} Light: {4}% Barometric Pressure: {6:0.1f} mBar".\
            format(*dataArray))
        
        db.commit()
        time.sleep(1)
        
writetoSQLite()
