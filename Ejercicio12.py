def funct_mes(input_mes):
  #Diccionario de meses
  meses = { 1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
         7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

  if 1 <= input_mes<= 12:
          return meses[input_mes]
  else:
    return  "El número del mes que has ingresado no es válido. Por favor, ingresa un número entre 1 y 12"


input_mes = int(input("Ingrese el número del mes que deseas saber: "))
nom_mes = funct_mes(input_mes)

#Verificar si la respuesta es un mes válido y aplicar el upper en el caso
if 1<= input_mes <= 12:
  print(f"El mes n° {input_mes} es: {nom_mes.upper()}")
else:
  print(nom_mes)