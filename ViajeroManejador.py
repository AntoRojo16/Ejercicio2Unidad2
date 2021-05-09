from ViajeroFrecuente import ClaseViajeroFrecuente
import csv
class ManejadorViajero:
    def __init__(self):
        self.__lista=[]
        
    def AgregarViajero(self,Viajero):
        self.__lista.append(Viajero)
        
    def getViajero (self,i):
        return self.__lista[i]
    
    def MostrarElemento (self,i):
        print (self.__lista[i])
        

    def testLibro (self):
        archivo=open("Viajero.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                '''saltear cabecera'''
                bandera= not bandera
            else:
                nro=int(fila[0])
                dni=int(fila[1])
                nom=fila[2]
                ape=fila[3]
                millas=int(fila[4])
                unViajero=ClaseViajeroFrecuente(nro,dni,nom,ape,millas)
                self.AgregarViajero(unViajero)
        archivo.close()
        
    def buscarViajero (self,nro):
        i=0
        unViajero= self.__lista[i]
        nron=unViajero.getnro()
        while (i<19)and(int(nron)!=int(nro)):
            i=i+1
            unViajero= self.__lista[i]
            nron=unViajero.getnro()
            
        if (int(nro)==int(nron)):
            print ("se encontro el viajero")
            return i
        else:
            return True
    def consultarMillas (self,i):
        unViajero=self.__lista[i]
        millas=unViajero.getmillas()
        print("sus millas son "+ str(millas))
            
        
    def acumularMillas (self,i,millas):
        unViajero=self.__lista[i]
        millasact=unViajero.getmillas()
        print("las milas antes de acumular son "+ str(millasact))
        unViajero.acumular(millas)
        millasacu=unViajero.getmillas()
        print("las millas acumuladas son "+ str(millasacu))
        
    
    def canjear (self,i,millas):
        unViajero=self.__lista[i]
        millasact=unViajero.getmillas()
        print("las millas antes de canjear es"+ str(millasact))
        unViajero.CanjearMillas(millas)
        millasactu=unViajero.getmillas()
        print("las millas despues de canjear es"+ str(millasactu))
        
        
      
            