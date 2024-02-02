import requests
from bs4 import BeautifulSoup

class Cuevana:
    def __init__(self, url):
        self.url = url

    def obtener_informacion_pelicula(self):
        # Realizar la solicitud HTTP a la página
        respuesta = requests.get(self.url)
        
        if respuesta.status_code == 200:
            # Analizar el HTML de la página
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            
            # Extraer información
            nombre_pelicula = soup.find('h1', class_='Title').text.strip()
            actores = [actor.text.strip() for actor in soup.find_all('li', class_='AAIco-adjust loadactor')]
            sinopsis = soup.find('div', class_='Description').text.strip()
            
            meta_class = soup.find('p', class_='meta')
            
            Duracion = ["No disponible", "No disponible"]
            
            if meta_class:
                spans = meta_class.find_all('span')
                if len(spans) >= 2:
                    Duracion = [spans[0].text.strip(), spans[1].text.strip()]

            # Devolver la información, incluyendo la lista de duración y año
            return {
                'nombre_pelicula': nombre_pelicula,
                'actores': actores,
                'sinopsis': sinopsis,
                'Duracion': Duracion
            }
        else:
            print(f"No se pudo acceder a la página. Código de estado: {respuesta.status_code}")
            return None

if __name__ == "__main__":
    # Lista de URLs de películas
    lista_urls_peliculas = ['https://cuevana.biz/pelicula/68726/titanes-del-pacifico', 'https://cuevana.biz/pelicula/561/constantine', 'https://cuevana.biz/pelicula/9799/rapido-y-furioso']

    # Lista para almacenar la información de todas las películas
    matriz_peliculas = list(map(Cuevana, lista_urls_peliculas))

    # Diccionario para almacenar la información de todas las películas
    diccionario_peliculas = {}

    # Función para imprimir y almacenar la información de una película
    def almacenar_informacion(pelicula):
        informacion = pelicula.obtener_informacion_pelicula()
        if informacion:
            nombre_pelicula = informacion['nombre_pelicula']
            diccionario_peliculas[nombre_pelicula] = informacion

    # Almacenar la información de todas las películas
    list(map(almacenar_informacion, matriz_peliculas))

    # Imprimir el diccionario de películas
    print("\nDiccionario de películas:")
    print(diccionario_peliculas)




