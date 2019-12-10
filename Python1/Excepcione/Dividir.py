def dividir(n1, n2):
    try:
        resultado = n1 / n2
    except ZeroDivisionError:
        print("Has dividido entre cero bobo")
    else:
        print("El resultado es: ",resultado)
    finally:
        print("Finalizado")
dividir(13, 0)
dividir(4, 2)