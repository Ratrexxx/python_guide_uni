# Escribir un programa para convertir una medida dada en pies a sus equivalentes en:
# a.	Yardas
# b.	Pulgadas
# c.	Centímetros
# d.	Metros
# (1 pie =12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54cm, 1m= 100cm).
# Leer el número de pies e imprimir el número de yardas, pies, pulgadas, centímetros y metros.

foots = float(input("Please enter the amount of foots you want to convert: "))

yards = foots / 3
inches = foots * 12
centimeters = inches * 2.54
meters = centimeters / 100

print(f"{foots:.2f} foots are equivalent to:")
print(f"{yards:.2f} yards")
print(f"{inches:.2f} inches")
print(f"{centimeters:.2f} centimeters")
print(f"{meters:.2f} meters")
