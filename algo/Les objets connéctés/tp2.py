"""
import network

# user data
ssid = "raspi-webgui" # wifi router name
pw = "touchardNSI" # wifi router password

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

# wait for connection
while not wifi.isconnected():
    pass

# wifi connected
print(wifi.ifconfig())
"""
"""
import network

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)

# wifi is connected ?
if wifi.isconnected():
    print ("connecté au réseau wifi")
    print(wifi.ifconfig())    
else:
    print (" NON connecté au réseau wifi")
"""
"""
import network
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
oled.fill(0)
oled.text("i2c", 0, 0)
oled.show()

# wifi is connected ?
print(wifi.ifconfig())
"""
import network
import urequests
import ujson
import utime

# user data
url = "http://worldtimeapi.org/api/timezone/Europe/Paris" 

# initialization

response = urequests.get(url)
    
if response.status_code == 200:
    worldtime = ujson.loads(response.text)
    print(type(worldtime))
    print(worldtime.keys())
    print(worldtime)
  
else:
    print("Pas de réponse")



