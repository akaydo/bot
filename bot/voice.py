import requests,vk
session = (vk.Session(access_token='token'))
api = vk.API(session)
def voice(text_say):
    try:
        key='570622413ab98962ffbf414293b043accf047fb3ee31ed2405fb907cab6268a1f4d222762596a8811303f' #Это ключ
        text=text_say
        forma='OGG'
        url='http://api.voicerss.org/?key={}&hl=ru-ru&src={}&c={}'.format(key,text,forma) #Это сайт откуда берется
        r=requests.get(url)
        r=r.content #Тут проводятся получение данных
        f=open("OK.ogg","wb") #Запись wb - написать побайтово
        f.write(r)
        f.close()
        upload=api.docs.getMessagesUploadServer(type='audio_message',v=5.85)['upload_url'] #Это мы загружаем в Вконтакте
        files=[('file',open("OK.ogg",'rb'))]
        se=requests.post(upload,files=files)

        se=se.json()['file']

        doc=api.docs.save(v=5.85,file=se)

        us_id=doc[0]['owner_id']
        id_id=doc[0]['id']
        doc ='doc{}_{}'.format(us_id,id_id)

        #print(doc)
    except:
        doc='Вот так('
    return doc
