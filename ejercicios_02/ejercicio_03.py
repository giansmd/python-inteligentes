from utils.utils import ingresar_n, ingresar_str


lista_libros = []


def ingresar_titulo_libro():
    titulo_libro = ingresar_str("el título del libro")
    return titulo_libro


def ingresar_autor_libro():
    autor_libro = ingresar_str("el autor del libro")
    return autor_libro


def ingresar_anno_libro():
    anno_libro = ingresar_n("el año de publicación del libro")
    return anno_libro


def ingresar_libro():
    titulo_libro = ingresar_titulo_libro()
    autor_libro = ingresar_autor_libro()
    anno_libro = ingresar_anno_libro()
    return titulo_libro, autor_libro, anno_libro


def registrar_libros(cantidad: int):
    for i in range(cantidad):
        print(f"==================== LIBRO {i + 1} ====================")
        lista_libros.append(ingresar_libro())
        print("=================================================")


cantidad_libros = ingresar_n("la cantidad de libros a registrar")
registrar_libros(cantidad_libros)

# debug
# for libro in lista_libros:
#     print(libro)


lista_nueva_libros = []

for libro in lista_libros:
    if libro[2] > 2000:
        lista_nueva_libros.append(libro)

print("Libros publicados después del año 2000")
for libro in lista_nueva_libros:
    print(libro)
