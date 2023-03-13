#Explicación + capturas de lo que nos sale + código 
#Importamos librerias
from urllib.parse import*
from contextlib import closing
from sys import*
from bs4 import*
from os import sep
from timeit import *
import asyncio
from aoihttp import*
from functools import partial
import html.parser

def wget(uri): #Nos devuelve el contenido de la uri
    parsed = urlparse(uri) #analizamos la uri
    with closing(HTTPConnection(parsed.netloc)) as conn: #abrimos la uri
        path = parsed.path #ruta del servidor
        if parsed.query:
            path += '¿?' + parsed.query
        conn.request('GET', path) #Envía la consulta al servidor
        response = conn.getresponse() #Recoge la respuesta
        if response.status != 200: #Analizamos la respuesta, si es 200 --> bien, 3xx --> redirección, 4xx --> error del cliente, 5xx --> error del servidor
            print(response.reason, file = stderr)
            return
        print('Respuesta correcta')
        return response.read()

def get_images_scr_from_html(doc_html): #nos da el scr de las imágenes
    soup = BeautifulSoup(doc_html, 'html.parser')
    return[img.get('src') for img in soup.find_all('img')]