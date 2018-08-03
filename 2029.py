PI = 3.14

while True:
    try:
        volume = float(input())
        diametro = float(input())

        raio = diametro/2

        area = PI*raio*raio
        altura = volume/area

        print("ALTURA = %.2f" % altura)
        print("AREA = %.2f" % area)

    except EOFError:
        break
