from math import log10, floor

def separar_en_digitos(num):
    logaritmo = log10(num)
    divisor = 10 ** floor(logaritmo)
    digitos = []
    while divisor >= 1:
        digitos.append(floor(num//divisor))
        num = num % divisor
        divisor = divisor // 10
    
    return digitos

print(sum(separar_en_digitos(2**1000)))