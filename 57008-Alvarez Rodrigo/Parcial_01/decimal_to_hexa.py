#Rodrigo Alvarez, 57008 II
import math

#En esta funcion se verifica el valor del modulo de %, para asignar las bases del sistema hexadecimal.

def mod_to_hexa(mod):
    if mod == 10:
        return 'A'
    elif mod == 11:
        return 'B'
    elif mod == 12:
        return 'C'
    elif mod == 13:
        return 'D'
    elif mod == 14:
        return 'E'
    elif mod == 15:
        return 'F'
    else:
        return str(mod)

#En esta funcion se recibe un numero decimal y se devuelve el mismo numero pero en base hexadecimal
def decimal_to_hexa(decimal):
    hexadecimal = ''
    while True:
        if (decimal//16)//16 == 0:
            mod = decimal%16
            decimal = decimal//16
            if decimal != 0:
                hexadecimal = mod_to_hexa(decimal) + mod_to_hexa(mod)+ hexadecimal 
            elif decimal == 0:
                hexadecimal =  mod_to_hexa(mod) + hexadecimal
            break
        mod = decimal%16
        decimal = decimal//16
        hexadecimal =mod_to_hexa(mod)+ hexadecimal 
    return hexadecimal
