persona_1 = input("Ingrese su nombre: ")
persona_2 = input("Ingrese su nombre: ")
persona_3 = input("Ingrese su nombre: ")

humedad = int(input("Ingrese el valor del porcentaje de la humedad actual: "))
print(f"Humedad actual: {humedad}%")

porc_1 = int(input(f"{persona_1}, por favor, ingrese tu porcentaje aproximado: "))
print(f"Porcentaje de {persona_1}: {porc_1}%")

porc_2 = int(input(f"{persona_2}, por favor, ingrese tu porcentaje aproximado: "))
print(f"Porcentaje de {persona_2}: {porc_2}%")

porc_3 = int(input(f"{persona_3}, por favor, ingrese tu porcentaje aproximado: "))
print(f"Porcentaje de {persona_3}: {porc_3}%")

dif_1 = abs(humedad - porc_1)
dif_2 = abs(humedad - porc_2)
dif_3 = abs(humedad - porc_3)

print("La cuenta será abonada por el que más lejos esté del porcentaje de humedad del día, por lo tanto:")
if porc_1 < porc_2 and porc_1 < porc_3:
  print(f"{persona_1} pagará la cuenta")
elif porc_2 < porc_1 and porc_2 < porc_3:
  print(f"{persona_2} Pagará la cuenta")
else: print(f"{persona_3} Pagará la cuenta")