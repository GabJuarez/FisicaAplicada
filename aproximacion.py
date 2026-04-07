from tabulate import tabulate
from math import exp

def factorial (x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

def expansion_e (x, n):
    if n == 1:
        return 1, []
    
    sum = 1 + x
    expansion = [1, x]

    for i in range(2, n, 1):
        sum = sum + x ** i / factorial(i)
        expansion.append(sum)

    return sum, expansion

def main():
    n = 100
    x = 1

    sum, expansion = expansion_e(x, n)

    table = [[1, expansion[0], exp(x) - expansion[0], exp(x) - expansion[0] / exp(x) * 100],
             [2, expansion[1], exp(x) - expansion[1], exp(x) - expansion[1] / exp(x) * 100]]
    
    for i in range(2, n, 1):
        real = exp(x)
        aprox = expansion[i]
        abs = real - aprox
        rel = abs / real * 100

        temp = [i + 1, expansion[i], abs, rel]
        table.append(temp)
        

    headers = ["Término N", "Suma", "Error absoluto", "Error relativo"]
    print(tabulate(table, headers=headers, tablefmt="simple_grid"))

main()

   
