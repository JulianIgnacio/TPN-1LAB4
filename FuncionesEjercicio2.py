num = int(input("Ingrese números de más de dos dígitos: "))

def suma_dosdig(num):
  suma = 0
  while num > 0:
    digito = num % 10
    suma += digito
    num //= 10
  return suma

resultado_suma = suma_dosdig(num)

print(f"El total de la suma de los dígitos de un entero es: {resultado_suma}")
