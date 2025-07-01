import random
import string


tamanho = int(input("Quantos caracteres a senha deve ter? "))


caracteres = string.ascii_letters + string.digits + string.punctuation


senha = ''.join(random.choices(caracteres, k=tamanho))

print("Senha gerada:", senha)
