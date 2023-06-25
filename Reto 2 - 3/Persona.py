# Reto 2 Herencia - Reto 3 Encapsulamiento

#Se declara la Super Clase Persona
class Persona:
    #atributos
    cargo=""
    valorHora=5000
    horasTrabajadas=0
    departamenteo="Cundinamarca"

    #metodos
    def __init__(self, cargo, valorHora, horasTrabajadas, departamento):
        # RETO 3 Se utiliza el prefijo de doble subrayado (__) para indicar que un atributo o método es privado
        #self.cargo=cargo
        # Atributo Privado
        self.__cargo=cargo
        self.valorHora=valorHora
        self.horasTrabajadas=horasTrabajadas
        self.departamenteo=departamento

    # Metodo Privado
    def __calcularHonorarios(self):
        # No sedebe hacer operaciones dentro de los print
        honorarios=(self.horasTrabajadas)*(self.valorHora)-((((self.horasTrabajadas)*(self.valorHora))*0.966)/100)
        # Es mejor declarar la variable, sus operaciones y posteriormente imprimirla en un metodo de retorno
        return print(honorarios)   

    def calcularHonorarios(self):
        # No sedebe hacer operaciones dentro de los print
        honorarios=(self.horasTrabajadas)*(self.valorHora)-((((self.horasTrabajadas)*(self.valorHora))*0.966)/100)
        # Es mejor declarar la variable, sus operaciones y posteriormente imprimirla en un metodo de retorno
        return print(honorarios) 
    
