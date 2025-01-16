import os

def funcion1():
    os.system('cls')
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    res = num1 + num2
    print(f"Resultado: {res}")
    print("Hola, soy función 1")
    input("Enter para continuar")

def funcion2():
    os.system('cls')
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    res = num1 - num2
    print(f"Resultado: {res}")
    print("Hola, soy función 2")
    input("Enter para continuar")

def funcion3():
    os.system('cls')
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    res = num1 * num2
    print(f"Resultado: {res}")
    print("Hola, soy función 3")
    input("Enter para continuar")

def funcion4():
    os.system('cls')
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))

    res = num1 / num2
    print(f"Resultado: {res}")

    print("Hola, soy función 4")
    input("Enter para continuar")

def run():
    op = 0
    while op != 5:
        os.system('cls')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir')
        op = int(input('Opción: '))
        if op == 1:
            funcion1()
        if op == 2:
            funcion2()
        if op == 3:
            funcion3()
        if op == 4:
            funcion4()
        if op == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    run()