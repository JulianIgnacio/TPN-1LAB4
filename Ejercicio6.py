import math

d = float(input("Ingrese el valor del diámetro de una esfera que se quiere calcular: "))

r = d//2
calculo = 4/3 * math.pi*r**3
vol = calculo

print(f"El volumen de la esfera de diámetro solicitado es: {vol}")