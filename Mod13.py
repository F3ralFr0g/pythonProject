# tehtävä 13.1

from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = int(luku)
        alkuluku = False
        for n in range(2, luku):
            if luku % n == 0:
                break
        else:
            alkuluku = True

        tilakoodi = 200
        vastaus =\
            {
                "status": tilakoodi,
                "luku": luku,
                "alkuluku": alkuluku
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen syöte"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


# tehtävä 13.2

from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def haeLentokenttä(icao):
    try:
        sql = f"SELECT name, municipality FROM airport WHERE IDENT = '{icao}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()
        name = tulos[0]
        municipality = tulos[1]

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "ICAO": icao,
            "kenttä": name,
            "kaupunki": municipality
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen ICAO-koodi"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

yhteys = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    database = "flight_game",
    user = "root",
    password = "mutsi",
    autocommit = True
)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)