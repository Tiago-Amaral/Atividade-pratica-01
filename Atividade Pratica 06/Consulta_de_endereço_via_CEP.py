import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url).json()

    if "erro" in resposta:
        print("CEP inválido.")
        return

    print("Logradouro:", resposta.get('logradouro', 'N/A'))
    print("Bairro:", resposta.get('bairro', 'N/A'))
    print("Cidade:", resposta.get('localidade', 'N/A'))
    print("Estado:", resposta.get('uf', 'N/A'))

cep = input("Digite o CEP (somente números): ")
consultar_cep(cep)
