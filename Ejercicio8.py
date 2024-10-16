hermanos = int(input("¿Cuántos hermanos son?: "))
print(f"A los {hermanos} hermanos, bienvenidos a la consola, aquí vamos a indicar qué regalos recibirán o no según las notas académicas que han obtenido.")

hermanos_info = []

for i in range (hermanos):
  nom = input(f"¿Cómo te llamas hermano/a {i+1}? Ingrese tu nombre:  ")
  print(f"Hola {nom}")
  nota = float(input("¿Qué notas recibiste hoy de la escuela?:  "))
  print(f"Nota académica de {nom}: {nota}")

  if nota < 6:
    print(f"Ouh! {nom}, no hay regalo y sigues esforzando para el próximo intento")
  elif 6 <= nota and nota < 7:
    print(f"¡Felicitaciones {nom}! Has recibido el regalo de una comida en un bar de tu elección")
  elif 7 <= nota and nota <= 9:
    print(f"¡Felicitaciones {nom}! Has recibido el regalo de una ropa a tu elección")
  else:
    print(f"¡Felicitaciones! Has recibido dos regalos: una comida en un bar de tu elección y una ropa a tu elección")

