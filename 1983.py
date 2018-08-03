
n = int(input())
maior = 0.0
inscricaoMaior = 0

for i in range(n):
    linha = input()
    inscricao, nota = linha.split(' ')
    nota = float(nota)

    if nota > maior:
        maior = nota
        inscricaoMaior = inscricao

if maior < 8.0:
    print("Minimum note not reached")
else:
    print(inscricaoMaior)
