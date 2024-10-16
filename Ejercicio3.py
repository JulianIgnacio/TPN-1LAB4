sueldo_basico = int(input("Ingrese su sueldo basico:"))
horas_extra = int(input("Ingrese sus horas extras:"))
año_de_antiguedad = int(input("Ingrese sus años de antiguedad:"))
asistencia_perfecta = 40000
valor_hora_extra = 5000
valor_de_antiguedad = 8000


# Cálculos
total_horas_extra = horas_extra * valor_hora_extra
total_antiguedad = año_de_antiguedad * valor_de_antiguedad
sueldo_bruto = sueldo_basico + asistencia_perfecta + total_horas_extra + total_antiguedad
descuento_jubilacion = sueldo_bruto * 0.11
descuento_obra_social = sueldo_bruto * 0.02
descuento_total = descuento_jubilacion + descuento_obra_social
sueldo_neto = sueldo_bruto - descuento_total

# Imprimir boleta de liquidación en consola
print("\n================= BOLETA DE LIQUIDACIÓN DE HABERES =================")
print(f"Sueldo básico:               ${sueldo_basico:,.2f}")
print(f"Bonus por asistencia perfecta: ${asistencia_perfecta:,.2f}")
print(f"Pago por horas extra ({horas_extra} horas):      ${total_horas_extra:,.2f}")
print(f"Antigüedad ({año_de_antiguedad} años):           ${total_antiguedad:,.2f}")
print("-----------------------------------------------------------------")
print(f"Sueldo bruto:                ${sueldo_bruto:,.2f}")
print(f"Descuento jubilación (11%):   -${descuento_jubilacion:,.2f}")
print(f"Descuento obra social (2%):   -${descuento_obra_social:,.2f}")
print(f"Descuento total:              -${descuento_total:,.2f}")
print("-----------------------------------------------------------------")
print(f"Sueldo neto:                 ${sueldo_neto:,.2f}")
print("=================================================================\n")