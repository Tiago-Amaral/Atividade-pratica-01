import csv

dados = [
    ['João', 30, 'São Paulo'],
    ['Maria', 25, 'Rio de Janeiro'],
    ['Pedro', 40, 'Belo Horizonte']
]

with open('pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['Nome', 'Idade', 'Cidade'])  # cabeçalho
    writer.writerows(dados)

print("Arquivo 'pessoas.csv' criado com sucesso.")
