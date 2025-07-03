import re

def eh_palindromo(texto):
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


frase = "A base do teto desaba"
print(f"É palíndromo? {eh_palindromo(frase)}")