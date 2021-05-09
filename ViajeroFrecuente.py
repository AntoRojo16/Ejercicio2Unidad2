class ClaseViajeroFrecuente:
    __nroViajero=""
    __Dni=""
    __nombre=""
    __apellido=""
    __MillasAcum=""
    
    
    
    def __init__(self,nro,dni,nom,ape,millas):
        self.__nroViajero=nro
        self.__Dni=dni
        self.__nombre=nom
        self.__apellido=ape
        self.__MillasAcum=millas
        
    def CantidadTotalMillas (self):
        return self.__MillasAcum
    
    def mostrarViajero(self):
        print (" numero de viajero"+str(self.__nroViajero)+" dni de viajero"+str(self.__Dni)+"nombre y apellido del viajero"+self.__nombre+self.__apellido+"millas acumuladas"+str(self.__MillasAcum))
    
    def CanjearMillas (self,millas):
        m=self.__MillasAcum
        #if (m==int(millas)):
         #   self.__MillasAcum=self.__MillasAcum-int(millas)
            
        if((int(millas)<m) or (millas==m)):
            self.__MillasAcum=self.__MillasAcum-int(millas)
        else: 
            print("No se puede cajear las millas")
            
    def acumular (self,millas):
        self.__MillasAcum=self.__MillasAcum + int(millas)
            
    def getnro(self):
        return self.__nroViajero
    
    def getDNI (self):
        return self.__Dni
    
    def getno (self):
        return self.__nombre
    
    def getape (self):
        return self.__apellido
    
    def getmillas (self):
        return self.__MillasAcum
    
    def __str__ (self):
        return "%s %s %s %s %s" % (self.__nroViajero, self.__Dni, self.__nombre, self.__apellido, self.__MillasAcum) 
            
