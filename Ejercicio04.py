#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión donde el prefijo es el código del país +34,
#y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono
#con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
Número = input('Dime cual es tu número como +34-913724710-56')
print('Tu número de telefono es', Número[4:13])