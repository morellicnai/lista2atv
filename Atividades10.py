while True:
    numero = int(input("Digite um número inteiro: "))
    multiplos = []

    for i in range(1, 100):
        if i*numero < 100:
            multiplos.append(i*numero)

    print("Os múltiplos de", numero, "menores que 100 são:", multiplos)
    
    continuar = input("Deseja continuar? (sim/não): ")
    if continuar == 'não':
        break