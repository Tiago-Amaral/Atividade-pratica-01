from datetime import datetime

def idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365  


ano = 2000
print(f"Idade em dias: {idade_em_dias(ano)} dias")
