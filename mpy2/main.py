import takephoto01,netcon,sendtg,settings
def photo(para):
    print(para)
    takephoto01.run('boy.jpg',para['lighting'])
    netcon.connect(para['wifissid'],para['wifipwd'])
    TOKEN=settings.TOKEN
    sendtg7.send_photo(TOKEN, para['chatid'], 'boy.jpg', para['description'])
