import requests

# Configuración inicial
API_KEY = "url"
BASE_URL = "https://api.themoviedb.org/3"

def obtener_rating_pelicula(titulo):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={titulo}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['results']:
            primera_pelicula = datos['results'][0]
            nombre = primera_pelicula['title']
            rating = primera_pelicula['vote_average']
            print(f"La película '{nombre}' tiene un rating de {rating}.")
        else:
            print("Película no encontrada.")
    else:
        print("Error al realizar la petición a la API.")

if __name__ == "__main__":
    titulo_pelicula = input("Introduce el título de una película para obtener su rating: ")
    obtener_rating_pelicula(titulo_pelicula)