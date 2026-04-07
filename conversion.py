prefixes = {"giga": 9, "mega": 6, "kilo": 3, "mili": -3, "micro": -6, "nano": -9}

def main():
    conv = input("Ingrese la conversión deseada en el siguiente formato... \n" \
                "10 kilogramos a miligramos [Valor medida_con_prefijo a medida_con_prefijo]: ")

    elements = conv.split()
    value = float(elements[0])

    unit = ""

    found_1, found_2 = False, False
    from_prefix, to_prefix = "", ""

    for key in prefixes.keys():
        if found_1 and found_2:
            break

        if key in elements[1]:
            found_1 = True
            unit = elements[1][len(key):]
            from_prefix = key


        if key in elements[3]:
            found_2 = True
            unit = elements[3][len(key):]
            to_prefix = key
    
    res = f"El resultado de la conversion es: {convert(value, from_prefix, to_prefix, unit)} {to_prefix + unit}"
    print(res)


def convert(value, from_prefix, to_prefix, unit) -> float :
    if from_prefix not in prefixes.keys() or to_prefix not in prefixes.keys():
        raise ValueError("Usa un prefijo válido")

    original_power = prefixes[from_prefix]
    target_power = prefixes[to_prefix]

    difference = original_power - target_power  
    return value * 10 ** difference
    

if __name__ == "__main__":    
    main()