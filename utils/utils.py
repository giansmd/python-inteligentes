def ingresar_n(p_label: str):
    while True:
        try:
            number = int(input(f"Ingrese {p_label}: "))
            if number > 0:
                break
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")
    return number


def ingresar_str(p_label: str):
    string = input(f"Ingrese {p_label}: ")
    return string
