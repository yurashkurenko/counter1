# This file is executed on every boot (including wake-boot from deepsleep)
from deviceid import deviceid,urlpara
import netcon
ssid,pwd = "OnePlus 8 Pro", "n6ggk5gs"
netcon.connect(ssid,pwd)
import getpara
para=getpara.getpara(urlpara,deviceid)
import main
from time import sleep
while(True):
    main.photo(para)
    sleep(int(para['polling']))




