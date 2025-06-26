valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15


valor_em_dolar = valor_reais / taxa_dolar
valor_em_euro = valor_reais / taxa_euro


print("Conversor de Moeda")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Em dólares: US$ {valor_em_dolar:.2f}")
print(f"Em euros: € {valor_em_euro:.2f}")