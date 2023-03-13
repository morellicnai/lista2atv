while True:
    num = int(input("Digite um número inteiro: "))

    perfeitos = []
    for i in range(1, num + 1):
        soma = 0
        for j in range(1, i):
            if i % j == 0:
                soma += j
        if soma == i:
            perfeitos.append(i)

    if len(perfeitos) == 0:
        print("Não foram encontrados números perfeitos menores ou iguais a", num)
    else:
        print("Foram encontrados", len(perfeitos), "números perfeitos menores ou iguais a", num)
        print("Os números perfeitos encontrados são:", perfeitos)

    resposta = input("Deseja continuar? (sim/não): ")
    if resposta.lower() != "sim":
        break