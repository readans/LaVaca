#Envia temperatura y humedad a Drive a traves de ifttA
#https://ifttt.com/maker_webhooks

import network, time, urequests
from machine import Pin

def conectaWifi(red, password):
     global miRed
     miRed = network.WLAN(network.STA_IF)     
     if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
     return True

sensor = Pin(4, Pin.IN)
led = Pin(2, Pin.OUT)

if conectaWifi("Wilpec", "73407340"):

    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/hand_up/with/key/bdbzFUxBnxLA7X7BzT59zq"  
    
    while (True):
        dato = sensor.value()
        time.sleep(1)
        if (dato):
            print(dato)
            urequests.request('GET', url)
 
else:
       print ("Imposible conectar")
       miRed.active (False)