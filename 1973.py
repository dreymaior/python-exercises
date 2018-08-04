# const
IMPAR = 1

n = int(input())

linha = input()

estrelas = {}
estrelasAtacadas = 0
carneirosNaoRoubados = 0
estrela = []

for i in range(n-1):
    espacoBranco = linha.find(' ')
    carneiros = int(linha[:espacoBranco])
    linha = linha[espacoBranco+1:]
    carneirosNaoRoubados += carneiros
    estrelas.update({i : [carneiros, False]})

carneiros = int(linha)
carneirosNaoRoubados += carneiros
estrelas.update({n-1 : [carneiros, False]})

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
