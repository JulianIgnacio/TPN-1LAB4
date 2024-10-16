import random

# Definir partes
partes = ["mejor parte", "parte mediana", "peor parte"]

#Definir valores de las partes
valores = [random.randint(0,100) for p in partes]

# Quien parte y reparte
quien_reparte = "El que reparte"

# Distribuir partes
def repartir_partes():
    partes_repartidas = random.sample(partes, len(partes))
    return partes_repartidas

#Definir y mostrar valores aleatorios
def valores_partes():
    #Valores repartidos
    valores_repartidos =[ valores[partes.index(p)] for p in repartir_partes()]
    return valores_repartidos

# Reparto de partes
reparto = repartir_partes()
reparto_valor = valores_partes()

# Asignación de partes

#resultado = f"{quien_reparte} se queda con la {reparto[0]} con un valor de {reparto_valor[0]}.\n" \
 #           f"El segundo se queda con la {reparto[1]} con un valor de {reparto_valor[1]}.\n" \
  #          f"El último se queda con la {reparto[2]} con un valor de {reparto_valor[2]}."

resultado = (
    f"{quien_reparte} se queda con la {reparto[0]} (valor: {reparto_valor[0]}).\n"
    f"{quien_reparte} se queda con la {reparto[1]} (valor: {reparto_valor[1]}).\n"
    f"{quien_reparte} se queda con la {reparto[2]} (valor: {reparto_valor[2]})."
)
print(resultado)
