from Clases import Factorial as factor
funcion = factor()

def menu():
    print("1. Factorial de un numero.")
    print("2. Salir")
    op = int(input(">> "))
    return op


def calcFactorial():
     numero = int(input("Calcular el factorial de: "))
  
     result = funcion.obtenerFactorial(numero)
     print(result)




def main():
    op = 0
    while(op != 2):
        op = menu()
        match(op):
            case 1:
                calcFactorial()
            case 2:
                exit()

main()





    