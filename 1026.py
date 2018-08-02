def unsigned(n):
    return n & 0xFFFFFFFF

while True:
    try:
        linha = input()
        i = linha.find(' ')

        n1 = unsigned(int(linha[:i]))
        n2 = unsigned(int(linha[i+1:]))

        sum = n1 ^ n2


        print(sum)
    except EOFError:
        break;
