import csv

with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    reader = csv.reader(arquivo)
    for linha in reader:
        print(linha)
