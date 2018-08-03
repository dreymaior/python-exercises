# const
IMPAR = 1

n = int(input())

linha = input()
linha = linha.split(' ')
estrelas = {}
estrelasAtacadas = 0
carneirosNaoRoubados = 0
estrela = []

for i in range(n):
    carneiros = int(linha[i])
    carneirosNaoRoubados += carneiros
    estrelas.update({i : [carneiros, False]})

proximaEstrela = 1

while proximaEstrela > 0 and proximaEstrela <= n:
    estrela = estrelas.get(proximaEstrela-1)
    carneiros = estrela[0]
    if (not(estrela[1])):
        estrela[1] = True
        estrelasAtacadas += 1

    if carneiros > 0:
        estrela[0] -= 1
        carneirosNaoRoubados -= 1

    if carneiros%2 == IMPAR:
        proximaEstrela += 1
    else:
        proximaEstrela -= 1

print(estrelasAtacadas, carneirosNaoRoubados)
