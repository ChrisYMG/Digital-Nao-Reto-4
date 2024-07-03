import requests
from bs4 import BeautifulSoup

# Definir la URL de la página web a raspar
url = 'https://www.youtube.com/'

# Realizar una solicitud HTTP GET a la URL
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraer información específica del contenido HTML
    # Por ejemplo, extraer todos los enlaces de la página
    enlaces = soup.find_all('a')
    
    # Imprimir los enlaces encontrados
    for enlace in enlaces:
        print(enlace.get('href'))
else:
    print(f'Error al realizar la solicitud: {response.status_code}')