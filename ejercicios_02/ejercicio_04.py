from utils.utils import ingresar_ne, ingresar_nn, ingresar_str


def ingresar_nombre_estudiante(n: int):
    return ingresar_str(f"el nombre del estudiante {n}")


def ingresar_nota_estudiante(n: int):
    return ingresar_ne(f"una nota del estudiante {n}")


def registrar_dict_alumnos():
    dict_alumnos = {}
    cantidad_alumnos = ingresar_nn("la cantidad de alumnos")
    for i in range(cantidad_alumnos):
        # PASO. registrar nombre
        while True:
            nombre_estudiante = ingresar_nombre_estudiante(i + 1)
            if dict_alumnos.get(nombre_estudiante) is None:
                break
            print("Error: el nombre ya existe en el diccionario. Esbriba otro.")

        # PASO. si el nombre no existe, registrar la lista de notas
        lista_notas_estudiante = []
        while True:
            nota_estudiante = ingresar_nota_estudiante(i + 1)
            if nota_estudiante >= 0 and nota_estudiante <= 20:
                lista_notas_estudiante.append(nota_estudiante)
            elif nota_estudiante > 20:
                print("Nota no válida. No se registró")
            elif len(lista_notas_estudiante) == 0:
                print("Escbriba al menos una nota.")
            else:
                break
        dict_alumnos[nombre_estudiante] = lista_notas_estudiante

    return dict_alumnos


dict_alumnos = registrar_dict_alumnos()


def get_alumnos_con_nota_promedio(dict_alumnos):
    dict_alumnos_con_nota_promedio = {}

    for alumno in dict_alumnos.items():
        nombre = alumno[0]
        notas = alumno[1]
        suma = 0
        for nota in notas:
            suma += nota
        promedio = suma / len(notas)  # tiene que ingresar al menos una nota
        dict_alumnos_con_nota_promedio[nombre] = round(promedio, 2)

    return dict_alumnos_con_nota_promedio


print(get_alumnos_con_nota_promedio(dict_alumnos))
