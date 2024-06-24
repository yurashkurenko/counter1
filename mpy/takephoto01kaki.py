#import os
#import camera
#import machine
#import time
#from machine import Pin, PWM
#from time import sleep

#frequency = 1000
#led = PWM(Pin(4), frequency)

#while True:
#  for duty_cycle in range(0, 1024):
#    led.duty(duty_cycle)
#    sleep(0.005)

def run(tfile):
#    led = machine.Pin(4, machine.Pin.OUT)
#    led = PWM(Pin(4), 1000)
    import camera
#    import os
    from machine import Pin, PWM
    from time import sleep
    camera.deinit()
    camera.init()
#    led.on()
    led = PWM(Pin(4), 5000)
#   led duty - яркость 0 - 1024
    led.duty(150)
    sleep(1)
    buf = camera.capture()
    sleep(1)
#    led.off()
    led.duty(0)
#    del led
#    del camera
#    camera.deinit()
#    print(buf[0:8])
    print('Фото сделано')
    f = open(tfile, 'wb')
    f.write(buf)
    f.close()
    del f
