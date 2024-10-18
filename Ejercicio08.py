#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre
#por pantalla el número de euros y el número de céntimos del precio introducido.
Precio = input('¿Cual es el precio del producto en euros con dos decimales?' )
Euros, centimos = (Precio.split(','))
print('Tu producto cuesta', Euros, 'Є con',centimos, 'céntimos')