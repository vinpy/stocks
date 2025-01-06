import requests
from bs4 import BeautifulSoup
import time
from winotify import Notification, audio

ticker = 'NIFTY_50'#'GMRAIRPORT'
exchange = 'INDEXNSE'
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
class1 = "YMlKec fxKbKc"
price = float(soup.find(class_=class1).text.strip()[0:].replace(",",""))
print(price)

toast = Notification(app_id="vinworld script",
                     title="Stock price",
                     msg=f'alert got triggered for {ticker} and price is {price}',
                     duration="short")

toast.set_audio(audio.LoopingAlarm2, loop=False)

if(price > 23600):
    toast.show()