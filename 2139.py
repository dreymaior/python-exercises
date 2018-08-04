PAR = 0
meses = []

for i in range(12):
    if i < 7:
        if i == 1:
            meses.append(29)
        else:
            if i%2 == PAR:
                meses.append(31)
            else:
                meses.append(30)
    else:
        if i%2 == PAR:
            meses.append(30)
        else:
            meses.append(31)

while True:
    try:
        linha = input()
        linha = linha.split(' ')

        mes = int(linha[0])
        dia = int(linha[1])

        faltam = 0

        if mes == 12:
            if dia == 25:
                print("E natal!")
            elif dia == 24:
                print("E vespera de natal!")
            elif dia > 25:
                print("Ja passou!")
            else:
                print("Faltam {} dias para o natal!".format(25-dia))
        else:
            for j in range(mes, 12):
                if j == mes:
                    faltam += meses[j-1]-dia
                else:
                    faltam += meses[j-1]

            faltam += 25

            print("Faltam {} dias para o natal!".format(faltam))

    except EOFError:
        break
