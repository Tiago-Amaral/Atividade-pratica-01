import requests


resposta = requests.get("https://randomuser.me/api/").json()


usuario = resposta["results"][0]
nome = f"{usuario['name']['first']} {usuario['name']['last']}"
email = usuario["email"]
pais = usuario["location"]["country"]

print("Nome:", nome)
print("Email:", email)
print("País:", pais)