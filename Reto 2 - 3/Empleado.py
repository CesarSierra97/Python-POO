#De la Super Clase Persona Importe sus metodos-
from Persona import Persona
#-a la nueva sub Clase Empleado 
class Empleado(Persona):
    #atributo
    nombre="cesar"
    apellido="sierra"

    #definimos el metodo constructor para la clase Empleado
    def __init__(self, cargo, valorHora, horasTrabajadas, departamento, nombre, apellido):
        #Heredamos el metodo constructor de la super clase Persona
        super().__init__(cargo, valorHora, horasTrabajadas, departamento)
        #Establecemos los self para los atributos de esta clase        
        self.nombre=nombre
        self.apellido=apellido

    def impEmpleado(self):
        print(f"El empleado: [{self.nombre} {self.apellido}]\ndel area de {self.cargo} a trabajado: ",self.horasTrabajadas)

#Creamos el objeto 
empleado1=Empleado("Desarrollador",5000,80,"Cundinamarca","Cesar","Sierra")
empleado1.impEmpleado()
empleado1.calcularHonorarios()
