from flask import Flask, render_template, request, redirect
from src.clases import *
import pandas as pd
#from src.websc import funcion_plantilla, funcion_clasificacion
app = Flask(__name__, template_folder = "../templates", static_folder = "../static")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plantilla')
def plantilla():
    jugadores = pd.DataFrame([["Dani", 5, "DF", 1], ["Raptor", 0,"DC", 0], ["Raptor", 0,"DC", 0]]).to_string().split()
    jugadores = jugadores[4:]
    jugadores = [jugadores[i] for i in range(len(jugadores)) if i%5]
    jugadores = [[jugadores[i + 4*j] for i in range(4)] for j in range(int(len(jugadores)/4))]
    return render_template('plantilla.html', jugadores = jugadores)


@app.route('/clasificacion')
def clasificacion():
    equipos = []
    return render_template('clasificacion.html', clasificacion = [])


@app.route('/partidos')
def partidos():
    return render_template('partidos.html', partidos = partidos)