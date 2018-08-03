def soma(lista):
    retorno = 0
    for i in lista:
        retorno += i

    return retorno

# const
PAR = 0

n = int(input())

linha = input()
linha = linha.split(' ')
carneiros = []
estrelasAtacadas = []
carneirosNaoRoubados = 0

for i in range(n):
    carneirosNaoRoubados += int(linha[i])
    carneiros.append(int(linha[i]))
    estrelasAtacadas.append(0)

proximaEstrela = 1

while proximaEstrela > 0 and proximaEstrela <= n:
    carneirosLocal = carneiros[proximaEstrela-1]
    if carneiros[proximaEstrela-1] > 0:
        estrelasAtacadas[proximaEstrela-1] = 1
        carneiros[proximaEstrela-1] -= 1
        carneirosNaoRoubados -= 1

    if carneirosLocal%2 != PAR:
        proximaEstrela += 1
    else:
        proximaEstrela -= 1


totalAtacadas = soma(estrelasAtacadas)

print(totalAtacadas, carneirosNaoRoubados)
