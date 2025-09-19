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
# for estudiante in lista_estudiantes:
#     print(estudiante)

lista_estudiantes.sort()

print("LISTA ORDENADA DE ESTUDIANTES:")
for estudiante in lista_estudiantes:
    print(estudiante)


nombre_a_buscar = ingresar_str("el nombre que se va a buscar")


def buscar_estudiante(nombre_a_buscar: str):
    for estudiante in lista_estudiantes:
        nombre_estudiante = estudiante[0]
        if nombre_estudiante == nombre_a_buscar:
            print(f"¡Estudiante encontrado!: {nombre_estudiante}")
            return estudiante
    return None


estudiante_encontrado = buscar_estudiante(nombre_a_buscar)

if estudiante_encontrado is not None:
    print(f"Nota: {estudiante_encontrado[1]}")
else:
    print("Estudiante no encontrado")