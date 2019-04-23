#Rodrigo Alvarez, 57008 II
from decimal_to_hexa import decimal_to_hexa

#Funcion que se encarga de que el valor que se ingrese sea de tipo int. Si se ingresa otro tipo, salta error.
def interfaz_parcial_dth(num):
    try:
        num = int(num)
        return decimal_to_hexa(num)
    except ValueError:
        return "Disculpe, solo acepto números!"