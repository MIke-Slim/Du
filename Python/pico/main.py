from machine import Pin
from utime import sleep
import utime

led = Pin(25, Pin.OUT)

if __name__ == '__main__':
    while True:
        # led点亮
        led.value(1)
        utime.sleep_ms(1000)
        # led熄灭
        led.value(0)
        utime.sleep_ms(10000)
