from math import sqrt
from tabulate import tabulate

class Carga:

    def __init__(self, q, coordenadas):
        self.q = q
        self.coordenadas = coordenadas

class OperacionesVectores:

    @staticmethod
    def restar_puntos( carga1, carga2):
        return [carga2.coordenadas[0] - carga1.coordenadas[0], carga2.coordenadas[1] - carga1.coordenadas[1]]
    
    @staticmethod
    def calcular_magnitud(coordenadas):
        return sqrt(coordenadas[0] ** 2 + coordenadas[1] ** 2)

    @staticmethod
    def calcular_vector_unitario(vector, magnitud):
        return [round(vector[0] / magnitud, 2), round(vector[1] / magnitud, 2)]


class CalculadoraFuerza:
    k = 9 * 10 ** 9
    cargas = []

    def __init__(self, cargas):
        self.cargas = cargas
    
    
    def calcular_fuerza_neta(self):
        carga_objetivo = self.cargas[-1]
        fuerza_neta = [0, 0]
        tabla_procedimiento = []
        tabla_fuerzas = []

        # Calcular fuerza vectorial 
        for i, carga in enumerate(self.cargas[:-1], start=1):
            desplazamiento = OperacionesVectores.restar_puntos(carga, carga_objetivo)
            magnitud = OperacionesVectores.calcular_magnitud(desplazamiento)

            if magnitud == 0:
                print(f"La carga {i} está en la misma posición que la carga objetivo, se omite debido a división por cero")
                continue

            unitario = OperacionesVectores.calcular_vector_unitario(desplazamiento, magnitud)
            f_escalar = CalculadoraFuerza.k * carga.q * carga_objetivo.q / magnitud ** 2
            f_vectorial = [round(x * f_escalar, 2) for x in unitario]

            tabla_procedimiento.append([
                i,
                carga.q,
                tuple(carga.coordenadas),
                tuple(desplazamiento),
                magnitud,
                tuple(unitario),
                f_escalar,
                tuple(f_vectorial),
            ])

            tabla_fuerzas.append([i, f_vectorial[0], f_vectorial[1]])

            # se acumula la fuerza vectorial por cada iteracion
            fuerza_neta = [fuerza_neta[0] + f_vectorial[0], fuerza_neta[1] + f_vectorial[1]]

        headers_procedimiento = [
            "Carga",
            "Valor",
            "Coordenadas",
            "Desplazamiento",
            "Magnitud",
            "Unitario",
            "F",
            "F vectorial",
        ]
        print("\nPROCEDIMIENTO POR CADA CARGA")
        print(tabulate(tabla_procedimiento, headers=headers_procedimiento, tablefmt="simple_grid"))

        tabla_fuerzas.append(["SUMA (Fuerza neta)", fuerza_neta[0], fuerza_neta[1]])
        headers_fuerzas = ["N de fuerza vectorial", "x", "y"]
        print("\nSUMA DE FUERZAS VECTORIALES")
        print(tabulate(tabla_fuerzas, headers=headers_fuerzas, tablefmt="simple_grid"))

        # resultado final en Newtons
        print(f"\nFuerza neta = <{round(fuerza_neta[0],2)}, {round(fuerza_neta[1],2)}> N")
        print(f"La magnitud de la fuerza neta es: {round(OperacionesVectores.calcular_magnitud(fuerza_neta), 2)} N")



def main():
    n = int(input("Ingrese el número de cargas: "))
    calculadora = CalculadoraFuerza([])


    for _ in range(n - 1):
        print(f"---------------CARGA {_ + 1}-------------------")
        x = float(input("Ingrese la coordenada x de la carga: "))
        y = float(input("Ingrese la coordenada y de la carga: "))
        q = float(input("Ingrese el valor de la carga (Coulombs): "))

        calculadora.cargas.append(Carga(q, [x, y]))

    print(f"-----CARGA A LA QUE SE LE APLICA LA FUERZA-----")
    x = float(input("Ingrese la coordenada x de la carga: "))
    y = float(input("Ingrese la coordenada y de la carga: "))
    q = float(input("Ingrese el valor de la carga (Coulombs): "))

    calculadora.cargas.append(Carga(q, [x, y]))
    print("--------------------------------------------")

    calculadora.calcular_fuerza_neta()
    
    
if __name__ == '__main__':
    main()


   