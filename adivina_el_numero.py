#Este programa adivina un número del 1 al 10
'''
Escribe un programa en el que el ordenador elija un numero al azar entre 1 y 10,
y le pida al usuario que intente adivinarlo. Si el usuario adivina correctamente,
el programa debe mostrar "¡Correcto!". Si no, debe mostrar "Sigue intentando". Pista: Usa una variable para almacenar el número secreto, y utiliza condicionales 
para comparar el numero ingresado con el numero secreto
'''

NUMEROALEATORIO=3
print("dime un num del 1 al 10")
numero=int(input())
if(numero==NUMEROALEATORIO):
    print("Has acertado")
else:
    print("sigue intentando")

