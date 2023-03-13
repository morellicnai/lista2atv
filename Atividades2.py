while True:
    numero = int(input("Digite um número inteiro: "))

    soma_digitos = 0
    while numero > 0:
        digito = numero % 10
        soma_digitos += digito
        numero //= 10

    print("A soma dos dígitos do número é:", soma_digitos)

    resposta = input("Deseja somar outro número? (sim/nnão): ")
    if resposta.lower() != "sim":
        break