from utils.utils import ingresar_n, ingresar_str


def ingresar_nota(n_estudiante: int):
    while True:
        nota = ingresar_n(f"la nota del estudiante {n_estudiante}")
        if nota <= 20:
            break
        else:
            print("Ingrese una nota válida (0-20)")
    return nota


def ingresar_estudiante(n_estudiante: int):
    nombre = ingresar_str(f"el nombre del estudiante {n_estudiante}")
    nota = ingresar_nota(n_estudiante)
    return nombre, nota


def ingresar_estudiantes():
    cantidad_estudiantes = ingresar_n("la cantidad de estudiantes")
    lista_estudiantes = []
    for i in range(cantidad_estudiantes):
        lista_estudiantes.append(ingresar_estudiante(i + 1))
    return lista_estudiantes


lista_estudiantes = ingresar_estudiantes()

# debug
for estudiante in lista_estudiantes:
    print(estudiante)
