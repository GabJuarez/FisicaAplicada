from math import sqrt
from tabulate import tabulate
class Carga:

    def __init__(self, q, coordenadas):
        self.q = q
        self.coordenadas = coordenadas

class OperacionesVectores:

    @staticmethod
    def restar_puntos( carga1, carga2) -> tuple[(int, int)]:
        return (carga2.coordenadas[0] - carga1.coordenadas[0], carga2.coordenadas[1] - carga1.coordenadas[1])
    
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

    @staticmethod
    def calcular_fuerza_vectorial(carga1, carga2):
        desplazamiento = OperacionesVectores.restar_puntos(carga1, carga2)
        magnitud = OperacionesVectores.calcular_magnitud(desplazamiento)
        unitario = OperacionesVectores.calcular_vector_unitario(desplazamiento, magnitud)

        # calcular fuerza
        f = CalculadoraFuerza.k * carga1.q * carga2.q / magnitud ** 2
        return [x * f for x in unitario]
    
    
    def calcular_fuerza_neta(self):
        ultima = self.cargas.pop()
        res = [0, 0]
        tabla_procedimiento = []
        tabla_fuerzas = []

        for i, carga in enumerate(self.cargas, start=1):
            desplazamiento = OperacionesVectores.restar_puntos(carga, ultima)
            magnitud = OperacionesVectores.calcular_magnitud(desplazamiento)
            unitario = OperacionesVectores.calcular_vector_unitario(desplazamiento, magnitud)
            f_escalar = CalculadoraFuerza.k * carga.q * ultima.q / magnitud ** 2
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
            res = [res[0] + f_vectorial[0], res[1] + f_vectorial[1]]

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

        tabla_fuerzas.append(["SUMA (Fuerza neta)", res[0], res[1]])
        headers_fuerzas = ["N de fuerza vectorial", "x", "y"]
        print("\nSUMA DE FUERZAS VECTORIALES")
        print(tabulate(tabla_fuerzas, headers=headers_fuerzas, tablefmt="simple_grid"))



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


   