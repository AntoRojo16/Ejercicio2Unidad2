from ViajeroManejador import ManejadorViajero
from clasedeMenu import Menu
import os
def test ():
    
    unManejador=ManejadorViajero()
    unManejador.testLibro()
    unManejador.MostrarElemento(0)
    f=input("ingrese un numero de viajero")
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n3. Inciso 3 \n4. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op,unManejador,f)
        salir = op == 4
if __name__=="__main__":
    test()
    
    
   