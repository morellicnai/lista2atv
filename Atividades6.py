while True:
    num = int(input("Digite um número inteiro: "))

    fibonacci = [0, 1]

    while len(fibonacci) < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    print("Sequência de Fibonacci até o", num, "º termo:")
    for i in fibonacci:
        print(i)

    continuar = input("Deseja digitar outro número? (sim/não) ")
    if continuar.lower() != "sim":
        break