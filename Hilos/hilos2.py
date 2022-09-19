import threading
import time
mensaje = ""
def enviar(n,name):
    global mensaje
    mensaje = "Hola "+name
    
def recibir(n, m):
    global mensaje
    print(mensaje)
    
nombre = input("Ingrese un nombre ")
t =threading.Thread(target = enviar, args =(1,nombre))
t2 =threading.Thread(target = recibir, args =(1,'thread2'))
t.start()
t.join()
time.sleep(3)
t2.start
