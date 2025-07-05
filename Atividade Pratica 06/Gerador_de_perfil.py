import requests

def gerar_perfil():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url).json()
    usuario = resposta['results'][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)

gerar_perfil()
