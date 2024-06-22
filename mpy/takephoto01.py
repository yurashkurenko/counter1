import os
import camera
import machine
import time

def run(tfile):
    led = machine.Pin(4, machine.Pin.OUT)
    camera.init()
    led.on()
    time.sleep(5)
    buf = camera.capture()
    led.off()
    camera.deinit()
    print(buf[0:8])
    print('Фото сделано')
    f = open(tfile, 'wb')
    f.write(buf)
    f.close()
