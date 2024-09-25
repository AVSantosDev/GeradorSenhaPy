#Usar 8 caracteres
#maiúsculas e minúsculas
#símbulos e espaços

   
import string
import random

def gerarSenha(qtdTotal, qtdEspecial, qtdNumeros, letMaiuscula):
    if qtdEspecial + qtdNumeros > qtdTotal:
        return "Erro: A quantidade de caracteres especiais não pode ser maior que o total de caracteres."


    letrasMinusculas = string.ascii_lowercase
    letrasMaiusculas = string.ascii_uppercase if letMaiuscula else ""
    numeros = string.digits
    caracteresEspeciais = string.punctuation

    listaCaracteres = letrasMinusculas + letrasMaiusculas
    if not listaCaracteres:
        return "Erro: Não há caracteres suficientes para gerar a senha."
    
    senha = random.SystemRandom().choices(caracteresEspeciais, k = qtdEspecial)
    senha += random.SystemRandom().choices(numeros, k = qtdNumeros)
    qtdRestante = qtdTotal - (qtdEspecial + qtdNumeros)
    senha += random.SystemRandom().choices(listaCaracteres, k = qtdRestante)
    random.shuffle(senha)

    return ''.join(senha)

try:
    qtdTotal = int(input("Digite a quantidade de caracteres da senha: "))
    qtdEspecial = int(input("Digite a quantidade de caracteres espéciais: "))
    qtdNumeros = int(input("Digite a quantidade de caracteres númericos: "))
    letMaiuscula = input("Incluir letra maiúscula (s/n): ").lower() == 's'

    senhaGerada = gerarSenha(qtdTotal, qtdEspecial, qtdNumeros, letMaiuscula)
    print("Senha gerada: ", senhaGerada)

except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos para as quantidades.")
