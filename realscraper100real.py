import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

class Cuevana:
    def __init__(self, url):
        self.url = url
        self.pelicula = {}

    async def obtener_informacion_pelicula(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    html = await response.text()

                    # Analizar el HTML de la página
                    soup = BeautifulSoup(html, 'html.parser')

                    # Extraer información
                    nombre_pelicula = soup.find('h1', class_='headline-1 js-widont prettify').text.strip()
                    actores = [actor.text.strip() for actor in soup.find_all('div', class_='cast-list text-sluglist')]
                    Actores = [' '.join(actor.replace("\nShow All…", "").split()) for actor in actores]
                    Sinopsis = soup.find('div', class_='truncate').text.strip()
                    duracion = soup.find('p', class_="text-link text-footer").text.strip().split()[0:2]
                    Duracion = ' '.join(duracion)
                    Year = soup.find('small', class_='number').text.strip()

                    self.pelicula[nombre_pelicula.lower()] = {
                        'Informacion': {
                            'Actores': Actores,
                            'Sinopsis': Sinopsis,
                            'Duracion': Duracion,
                            'Year': Year
                        },
                    }

                    return self.pelicula[nombre_pelicula.lower()]
                else:
                    print(f"No se pudo acceder a la página. Código de estado: {response.status}")
                    return None

async def main():
    # Lista de URLs de películas
    urls = ['https://letterboxd.com/film/the-dark-knight/']

    # Crear instancias de Cuevana para cada URL
    peliculas = [Cuevana(url) for url in urls]

    # Almacenar la información de todas las películas
    tasks = [pelicula.obtener_informacion_pelicula() for pelicula in peliculas]
    resultados = await asyncio.gather(*tasks)

    # Imprimir el diccionario de películas  
    print(resultados)

if __name__ == "__main__":
    # Obtener el tiempo de inicio
    inicio = time.time()

    # Ejecutar el bucle de eventos de asyncio
    asyncio.run(main())

    # Obtener el tiempo de finalización y calcular el tiempo transcurrido
    fin = time.time()
    print(f"Tiempo transcurrido: {fin - inicio} segundos")
