import os
from ViajeroManejador import ManejadorViajero

class Menu:
    __switcher:None
    
    def __init__(self):
        self.__switcher={ 1: self.opcion1,
                          2: self.opcion2,
                          3: self.opcion3,
                          4: self.salir}
        
    def getSwitcher (self):
        return self.__switcher
    
    def opcion (self,op,viajeros,num):
        func=self.__switcher.get(op, lambda: print("opcion no valida")) #busco la clve op dentro del diccionario y si no la encuentra devuelve un print
        func(viajeros,num)
        
    def salir (self,viajero, num):
        print ("Salir")
        
    def opcion1 (self,viajeros,num):
        os.system('cls')
        if (viajeros.buscarViajero(num)==True):
            print("Error el numero ingresado no pertenece a un viajero")
        else:
            i=viajeros.buscarViajero(num)
            viajeros.consultarMillas(i)
            
            
    def opcion2 (self,viajero,num):
        os.system('cls')
        i=viajero.buscarViajero(num)
        if (viajero.buscarViajero(num)==True):
            print("Error el numero ingresado no pertenece a un viajero")
        else:
            j=input("Ingrse la cantidad de millas")
            viajero.acumularMillas(i,j)
            
    def opcion3 (self, viajeros,num):
        os.system('cls')
        i=viajeros.buscarViajero(num)
        if (viajeros.buscarViajero(num)==True):
            print("Error el numero ingresado no pertenece a un viajero")
        else:
            m=input("Ingrese la cantidad de millas a canjear")
            viajeros.canjear(i,m)
        
        
    