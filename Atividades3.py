while True:
    num = int(input("Digite um número inteiro: "))

    print("Números primos menores ou iguais a", num, ":")

    for i in range(2, num+1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(i)

    resposta = input("Deseja continuar? (sim/não): ")
    if resposta.lower() != "sim":
        break