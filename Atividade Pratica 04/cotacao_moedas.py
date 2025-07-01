import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

resposta = requests.get(url).json()
chave = f"{moeda}BRL"

if chave in resposta:
    dados = resposta[chave]
    print("Moeda:", dados["name"])
    print("Valor atual (R$):", dados["bid"])
    print("Máximo do dia:", dados["high"])
    print("Mínimo do dia:", dados["low"])
    print("Última atualização:", dados["create_date"])
else:
    print("Moeda não encontrada ou inválida.")
