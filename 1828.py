# constantes
escolhas = {
    "tesoura" : 0,
    "papel" : 1,
    "pedra" : 2,
    "lagarto" : 3,
    "Spock" : 4
}

NUM_ESCOLHAS = 5


def jogo(escolhaSheldon, escolhaRaj):
    resultado = regras[escolhas[escolhaSheldon]][escolhas[escolhaRaj]]

    if resultado == -1:
        retorno = "Raj trapaceou"
    elif resultado == 0:
        retorno = "De novo"
    else:
        retorno = "Bazinga"

    return retorno

############################################################################
# main

# matriz do jogo
#      |  0  |  1  |  2  |  3  |  4
#   0  |  0  |  1  | -1  |  1  | -1
#   1  | -1  |  0  |  1  | -1  |  1
#   2  |  1  | -1  |  0  |  1  | -1
#   3  | -1  |  1  | -1  |  0  |  1
#   4  |  1  | -1  |  1  | -1  |  0
#

# preencher matriz de regras
regras = [[0*i for i in range(NUM_ESCOLHAS)] for j in range(NUM_ESCOLHAS)]

for i in range(NUM_ESCOLHAS):
    for j in range(NUM_ESCOLHAS):
        if i == 0:
            if j == 1 or j == 3:
                regras[i][j] = 1
            elif j == 2 or j == 4:
                regras[i][j] = -1
        elif i == 1:
            if j == 0 or j == 3:
                regras[i][j] = -1
            elif j == 2 or j == 4:
                regras[i][j] = 1
        elif i == 2:
            if j == 0 or j == 3:
                regras[i][j] = 1
            elif j == 1 or j == 4:
                regras[i][j] = -1
        elif i == 3:
            if j == 0 or j == 2:
                regras[i][j] = -1
            elif j == 1 or j == 4:
                regras[i][j] = 1
        else:
            if j == 0 or j == 2:
                regras[i][j] = 1
            elif j == 1 or j == 3:
                regras[i][j] = -1

t = int(input())

for i in range(t):
    linha = input()
    espacoBranco = linha.find(' ')

    escolhaSheldon = linha[:espacoBranco]
    escolhaRaj = linha[espacoBranco+1:]

    print("Caso #{}: {}!".format(i+1,jogo(escolhaSheldon,escolhaRaj)))
