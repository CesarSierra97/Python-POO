from Bolsillo import Bolsillo
class Nequi(Bolsillo):

    def __init__(self, numCel, nombreBolsillo, clave, saldo, idBolsillo, estadoBolsillo):
        super().__init__(numCel, nombreBolsillo, clave, saldo, idBolsillo, estadoBolsillo)

    def enviar(self):
        envia=int(input("¿Cuanto desa enviar?"))
        if envia > self.saldo:
            print("Saldo insuficiente para realizar el envio")
        else:
            self.saldo=(self.saldo)-envia
        return print(f"Su saldo actual es de: {self.saldo}")

    def pedir(self):
        pide=int(input("Ingrese el valor a pedir:\n¡No se le olvide pedir el Favor!\n"))
        self.saldo=(self.saldo)+pide
        return print(f"Su saldo actual es de: {self.saldo}")
    
