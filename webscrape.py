import bs4
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) Apple \
WebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = requests.get('https://www.amazon.com/Lenovo-Thinkpad-T470-Business-Laptop\
              /dp/B07256JS27/ref=sr_1_3?ie=UTF8&qid=1514868659&sr=8-3&keywords=thinkpad+t470\
              ', headers=headers)
status = req.raise_for_status()
if status is None:
    bSoup = bs4.BeautifulSoup(req.text, 'html.parser')
    elems = bSoup.select('#priceblock_ourprice')
    print(elems[0].text)
    el = elems[0].text.split('$')
    print(el[1])
else:
    print('Couldn\'t resolve')
