from Nequi import Nequi
class Ejecucion(Nequi):

    bolsillo1=Nequi("","","",5000,777,False)

    bolsillo1.crearBolsillo()
    if (bolsillo1.entrarBolsillo()):
        op1="1"
        while(op1=="1"):
            print(f"Bienvenido al menu de Nequi\n Estas usando el bolsillo: [{bolsillo1.nombreBolsillo}]")
            op=""
            while(op!="1" and op!="2" and op!="3" and op!="4" and op!="5" and op!="6" and op!="7"):
                op=input(f"Seleccione una opscion:\n 1. Consultar Saldo\n 2. Recarga Saldo\n 3. Saca Plata\n 4. Envía Plata\n 5. Pide Plata\n 6. Validar Estado\n 7. Consula de Datos\n\t Digite [S] para salir\n")        
                if(op=="1"):
                    bolsillo1.consultarSaldo()
                    break
                elif(op=="2"):
                    r=int(input("Digite el valor de la recarga\n"))
                    bolsillo1.recargarSaldo(r)
                    print(type(bolsillo1.saldo))
                    break
                elif(op=="3"):
                    s=int(input("Digite el valor que va a retirar\n"))
                    bolsillo1.sacarPlata(s)
                    break
                elif(op=="4"):
                    bolsillo1.enviar()
                    break
                elif(op=="5"):
                    bolsillo1.pedir()
                    break
                elif(op=="6"):
                    bolsillo1.estado()
                    break
                elif(op=="7"):
                    bolsillo1.datos()
                    break
                elif(op=="S" and op=="s"):
                    break
                else:
                    print("******************\nLos valores son incorrectos\nDigite unicamente un numero del 1 al 6\n*********************")   

            op1=input("**Seleccione\n 1. Menu\n Digite [S] para salir")
    else:
        print("***Los datos ingresados son Incorrectos")
    print("Gracias por vicitarnos")

