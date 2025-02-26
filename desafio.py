
nome_usuario = input("Digite seu nome: ")

if nome_usuario.isdigit():
    print("Nome inválido")
    exit()
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Você digitou apenas espaços")
    exit()
