#Explicación + capturas de lo que nos sale + código 
#Importamos librerias
from urllib.parse import*
from contextlib import closing
from sys import*
from bs4 import*
from os import sep
from timeit import *
import asyncio
from aiohttp import *
from functools import partial
import html.parser

def wget(uri):
    parsed = urlparse(uri)
    with closing (HTTPConnection(parsed.netloc)) as conn:
        path = parsed.path
        if parsed.query:
            path += '¿?' + parsed.query
        conn.request('GET', path)
        response = conn.getresponse()
        if response.status != 200:
            print(response.reason, file = stderr)
            return
        print('Respuesta correcta')
        return response.read()
            