import requests

cep = input("Digite o CEP (somente números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url).json()

if "erro" not in resposta:
    print("Logradouro:", resposta["logradouro"])
    print("Bairro:", resposta["bairro"])
    print("Cidade:", resposta["localidade"])
    print("Estado:", resposta["uf"])
else:
    print("CEP inválido ou não encontrado.")
