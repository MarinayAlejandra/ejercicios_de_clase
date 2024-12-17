def contar_vocales(frase):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador=0
    for letra in frase:
        if letra in vocales:
            contador + 1
    return contador
print (contar_vocales("Hola Pyithon"))