while True:
    num = int(input("Digite um número inteiro: "))

    fatorial = 1

    for i in range(2, num+1):
        fatorial *= i

    print("O fatorial de", num, "é", fatorial)

    resposta = input("Deseja continuar? (sim/não): ")
    if resposta.lower() != "sim":
        break