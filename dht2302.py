import adafruit_dht
import board
import time

dht = adafruit_dht.DHT22(board.D4)

while True:
    try:
        humidity = dht.humidity
        temperature = dht.temperature
        print('Humidity', humidity, 'Temperatur', temperature)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1)
        continue
    
    except Exception as error:
        dht.exit()
        raise error
    
    time.sleep(1)