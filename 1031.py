#  imcompleted

def restante(n, k):
    r = 0
    for i in range(1, n):
        r = (r + k) % i;

    return r


n = int(input())
k = 1

while n != 0:

    while True:
        if restante(n, k) != 11:
            k += 1
        else:
            break

    print("{}".format(k))

    n = int(input())
