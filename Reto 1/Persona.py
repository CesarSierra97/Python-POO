class Persona:
    #Atributos
    tipoDoc=""
    documento=""
    nombre=""
    apellido=""
    peso=""
    estatura=""
    edad=""
    sexo=""

    #Metodos
    def __init__(self,tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo):
        self.tipoDoc=tipoDoc
        self.documento=documento
        self.nombre=nombre
        self.apellido=apellido
        self.peso=peso
        self.estatura=estatura
        self.edad=edad
        self.sexo=sexo

    def pedirDatos(self):
        self.tipoDoc=input("Digite su tipo de documento")
        self.documento=input("Digite su documento")
        self.nombre=input("Digite su nombre")
        self.apellido=input("Digite su apellido")
        self.peso=int(input("Digite su peso en Kg"))
        self.estatura=int(input("Digite su estatura en Mts"))
        self.edad=int(input("Digite su edad"))
        self.sexo=input("Digite su tipo de sexo")

    def mostrarDatos(self):
        print(f"Los datos registrados son:\n Nombre: {self.nombre} ")
        print(f" Apellido: {self.apellido} ")
        print(f" Tipo de documento: {self.tipoDoc} ")
        print(f" Numero de documento: {self.documento} ")
        print(f" Peso actual: {self.peso} ")
        print(f" Estatura: {self.estatura} ")
        print(f" Sexo: {self.sexo} ")

    def calculaImc(self):
        r=(self.peso/((self.estatura)*(self.estatura)))
        if(r<20):
            print("Estas bajo de peso")
        elif(r==20):
            print("Estas en el peso ideal")
        elif(r>25):
            print("Sobre peso")
        else:
            print("**ERROR 404**")

    def calcularMayor(self):
        if(self.edad>=18):
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
     