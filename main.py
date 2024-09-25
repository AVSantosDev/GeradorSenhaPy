#Usar 8 caracteres
#maiúsculas e minúsculas
#símbulos e espaços

   
import string
import random
import hashlib

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


 #Modo usando tabela hash
#def criptografarPalavra(palavra):
    # hashObj  = hashlib.sha256(palavra.encode()) 
    # return hashObj.hexdigest()

def criptografarPalavra(palavra, deslocamento):
    criptografada = ""

    #Utilizando modelo de cifra de Cesar para deslocar a palavra no alfabeto
    for char in palavra:
        if char.isalpha():
            deslocando = ord(char) + deslocamento
            if char.islower():
                if deslocando > ord('z'):
                    deslocando -= 26
            elif char.isupper():
                if deslocando > ord ('Z'):
                    deslocando -= 26
            criptografada += chr(deslocando)
        else:
            criptografada += char
    return criptografada


try:
    print("************************************************")
    opcaoPrimaria = input("Você deseja Gerar uma senha digite 1\nVocê deseja Criptografar uma palavra Digite 2: ")
    
    if opcaoPrimaria == '1':
        print("************************************************")
        qtdTotal = int(input("Digite a quantidade de caracteres da senha: "))
        qtdEspecial = int(input("Digite a quantidade de caracteres espéciais: "))
        qtdNumeros = int(input("Digite a quantidade de caracteres númericos: "))
        letMaiuscula = input("Incluir letra maiúscula (s/n): ").lower() == 's'

        senhaGerada = gerarSenha(qtdTotal, qtdEspecial, qtdNumeros, letMaiuscula)
        print("Senha gerada: ", senhaGerada)

    elif opcaoPrimaria == '2':
        print("************************************************")
        palavra = input("Digite a palavra que deseja criptografar: ")
        deslocamento = int(input("digite a quantidade de deslocamento: "))
        palavraCriptografada = criptografarPalavra(palavra, deslocamento)
        print("Palavra criptografada é: ", palavraCriptografada)
        print("Programa encerrado")

    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")


except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos para as quantidades.")
