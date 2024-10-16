x = int(input("Ingrese un número que necesitas para saber si es primo o no: "))

def num_primo(x):
  i = 2
  primo = True

  while i < x and primo:
    if x % i == 0:
      primo = False
    else:
      i = i + 1
  return primo

if num_primo(x):
  print("El valor de x que has ingresado SI es un número primo")
else:
  print("El valor de x que has ingresado NO es un número primo")