def suma(x, y):
    resultado=x + y 
    return resultado
print ("el resultado de la suma es", suma(5,4))
def resta(a, b):
    res = a - b
    return res 
print ("el resultado de la resta es ", resta(10,5))

def multiplicación (x, y):
    resultado= x * y
    return resultado

def siguiente (num):
    resultado= num+1
    return resultado
print ("el resultado de siguiente es", siguiente(5))

def mayor_de_dos(a, b):
    if (a > b ):
        if (a > c):
          return a
        else:
            return c 
    else:
        if(b>c):
            return b
        else:
            return c

print ("el mayor es", mayor_de_tres (4,))

def mayor_de_tres(a, b, c):
    if (a > b or c ):
        return a
    else:
        return b or c
print ("el mayor es",mayor_de_tres (1,2,3))

def multiplicar (x1, x2):
    res = x1 * x2
    return res
print("El resultado es:", multiplicar(4,7))



def contar_vocales(frase):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador=0
    for letra in frase:
        if letra in vocales:
            contador + 1
    return contador
print (contar_vocales("Hola Pyithon"))