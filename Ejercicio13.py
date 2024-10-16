def tipo_triangulo(a,b,c):
   # Verifica si los lados cumplen con la desigualdad triangular
  if (a+b<=c) or (a+c<=b) or (b+c<=a):
   return "Con los lados que has ingresado no se puede formar un tríangulo. Por favor, intente de nuevo"
  elif a == b and a == c:
    # a == b == c
   return "¡Bien! Los valores de los lados que has ingresado logró formar un triángulo EQUILÁTERO."
  elif (a == b and a !=c) or ( a == c and a!= b) or (b == c and b!= a):
    # a == b or a == c or b == c
   return "¡Bien! Los valores de los lados que has ingresado logró formar un triángulo ISÓSCELES."
  else:
   return "¡Bien! Los valores de los lados que has ingresado logró formar un triángulo ESCALENO."

#Ingreso los valores de los lados de un triángulo
a = float(input("Ingrese el valor del lado A del triángulo: "))
b = float(input("Ingrese el valor del lado B del triángulo: "))
c = float(input("Ingrese el valor del lado C del triángulo: "))

# Verifica si los lados son mayores que 0
if a<= 0 or b <= 0 or c<= 0:
  print("Todos los lados deben tener una longitud mayor a 0 (cero)")
else:
  print(tipo_triangulo(a,b,c)) #Llamar a la función tipo_triangulo y muestra el resultado que corresponde

