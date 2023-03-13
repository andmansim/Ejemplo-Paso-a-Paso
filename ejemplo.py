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

async def wget(session, uri): #Nos devuelve el contenido de la uri
    
    async with session.get(uri) as response: #abrimos la uri

        if response.status != 200: #Analizamos la respuesta, si es 200 --> bien, 3xx --> redirección, 4xx --> error del cliente, 5xx --> error del servidor
            return None
        if response.content_type.startswith('text/'):
            return await response.text()
        else:
            
            return


async def get_images_scr_from_html(doc_html): #nos da el scr de las imágenes
    soup = BeautifulSoup(doc_html, 'html.parser')
    for img in soup.find_all('img'):
        yield img.get('scr')
        await asyncio.sleep(0.001)
    
async def download(session, uri):
    content = await wget(session, uri)
    if content is None:
        with open(uri.split(sep)[-1], 'wb') as f:
            f.write(content)
            return uri
        
def get_uri_from_images_scr(base_uri, images_src):
    parsed = urlparse(base_uri)
    result = []
    for src in images_src:
        parsed1 = urlparse(src)
        if parsed1.netloc =='':
            path = parsed.payh
            if parsed1.query:
                path += '¿?' + parsed1.query
            if path[0] != '/':
                if parsed.path == '/':
                    path = '/' + path 
                else:
                    path = '/' + '/'.join(parsed.path.split('/')[:1]) + '' + path
        