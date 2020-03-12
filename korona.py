import requests
import json
import csv
import datetime
import time
import pandas as pd
from bs4 import BeautifulSoup



def sprawdz():
    dzis = datetime.datetime.now().strftime('%d-%m-%y')
    teraz = datetime.datetime.now().strftime('%d-%m-%y godz. %H:%M')
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
                continue
            dzisiaj.writerow(x)
    data = pd.read_csv(f'{dzis}.csv')
    print(data.sort_values('Liczba', ascending=False))
    print("Suma:",data.sum()['Liczba'],"| Suma zgonów:",int(data.sum()['Liczba zgonów']))
    print(f'Aktualizacja {teraz}')

while True:
    sprawdz()
    time.sleep(60)
