def run(tfile,lighting):
    import camera
    from machine import Pin, PWM
    from time import sleep
    camera.deinit()
    camera.init()
    led = PWM(Pin(4), 5000)
    led.duty(int(lighting))
    sleep(1)
    buf = camera.capture()
    sleep(1)
    led.duty(0)
    print('Фото сделано')
    f = open(tfile, 'wb')
    f.write(buf)
    f.close()
    del f