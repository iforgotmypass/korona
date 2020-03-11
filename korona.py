import requests
import json
import csv
import datetime
import schedule
import time
from bs4 import BeautifulSoup

def sprawdz():
    dzis = datetime.datetime.now().strftime('%d-%m-%y')
    strona = requests.get('https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2')
    soup = BeautifulSoup(strona.content, 'html.parser')
    lista = json.loads(soup.find(id='registerData').get_text())
    listacsv = csv.reader(lista['data'].split("\n"), delimiter=';')
    with open(f'{dzis}.csv',mode='w') as dzisiaj:
        dzisiaj = csv.writer(dzisiaj, delimiter=",")
        for x in listacsv:
            try:
                x.pop()
            except:
                print('Lista pusta')
            dzisiaj.writerow(x)
    print(f'Aktualizacja godz. 20:00 {dzis}')

schedule.every().day.at('20:00').do(sprawdz)

while True:
    schedule.run_pending()
    time.sleep(1)
