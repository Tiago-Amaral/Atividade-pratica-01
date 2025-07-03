def calcular_gorjeta(valor_conta, porcentagem):
    gorjeta = valor_conta * (porcentagem / 100)
    return gorjeta


valor = 150
porcentagem = 10
print(f"Gorjeta: R${calcular_gorjeta(valor, porcentagem):.2f}")