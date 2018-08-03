nc = int(input())

for i in range(nc):
    linha = input()
    espaco = linha.find(' ')

    n = int(linha[:espaco])
    k = int(linha[espaco+1:])

    vecInicio = [0*i for i in range(n)]
    pontoInicio = 1
    for j in range(n, 0, -1):
        pontoInicio = (pontoInicio + k - 2) % j + 1
        vecInicio[j-1] = pontoInicio

    vecSobreviventes = [0*i for i in range(n)]
    sobrevivente = 0
    for j in range(1, n+1):
        if j == 1:
            vecSobreviventes[j-1] = 1
        else:
            if vecSobreviventes[j-2] < vecInicio[j-1]:
                vecSobreviventes[j-1] = vecSobreviventes[j-2]
            else:
                vecSobreviventes[j-1] = vecSobreviventes[j-2]+1

    print("Case {}: {}".format(i+1,vecSobreviventes[n-1]))
