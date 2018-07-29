import bs4
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) Apple \
WebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = requests.get('https://www.astroyogi.com/horoscopes/daily/cancer-free-horoscope.aspx', headers=headers)
status = req.raise_for_status()
if status is None:
    bSoup = bs4.BeautifulSoup(req.text, 'html.parser')
    elems = bSoup.select('#ContentPlaceHolder1_LblPredictiontom')
    print(elems[0].text)
else:
    print('Couldn\'t resolve')
