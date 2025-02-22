import requests
from bs4 import BeautifulSoup
import pandas as pd


def download_soup(url):
    """
    Función que realiza una petición a una url y devuelve el objeto BeautifulSoup
    """
    print("Empezando petición a: " + url)
    response = requests.get(url)
    if response.status_code == 200:
        page = response.text
        soup = BeautifulSoup(page, "lxml")
        print("Petición completada con éxito!")
        return soup
    else:
        print("Error, código de estado: " + response.status_code)


def get_clasificacion(url):
    """
    Función que obtiene la clasificación de un grupo de la preferente
    """
    soup = download_soup(url)

    # Buscamos la tabla de clasificación
    table = soup.find("table", {"id": "tableClasif"})
    # Buscamos las filas de la tabla
    rows = table.find_all("tr")
    # Creamos una lista vacía para guardar los datos
    clasificacion = {
        "Posicion": [],
        "Equipo": [],
        "Puntos": [],
        "PJ": [],
        "Victorias": [],
        "Empates": [],
        "Derrotas": [],
        "GF": [],
        "GC": [],
        "DG": [],
    }

    # Iteramos sobre las filas de la tabla
    for row in rows[1:]:
        # Buscamos las celdas de la fila
        cells = row.find_all("td")

        # Guardamos los datos en las listas
        clasificacion["Posicion"].append(cells[0].text)
        equipo = cells[2].find("span")
        clasificacion["Equipo"].append(equipo.text)
        clasificacion["Puntos"].append(cells[3].text)
        for i in range(4, 10):
            info = cells[i].find("a")
            clasificacion[list(clasificacion.keys())[i - 1]].append(info.text)
        clasificacion["DG"].append(cells[10].text)

    # Creamos un DataFrame con los datos
    clasificacion = pd.DataFrame(clasificacion)
    return clasificacion


def get_plantilla(url):

    soup = download_soup(url)

    table = soup.find("table", {"id": "tablePlantilla"})

    jugadores = list(table.find_all("tr"))

    plantilla = {"Nombre": list(), "Posición": list(), "Goles": list()}

    subconjuntos = (
        jugadores[2:5]
        + jugadores[6:12]
        + jugadores[13:17]
        + jugadores[18:22]
        + jugadores[23:30]
    )
    for jugador in subconjuntos:  # for i in jugadores(2,3,4,6,7,...)

        campos = jugador.find_all("td")  # 2, 3, 10
        nombre = campos[2]
        posicion = campos[3]
        goles = campos[10]

        campo_nombre = nombre.find("a")
        nombre_pila = campo_nombre.find("span")
        plantilla["Nombre"].append(nombre_pila.text)

        campo_posicion = posicion.find("span")
        plantilla["Posición"].append(campo_posicion.text)

        campo_goles = goles.find("span")
        plantilla["Goles"].append(campo_goles.text)

    for i, nombre in enumerate(plantilla["Nombre"]):
        if nombre.strip() == "Rego":  # .strip() por si hay espacios extra
            plantilla["Posición"][i] = "Delantero"
        if nombre.strip() == "Victor Bellón":
            plantilla["Posición"][i] = "Defensa"
        if nombre.strip() == "Pallas":
            plantilla["Posición"][i] = "Delantero Centro"
        if nombre.strip() == "Oton":
            plantilla["Posición"][i] = "Lateral Izquierdo"
        if nombre.strip() == "Marcos Blanco":
            plantilla["Posición"][i] = "Centrocampista"
        if nombre.strip() == "Kovaleff":
            plantilla["Posición"][i] = "Extremo Izquierdo"
        if nombre.strip() == "Martin Vieites":
            plantilla["Goles"][i] = "24 (goles encajados)"
        if nombre.strip() == "Varela":
            plantilla["Goles"][i] = "21 (goles encajados)"
        if nombre.strip() == "Vergara":
            plantilla["Goles"][i] = "20 (goles encajados)"
    return pd.DataFrame(plantilla)


if __name__ == "__main__":
    url = "https://www.lapreferente.com/E13046/cd-larin"
    get_plantilla(url)
    get_clasificacion(url)
