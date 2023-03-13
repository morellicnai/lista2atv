while True:
    num = int(input("Digite um número inteiro: "))
    binario = ""

    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num = num // 2

    print("O número em binário é:", binario)

    resposta = input("Deseja continuar? (sim/não): ")
    if resposta.lower() != "sim":
        break