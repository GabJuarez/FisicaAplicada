"""Hacer una función que haga los cálculos para calcular la resistencia equivalente, 
corriente a través de la batería  y voltajes o corrientes en cada resistor, para un 
circuito en serie o paralelo """

class Resistor:
    def __init__(self, resistencia):
        self.resistencia = resistencia

class Circuito:
    def __init__(self, resistores, paralelo, voltaje):
        self.resistores = resistores
        self.paralelo = paralelo
        self.voltaje = voltaje

    def CalcularResistenciaEquivalente(self):
        resistencia_equivalente = 0
        if not self.paralelo:
            for resistor in self.resistores:
                resistencia_equivalente += resistor.resistencia
        else:
            inversos = 0 
            for resistor in self.resistores:
                inversos += 1 / resistor.resistencia
            resistencia_equivalente = inversos ** -1
        return resistencia_equivalente
            
    def CalcularCorriente(self, resistencia_equivalente):
        return self.voltaje / resistencia_equivalente
    

    def CalcularVoltajeCadaResistor(self, corriente):
        if self.paralelo:
         return [self.voltaje / x.resistencia for x in self.resistores]
        else:    
            return [x.resistencia * corriente for x in self.resistores]
    

def main():
    # paralelo
    r1 = Resistor(10000)
    r2 = Resistor(2000)
    r3 = Resistor(1000)

    resistores = [r1, r2, r3]
    c = Circuito(resistores, True, 9)
    re = c.CalcularResistenciaEquivalente()
    corriente = c.CalcularCorriente(re)
    votaje_resistor = c.CalcularVoltajeCadaResistor(corriente)
    print(re)
    print(corriente)
    print(votaje_resistor)

    # en serie
    rs1 = Resistor(3000)
    rs2 = Resistor(10000)
    rs3 = Resistor(5000)

    resistores_serie = [rs1, rs2, rs3]
    cs = Circuito(resistores_serie, False, 9)
    res = cs.CalcularResistenciaEquivalente()
    corriente_serie = cs.CalcularCorriente(res)
    votaje_resistor_serie = cs.CalcularVoltajeCadaResistor(corriente_serie)
    print(res)
    print(corriente_serie)
    print(votaje_resistor_serie)


if __name__ == "__main__":
    main()