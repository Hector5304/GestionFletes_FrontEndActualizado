"""
Script simple para calcular el dígito verificador de un RUT chileno
Código original del usuario
"""
import sys
import operator
import math

def calcular_dv_rut():
    """Calcula el dígito verificador de un RUT"""
    rut = input("Rut (primeros 8 dígitos sin puntos): ")
    rut_list = []
    num_cal = [3, 2, 7, 6, 5, 4, 3, 2]

    for i in rut:
        rut_list.append(i)

    rut_list_int = [int(x) for x in rut_list]

    calculo = list(map(operator.mul, rut_list_int, num_cal))

    def dv(n):
        x = sum(list(n))
        e = math.floor(x / 11)
        f = x - (11 * e)
        h = 11 - f
        
        if (h == 11):
            h = "0"
        elif (h == 10):
            h = "k"
        return(h)

    print("El dígito verificador es:", dv(calculo))


if __name__ == "__main__":
    calcular_dv_rut()
