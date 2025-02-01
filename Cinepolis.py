class CompraBoletos: 
    precioUnitario = 12
    descuento1 = 0.10  
    descuento2 = 0.15  
    descuentoCINECO = 0.10  

    def __init__(self, total_general=0, ventas=[]):
        self.total_general = total_general
        self.ventas = ventas

    ticket = open("ventas.txt", "w")
    ticket.write("-------CINEPOLIS LA CAPITAL DEL CINE-------\n----------------TICKET----------------\n")
    ticket.close()

    def iniciar(self):
        print("----------- BIENVENIDO A CINEPOLIS : LA CAPITAL DEL CINE -----------")
        while True:
            opcion = input("\n1. Comprar boletos\n2. Terminar venta\nSeleccione una opción: ")

            if opcion == "1":
                self.realizar_compra()
            elif opcion == "2":
                self.finalizar_ventas()
                break
            else:
                print("ERROR \nIngrese una opción válida")

    def realizar_compra(self):
        nombre = input("Ingrese su nombre: ")

        while True:
            personas = int(input("Ingrese el numero de personas (Considere como maximo 7 boletos por persona): "))
            if personas > 0:
                break
            print("ERROR \nDebe ser al menos una persona.")

        boletos = 0

        while True:
            limite_boletos = personas * 7
            if boletos == 0:
                boletos = int(input(f"¿Cuantos boletos desea comprar? (Usted puede comprar hasta {limite_boletos} boletos): "))

            if 1 <= boletos <= limite_boletos:
                break
            
            while True:
                print("ERROR \nDebe ingresar entre 1 y {} boletos.".format(limite_boletos))
                print("1. Cambiar numero de boletos")
                print("2. Cambiar numero de personas")
                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    boletos = int(input(f"¿Cuantos boletos desea comprar? (Usted puede comprar hasta {limite_boletos} boletos): "))
                    break  

                elif opcion == "2":
                    while True:
                        personas = int(input("Ingrese el numero de personas (Considere como maximo 7 boletos por persona): "))
                        if personas > 0:
                            break
                        print("ERROR \nDebe ser al menos una persona.")
                    
                    limite_boletos = personas * 7

                    if 1 <= boletos <= limite_boletos:
                        break  
                    else:
                        print(f"Los {boletos} boletos que ingreso aun no son validos. Debe corregirlos.")
                        boletos = 0
                        continue  

            else:
                continue  

        total = boletos * self.precioUnitario
        if 3 <= boletos <= 5:
            total *= (1 - self.descuento1)
        if boletos > 5:
            total *= (1 - self.descuento2)

        print("Seleccione su metodo de pago:")
        print("1. Tarjeta CINECO (Otorga 10% de descuento)")
        print("2. Efectivo")
        metodo_pago = input("Ingrese opcion (1/2): ")
        
        if metodo_pago == "1":
            total *= (1 - self.descuentoCINECO)

        self.total_general += total
        venta = f"{nombre}: ${total}"
        self.ventas.append(venta)
        print(f"Total a pagar para {nombre}: ${total}")

        ticket = open("ventas.txt", "a")
        ticket.write(venta + "\n")
        ticket.close()

    def finalizar_ventas(self):
        print("\nDetalles de su compra\n")
        ticket = open("ventas.txt", "r")
        lineas = ticket.readlines()
        for linea in lineas:
            print(linea.strip())
        ticket.close()

        print("Total general de todas las compras: ${}".format(self.total_general))

        ticket = open("ventas.txt", "a")
        ticket.close()

        print("\nSu ticket fue generado \nGracias por su compra! :)")

if __name__ == "__main__":
    app = CompraBoletos()
    app.iniciar()
