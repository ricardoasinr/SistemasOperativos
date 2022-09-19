import multiprocessing
import time
def addFrase():
    frase = input("Introduce una frase: ")
    f = open ('fifoP','w')
    f.write(frase)
    f.close()
    print("3")
    

def imprimirFrase():
    print("1")
    f = open('fifoP', 'r')
    mensaje = f.read()
    print(mensaje)
    f.close()
    print("2")

if __name__ == '__main__':
    inputFrase = multiprocessing.Process(name='inputFrase', target=addFrase())
    printFrase = multiprocessing.Process(name='printFrase', target=imprimirFrase())
    
    inputFrase.start()
    inputFrase.join()
    printFrase.start()
    printFrase.join()

