import os
import camera
#import machine
#import time
from machine import Pin, PWM
from time import sleep

frequency = 5000
led = PWM(Pin(4), frequency)

#while True:
#  for duty_cycle in range(0, 1024):
#    led.duty(duty_cycle)
#    sleep(0.005)

def run(tfile):
#    led = machine.Pin(4, machine.Pin.OUT)
    led = PWM(Pin(4), 5000)
#    camera.deinit()
    camera.init()
#    led.on()
    led.duty(500)
#    sleep(5)
    buf = camera.capture()
#    sleep(5)
#    led.off()
    led.duty(0)
#    camera.deinit()
#    print(buf[0:8])
    print('Фото сделано')
    f = open(tfile, 'wb')
    f.write(buf)
    f.close()