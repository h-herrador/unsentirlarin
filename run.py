from flask import Flask, render_template, jsonify
import pandas as pd
from web_scrapping import get_clasificacion, get_plantilla, get_jornadas  # Importa tus funciones

app = Flask(__name__)

# Página de inicio
@app.route('/')
def page_index():
    return render_template('index.html')

# Página de clasificación
@app.route('/clasificacion')
def page_clasificacion():
    return render_template('clasificacion.html')

# Página de plantilla
@app.route('/plantilla')
def page_plantilla():
    return render_template('plantilla.html')

# Página de jornadas
@app.route('/jornadas')
def page_jornadas():
    return render_template('jornadas.html')

# Página de actualidad
@app.route('/actualidad')
def page_actualidad():
    return render_template('actualidad.html')

# Rutas para obtener los datos en formato JSON
@app.route('/data/clasificacion')
def data_clasificacion():
    df = get_clasificacion("https://www.lapreferente.com/E13046/cd-larin")
    return jsonify(df.to_dict(orient="records"))

@app.route('/data/plantilla')
def data_plantilla():
    df = get_plantilla("https://www.lapreferente.com/E13046/cd-larin")
    return jsonify(df.to_dict(orient="records"))

@app.route('/data/jornadas')
def data_jornadas():
    df = get_jornadas()
    return jsonify(df.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)
