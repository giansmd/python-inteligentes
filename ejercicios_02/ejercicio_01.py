from utils.utils import ingresar_n, ingresar_str


def ingresar_nota(n_nota: int, n_estudiante: int):
    while True:
        nota = ingresar_n(f"la nota {n_nota} del estudiante {n_estudiante}")
        if nota <= 20:
            break
        else:
            print("Ingrese una nota válida (0-20)")
    return nota


def ingresar_estudiante(n_estudiante: int):
    nombre = ingresar_str(f"el nombre del estudiante {n_estudiante}")
    nota1 = ingresar_nota(1, n_estudiante)
    nota2 = ingresar_nota(2, n_estudiante)
    nota3 = ingresar_nota(3, n_estudiante)
    return nombre, [nota1, nota2, nota3]


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

lista_nueva_estudiantes = []


def generar_nueva_tupla(estudiante: tuple):
    nombre_estudiante = estudiante[0]
    promedio = 0
    notas_estudiante = estudiante[1]
    for nota in notas_estudiante:
        promedio += nota
    promedio /= 3
    promedio = round(promedio, 2)
    return nombre_estudiante, promedio


for estudiante in lista_estudiantes:
    lista_nueva_estudiantes.append(generar_nueva_tupla(estudiante))

# debug
for estudiante in lista_nueva_estudiantes:
    print(estudiante)
