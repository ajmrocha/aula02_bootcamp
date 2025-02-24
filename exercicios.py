import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero_01 = int(input("Insira um número inteiro: "))
# numero_02 = int(input("Insira outro número inteiro: "))
# soma = numero_01 + numero_02
# print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numero = int(input("Insira um número inteiro: "))
# resto = numero % 5
# print(resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero_01 = int(input("Insira um número inteiro: "))
# numero_02 = int(input("Insira outro número inteiro: "))
# multiplicacao = numero_01 * numero_02
# print(multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero_01 = int(input("Insira um número inteiro: "))
# numero_02 = int(input("Insira outro número inteiro: "))

# resultado = numero_01 // numero_02  

# print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero = int(input("Insira um número inteiro: "))
# quadrado = numero ** 2
# print(quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero_01 = float(input("Insira um número flutuante: "))
# numero_02 = float(input("Insira outro número flutuante: "))
# soma = numero_01 + numero_02
# print(soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero_01 = float(input("Insira um número flutuante: "))
# numero_02 = float(input("Insira outro número flutuante: "))
# media = (numero_01 + numero_02) / 2
# print(media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# numero_base = float(input("Insira a base: "))
# expoente = float(input("Insira o expoente: "))
# potencia = numero_base ** expoente
# print(potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# temperatura_celsius = float(input("Insira a temperatura em Celsius: "))
# temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
# temperatura_fahrenheit = round(temperatura_fahrenheit, 2)
# print(temperatura_fahrenheit)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio_do_circulo = float(input("Insira o raio do círculo: "))
# area_do_circulo = math.pi * (raio_do_circulo ** 2)
# area_do_circulo = round(area_do_circulo, 2)

# print(area_do_circulo)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# nome = input("Insira seu nome: ")
# nome_maiusculo = nome.upper()
# print(nome_maiusculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome = input("Insira seu nome completo: ")
# nome_minusculo = nome.lower()
# print(nome_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Insira uma frase: ")
# frase_sem_espacos = frase.strip()
# print(frase_sem_espacos)
# print(len(frase_sem_espacos))

# frase = input("Insira uma frase: ")
# frase_sem_espaco = frase.replace(" ", "")
# print(frase_sem_espaco)
# print(len(frase_sem_espaco))

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data_do_usuario = input("Insira uma data no formato 'dd/mm/aaaa': ")

# data_do_usuario.split("/")
# dia, mes, ano = data_do_usuario.split("/")

# print(f"Dia: {dia}")
# print(f"Mês: {mes}")
# print(f"Ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# nome = input("Insira seu nome: ")
# sobrenome = input("Insira seu sobrenome: ")

# nome_completo = nome + " " + sobrenome
# print(nome_completo)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# Validação da idade
while True:
    try:
        idade_str = input("Insira sua idade: ")
        idade = int(idade_str)
        
        # Verificar se é um número inteiro positivo razoável
        if idade < 0 or idade > 120:
            print("Por favor, digite uma idade válida (entre 0 e 120).")
            continue
            
        break  # Sai do loop se a conversão for bem-sucedida e o valor for válido
    except ValueError:
        # Verifica se foi um número decimal (com ponto)
        if "." in idade_str:
            print("Erro: Por favor, digite apenas números inteiros.")
        else:
            print("Erro: Por favor, digite apenas números para a idade.")

# Verificação de idade para dirigir
if idade >= 18:
    # Validação da CNH
    while True:
        possui_cnh = input("Você possui CNH? (S/N): ").upper()
        if possui_cnh == "S" or possui_cnh == "N":
            break
        else:
            print("Entrada inválida. Digite S para Sim ou N para Não.")
    
    # Verificação da CNH
    if possui_cnh == "S":
        print("Você é maior de idade e possui CNH. Pode dirigir.")
    else:  # possui_cnh == "N"
        print("Você é maior de idade, mas não possui CNH. Não pode dirigir.")
        
else:
    print("Você é menor de idade. Não pode dirigir.")


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação



