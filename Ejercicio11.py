#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una
#cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades
#con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
Producto = input('Introduce el producto: ')
Precio = float(input('Introducde el precio unitario: '))
Unidades = int(input('Introduce el número de unidades: '))
Total = Precio * Unidades
print(Producto, 'vale {Precio:9.2f} € x {Unidades:3d} unidades y en total cuesta {Total:11.2f}'
      .format(Precio = Precio, Unidades = Unidades, Total = Total))