while True:
    try:
        n = int(input())
        k = n//3
        m = n//2

        for i in range(n):
            if i < k:
                zerosExternos = i*'0'
                zerosInternos = (n-(i*2)-2)*'0'

                linha = zerosExternos + '2' + zerosInternos + '3' + zerosExternos
            elif i >= (n-k):
                zerosExternos = (n-i-1)*'0'
                zerosInternos = (n-2*(n-i+1)+2)*'0'
                linha = zerosExternos + '3' + zerosInternos + '2' + zerosExternos
            else:
                if i != m:
                    linha = k*'0' + (n-(2*k))*'1' + k*'0'
                else:
                    linha = k*'0' + ((n-(2*k))//2)*'1' + '4' + ((n-(2*k))//2)*'1' + k*'0'

            print(linha)

        print()

    except EOFError:
        break
