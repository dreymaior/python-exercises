
linha = input().split(' ')

a, b = int(linha[0]), int(linha[1])

if b > 0:
    q = a // b
    r = a % b
else:
    b *= -1
    q = a // b
    q *= -1
    r = a % b

print(q, r)
