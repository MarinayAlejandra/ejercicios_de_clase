# Este programa te da acceso a partir de contraseña
'''
Escribe un programa que le pida al usuario ingresar un nombre
 de usuario y una contraseña. Si el nombre de usuario es "admin" 
 y la contraseña es "1234", el programa debe mostrar "Acceso concedido". 
 Si no, debe mostrarontrolar el acceso. 
'''
USUARIO_BBDD="admin"
PASSWORD_BBDD=1234

print("ingresa el nombre de usuario")
usuario=(input()) 
print("Es necesario que crees una contraseña")
contrasena=int(input())

if(usuario == USUARIO_BBDD) and ( contrasena == PASSWORD_BBDD):
    print("Acceso concedido")
else:
    print("acceso denegado")
