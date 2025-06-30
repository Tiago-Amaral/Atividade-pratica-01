temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Converter para (C, F ou K): ").upper()

resultado = None

# Conversão para Celsius
if origem == "F":
    temp_c = (temp - 32) * 5/9
elif origem == "K":
    temp_c = temp - 273.15
else:
    temp_c = temp

# Conversão de Celsius para destino
if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida!")

if resultado is not None:
    print(f"Temperatura convertida: {resultado:.2f}°{destino}")