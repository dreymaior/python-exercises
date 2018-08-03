caso = 1;

while True:
    try:
        n = int(input())
        numeros = 0
        saida = ""

        if n == 0:
            saida = '0'
            numeros = 1
        elif n == 1:
            saida = '0 1'
            numeros = 2
        else:
            for i in range(n):
                if i == 0:
                    saida += '0 '
                    numeros += 1
                elif i == 1:
                    saida += '1 '
                    numeros += 1
                else:
                    for j in range(i):
                        saida += str(i) + ' '
                        numeros += 1
            for i in range(n):
                saida += str(n) + ' '
                numeros += 1

            saida = saida[:len(saida)-1]

        if numeros < 2:
            print("Caso {}: {} numero".format(caso, numeros))
        else:
            print("Caso {}: {} numeros".format(caso, numeros))

        print(saida)
        print()

        caso += 1
    except EOFError:
        break
