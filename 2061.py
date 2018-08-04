linha = input()
linha = linha.split(' ')

numeroAbas = int(linha[0])
acoes = int(linha[1])

for i in range(acoes):
    acao = input()
    if acao == 'fechou':
        numeroAbas += 1
    else:
        numeroAbas -= 1

print(numeroAbas)
