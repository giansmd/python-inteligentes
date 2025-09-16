while True:
  try:
    time_in_seconds = float(input("Ingrese el tiempo recorrido en segundos: "))
    break
  except ValueError:
    print("Error: Por favor ingrese un número flotante válido.")

g = 9.8
altura_objeto = 0.5 * g * ((time_in_seconds) ** 2)
altura_objeto = round(altura_objeto, 2)

print(f"La altura a la que cayó el objeto fue de {altura_objeto} metros")