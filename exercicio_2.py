
km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))

preco = (km * 0.15) + (dias * 60)

print(f"O preço a ser pago é de R${preco:.2f}")