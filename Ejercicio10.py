#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
#y muestre por pantalla cada uno de los productos en una línea distinta.
Compra = input('Productos de una cesta de la compra, separados por comas ')
Compra = Compra.replace(',', '\n')
print(Compra)