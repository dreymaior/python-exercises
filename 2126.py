caso = 1

while True:
    try:
        n1 = input()
        n2 = input()

        subsequencias = n2.count(n1)
        posicao = n2.rfind(n1)

        print("Caso #{}:".format(caso))

        if subsequencias > 0:
            print("Qtd.Subsequencias: {}".format(subsequencias))
            print("Pos: {}".format(posicao+1))
        else:
            print("Nao existe subsequencia")

        print()
        caso += 1

    except EOFError:
        break
