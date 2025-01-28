class Distancia:
    #Declaracion de Propiedades
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    # Declaración del constructor
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2= 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def pedir(self):
        print("Ingrese los siguientes datos:")
        self.x1 = int(input("Ingrese el punto X1: "))
        self.y1 = int(input("Ingrese el punto Y1: "))
        self.x2 = int(input("Ingrese el punto X2: "))
        self.y2 = int(input("Ingrese el punto Y2: "))

    def calcular(self):
        distancia = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        print("La distancia entre los puntos es: {}".format(distancia))
        
def main():
    obj = Distancia()
    obj.pedir()
    obj.calcular()

if __name__ == "__main__":
    main()

