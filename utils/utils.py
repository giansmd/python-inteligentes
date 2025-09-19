def ingresar_ne(p_label: str):
    while True:
        try:
            number = int(input(f"Ingrese {p_label}: "))
            return number
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")


def ingresar_n(p_label: str):
    return ingresar_nn(p_label)


def ingresar_nn(p_label: str):
    while True:
        try:
            number = int(input(f"Ingrese {p_label}: "))
            if number > 0:
                break
        except ValueError:
            print("Error: Por favor ingrese un número natural válido.")
    return number


def ingresar_str(p_label: str):
    while True:
        string = input(f"Ingrese {p_label}: ")
        if len(string) != 0:
            break
    return string
