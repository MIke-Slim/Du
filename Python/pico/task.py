from machine import Pin
led=Pin(25,Pin.OUT)

while True:
    led.value(1)
    