import csv
from requests_html import HTMLSession
import ccxt


def get_gemini_static(file):
    gemini = ccxt.gemini()
    fee = gemini.fees
    taker_fee, maker_fee = fee['trading']['taker'] * 10000, fee['trading']['maker'] * 10000

    session = HTMLSession()
    url = 'https://docs.gemini.com/websocket-api/#timestamps'
    r = session.get(url)
    text = r.html.text
    start = text.find('Minimum price increment')
    end = text.find('Sequence numbers')
    text = text[start:end]
    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        for currency in ['btcusd', 'ethusd']:
            uid = list(currency)
            uid.insert(3, '_')
            uid = ''.join(uid).upper()
            uid = uid + '-gemini'
            text = text[text.find(currency):]
            texts = text.split('\n')
            csvwriter.writerow([uid, 'Gemini', currency, texts[5].split(' ')[0], '1', texts[4].split(' ')[0], '',
                                texts[3].split(' ')[0], '', '8', '2', taker_fee, maker_fee, 0, 0, 'cryptocurrency'])

