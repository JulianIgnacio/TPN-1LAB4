from datetime import datetime

fecha_1 = input("Ingrese la primera fecha (dd-mm-yyyy): ")
fecha_2 = input("Ingrese la segunda fecha (dd-mm-yyyy): ")

fecha_1 = datetime.strptime(fecha_1,"%d-%m-%Y")
fecha_2 = datetime.strptime(fecha_2,"%d-%m-%Y")

dif_fechas = fecha_2 - fecha_1
print(f"Entre dos fechas ingresadas hay {dif_fechas.days} días en total.")