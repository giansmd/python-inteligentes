from utils.utils import ingresar_ne, ingresar_str
from typing import Dict

agenda = {
    "Gian": "949547447",
    "Franco": "998651869",
    "Miguel": "949476059",
    "Lucero": "995085050",
}


def get_opcion():
    while True:
        opcion = ingresar_ne("una opción")
        if opcion >= 1 and opcion <= 5:
            return opcion
        print("Error: Opción inválida. Escriba de nuevo.")
        print("======================================================================")


def mostrar_menu():
    print("================================ MENÚ ================================")
    print("1. Añadir/Modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    print("======================================================================")


def add_contacto(agenda: Dict[str, str], nombre_contacto: str):
    # PASO. Ingresar número del nuevo contacto
    while True:
        print("Contacto no encontrado. ¿Desea añadir su número? (1: Si, 0: No)")
        opcion_add = ingresar_ne("la opción")
        if opcion_add != 1 and opcion_add != 0:
            continue
        elif opcion_add == 1:
            # PASO. Validación 9 caracteres
            while True:
                numero_telefono = ingresar_str("el número celular del nuevo contacto")
                if len(numero_telefono) != 9:
                    print("El número celular debe ser de 9 caractéres (Perú)")
                    continue
                else:
                    break
            agenda[nombre_contacto] = numero_telefono
            print(
                "======================================================================"
            )
            print("¡Contacto añadido satisfactoriamente!")
            input("Presione cualquier tecla para continuar")
            break
        elif opcion_add == 0:
            break


def modificar_contacto(agenda: Dict[str, str], nombre_contacto: str):
    # PASO. Mostrar teléfono del contacto
    print(f"El número celular de {nombre_contacto} es {agenda[nombre_contacto]}")
    # PASO. Mostrar opciones para modificar o salir al menú
    print("¿Desea modificar su número celular? (1: Si, 0: No)")
    opcion_add = ingresar_ne("la opción")
    while True:
        if opcion_add != 1 and opcion_add != 0:
            continue
        elif opcion_add == 1:
            # PASO. Validación 9 caracteres
            while True:
                numero_telefono = ingresar_str(
                    f"el nuevo número celular del contacto {nombre_contacto}"
                )
                if len(numero_telefono) != 9:
                    print("El número celular debe ser de 9 caractéres (Perú)")
                    continue
                else:
                    break
            agenda[nombre_contacto] = numero_telefono
            print(
                "======================================================================"
            )
            print("¡Contacto modificado correctamente!")
            input("Presione cualquier tecla para continuar")
            break
        elif opcion_add == 0:
            break


def agenda_add_modificar(agenda: Dict[str, str]):
    nombre_a_buscar = ingresar_str("el nombre a buscar en la agenda")
    if agenda.get(nombre_a_buscar) is None:
        add_contacto(agenda, nombre_a_buscar)
    else:
        modificar_contacto(agenda, nombre_a_buscar)


def agenda_buscar(agenda: Dict[str, str]):
    if len(agenda) == 0:
        print("La lista está vacía")
        print("======================================================================")
    else:
        caracteres_a_buscar = ingresar_str("el nombre a buscar en la agenda")
        contador_encontrados = 0
        for nombre, numero_telefono in agenda.items():
            if nombre.startswith(caracteres_a_buscar):
                contador_encontrados += 1
                print(nombre, numero_telefono, sep=" :: ")
        if contador_encontrados == 0:
            print(
                "No se ha encontrado ningún contacto que empiece con los caracteres buscados"
            )
    input("Presione cualquier tecla para continuar")
    return


def agenda_borrar(agenda: Dict[str, str]):
    if len(agenda) == 0:
        print("La lista está vacía")
        input("Presione cualquier tecla para continuar")
        return

    contacto_nombre_a_borrar = ingresar_str("nombre del contacto que desea eliminar")
    if agenda.get(contacto_nombre_a_borrar) is None:
        print("Contacto no encontrado. Vuelva a intentarlo")
        input("Presione cualquier tecla para continuar")
        return

    while True:
        print(
            f"¿Está seguro de eliminar el contacto {contacto_nombre_a_borrar}? (1: Si, 0: No)"
        )
        opcion_add = ingresar_ne("la opción")
        if opcion_add != 1 and opcion_add != 0:
            continue
        elif opcion_add == 1:
            del agenda[contacto_nombre_a_borrar]
            print(
                "======================================================================"
            )
            print("¡Contacto eliminado!")
            input("Presione cualquier tecla para continuar")
            break
        elif opcion_add == 0:
            break

    return


def agenda_listar(agenda: Dict[str, str]):
    if len(agenda) == 0:
        print("La lista está vacía")
        print("======================================================================")
    else:
        for nombre, numero_telefono in agenda.items():
            print(nombre, numero_telefono, sep=" :: ")
    input("Presione cualquier tecla para continuar")


def init():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = get_opcion()
        print("======================================================================")
        if opcion == 1:
            agenda_add_modificar(agenda)
        elif opcion == 2:
            agenda_buscar(agenda)
        elif opcion == 3:
            agenda_borrar(agenda)
        elif opcion == 4:
            agenda_listar(agenda)
        elif opcion == 5:
            break


init()
