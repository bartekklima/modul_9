import csv
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
dane = data[0]['rates']

with open('dane_z_banku.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    print(dane)
    spamwriter.writerow(dane)