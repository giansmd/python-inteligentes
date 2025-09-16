while True:
  try:
    first_number = int(input("Ingrese el primer número: "))
    break
  except ValueError:
    print("Error: Por favor ingrese un número entero válido.")

while True:
  try:
    second_number = int(input("Ingrese el segundo número: "))
    break 
  except ValueError:
    print("Error: Por favor ingrese un número entero válido.")

suma = first_number + second_number
resta = first_number - second_number
producto = first_number * second_number

print(f"La suma de los números {first_number} y {second_number} es: {suma}")
print(f"La resta de los números {first_number} y {second_number} es: {resta}")
print(f"El producto de los números {first_number} y {second_number} es: {producto}")