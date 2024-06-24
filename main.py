#main10.py
import takephoto01,netcon,sendtg7
def photo():
    takephoto01.run('boy.jpg')
    ssid,pwd = "OnePlus 8 Pro", "n6ggk5gs"
#    ssid,pwd = "OnLime_A5B1", "yppCqGhcVo"
#    ssid,pwd = "MERCUSYS_EB85", "27032021"
    netcon.connect(ssid,pwd)
#    time.sleep(5)
#    netcon.status()
#    time.sleep(5)
#    netcon.status()
    deviceid="1212121212"
    url='https://tgdj.ubnt.cloudns.cl/devpara'
    TOKEN='1701291551:AAEk2TbH7mbHLPVVBrP0gEOSZBezbjH1FHY'
    CHATID='159085018'
    URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    wifissid="MERCUSYS_9941"
    passw1="69528064"
    CAPTION="Счетчик воды в ванной"
    photo_path='boy.jpg'
    sendtg7.send_photo(TOKEN, CHATID, photo_path, CAPTION)
 #   netcon.disconnect()
    