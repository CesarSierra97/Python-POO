class Bolsillo:
    idBolsillo=0
    nombreBolsillo=""
    saldo=0
    clave=""
    numCel=""
    estadoBolsillo=False

    # Metodo constructor
    def __init__(self,numCel, nombreBolsillo, clave, saldo, idBolsillo, estadoBolsillo):
        self.numCel=numCel
        self.nombreBolsillo=nombreBolsillo
        self.clave=clave
        self.saldo=saldo
        self.estadoBolsillo=estadoBolsillo
        self.idBolsillo=idBolsillo

    # Metodos 
    def crearBolsillo(self):
        self.idBolsillo=self.idBolsillo+1
        self.numCel=input("Ingrese su numero de celular\t")
        self.nombreBolsillo=input("Indique el nombre del Bolsillo\t")
        self.clave=input("Digite una contraseña\t")
        self.saldo  
        rta=print(f"El bolsillo\t[{self.nombreBolsillo}], \nFue creado Exitosamente!")
        self.estadoBolsillo=True
        return rta
    
    def entrarBolsillo(self):
        tel=input("Digite su numero de celular")
        pas=input("Digite su contraseña")
        if tel==self.numCel and pas==self.clave:
            return True
        else:
            print("Datos incorrectos")           
        
    def consultarSaldo(self):
        return print(f"Su saldo actual es {self.saldo}")
    
    # Metodos con parametros
    
    def recargarSaldo(self,recarga):        
        self.saldo=(self.saldo)+recarga
        return print(f"Su saldo actual es de: {self.saldo}")
    
    def sacarPlata(self, sacar):       
        if sacar > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo=self.saldo-sacar 
        return print(f"Su saldo actual es de: {self.saldo}")
    
    def estado(self):
        print(f"El bolsillo: {self.nombreBolsillo}\nSe encuentra estado Activo = {self.estadoBolsillo}")
    
    def datos(self):
        print("**Consula:")
        print(f"Id: {self.idBolsillo}")
        print(f"Nombre: {self.nombreBolsillo}")
        print(f"Numero: {self.numCel}")
        print(f"Password: {self.clave}")
        if self.estadoBolsillo==True:
            print(f"Estado: Activo")
        else:
            print(f"Estado: Inactivo")
        



    



            