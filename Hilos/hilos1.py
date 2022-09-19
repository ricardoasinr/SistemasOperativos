import threading
import time
count=1

#Funcion ejecutar

def cuenta(n,name):
	global count
	bucle=1
	while bucle<5:
		print("")
		print(name,count)
		count+=1
		bucle+=1


def imprimir(n,name):
    global count
    print(name, count)

#Se crea el hilo
t=threading.Thread(target=cuenta, args=(1, 'thread1'))
t2=threading.Thread(target=cuenta, args=(1, 'thread2'))
t3=threading.Thread(target=imprimir, args=(1,'thread3'))

#Iniciamos procesos
t.start()
#time.sleep(3)
t2.start()
#time.sleep(3)
t3.start()
	
