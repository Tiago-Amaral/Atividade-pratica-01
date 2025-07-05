import json

pessoa = {
    "Nome": "Ana",
    "Idade": 28,
    "Cidade": "Curitiba"
}

# Escrevendo em JSON
with open('pessoa.json', 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)

# Lendo do JSON
with open('pessoa.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
    print("Dados da pessoa:")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
