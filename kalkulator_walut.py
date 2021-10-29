from flask import Flask, render_template, request
import csv

app = Flask(__name__)

with open('dane_z_banku.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    kursy_walut=next(csvreader)[1]



@app.route("/kalkulator/", methods=["GET", "POST"])
def calkulator():
    if request.method == "POST":
        data = request.form
        waluta = data.get('waluta')
        ilość = data.get("ilość")


    return render_template("form.html", dane=kursy_walut)  # przekazuję słowniki z danymi kursów walut

