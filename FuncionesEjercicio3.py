num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

def producto(num1,num2):
    resultado = 0
    resultado = num1 // num2
    return resultado
resultado_cociente = producto(num1,num2)

print(f"El Cociente de los dos numeros es: {resultado_cociente}")