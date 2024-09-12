SueldoBasico= input("Ingrese su sueldo basico:")
AsistenciaPerfecta=40000
HoraExtra=5000
DescuentoJubilacion=(11/SueldoBasico) * 100
DescuentoObraSocial=(11/SueldoBasico) * 100
AñoAntigüedad=8000
SueldoTotalEmpleado=SueldoBasico+AsistenciaPerfecta+HoraExtra+AñoAntigüedad-DescuentoJubilacion-DescuentoObraSocial
print("Sueldo Empleado")
print(f"Sueldo Basico: {SueldoBasico}")
print(f"Asistencia Perfecta: {AsistenciaPerfecta}")
print(f"Horas Extra: {HoraExtra}")
print(f"Años de antigüedad : {AñoAntigüedad}")
print(f"Descuento por Jubilacion : {DescuentoJubilacion}")
print(f"Descuento por obra social : {DescuentoObraSocial}")
print(f"Sueldo total del empleado : {SueldoTotalEmpleado}")