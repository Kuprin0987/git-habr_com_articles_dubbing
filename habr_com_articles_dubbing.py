from bs4 import BeautifulSoup
import requests
import pyttsx3
import time

url = input('Введите ссылку статьи хабара: ')

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

tts = pyttsx3.init()

header = soup.find('h1', class_='tm-article-snippet__title tm-article-snippet__title_h1')

class_div = 'article-formatted-body article-formatted-body article-formatted-body_version-2'

div_article = soup.find('div', class_=class_div)

if div_article == None:
    print('Эта статья не может быть спарсина программой(так как формат body этой статьи версии 2), попробуйте спарсить другую статью')
else:
    print('Данная статья парсится программой')
    list_tegs = div_article.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'code', 'img'])

    tts.say(header.text)
    tts.runAndWait()
    time.sleep(0.5)

    for tag in list_tegs:
        if tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            time.sleep(0.25)

            tts.say(tag.text)
            tts.runAndWait()

            time.sleep(0.25)
            continue
        
        if tag.name == 'code':
            time.sleep(0.25)
            
            tts.say('Внимание, код')
            tts.runAndWait()

            time.sleep(0.25)
            continue
        
        if tag.name == 'img':
            time.sleep(0.25)
            
            tts.say('Внимание, картинка')
            tts.runAndWait()

            time.sleep(0.25)
            continue
        
        tts.say(tag.text)
        tts.runAndWait()
