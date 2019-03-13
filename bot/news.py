import requests


def news():
    try:
        url='https://newsapi.org/v2/top-headlines?country=ru&apiKey=9d4fb0f8eac9485781679c683ecd2471'
        r=requests.get(url)
        r=r.json()
        message=''
        if r.get('status')=='ok':
            for i in range(5):
                title=r.get('articles')[i]['title']
                urls=r.get('articles')[i]['url']
                message=message+str(i+1)+'.'+title+'\n'+urls+'\n \n'
        else:
            message='все сломалось(('

    except:
        message='CRITICAL ERROR'

    return message





#9d4fb0f8eac9485781679c683ecd2471
