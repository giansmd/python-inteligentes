import numpy as np
from utils.utils import ingresar_str, ingresar_nn, ingresar_ne


class Estudiante:
    def __init__(self, nombre: str, lista_notas: list[float]):
        self.nombre = nombre
        self.lista_notas = lista_notas

    def calcularPromedio(self) -> float:
        if len(self.lista_notas) == 0:
            raise ValueError("La lista de notas está vacía.")
        return np.mean(self.lista_notas)

    def detectarNotaMaxima(self) -> float:
        if len(self.lista_notas) == 0:
            raise ValueError("La lista de notas está vacía.")
        return np.max(self.lista_notas)

    def detectarNotaMinima(self) -> float:
        if len(self.lista_notas) == 0:
            raise ValueError("La lista de notas está vacía.")
        return np.min(self.lista_notas)


if __name__ == "__main__":
    nombre_estudiante = ingresar_str("el nombre del estudiante")
    while True:
        cantidad_notas = ingresar_ne("la cantidad de notas")
        if cantidad_notas >= 0:
            break
        else:
            print("Error: La cantidad de notas no puede ser negativa.")
    notas = []
    for i in range(cantidad_notas):
        while True:
            nota = ingresar_nn(f"la nota {i + 1}")
            if nota <= 20:
                break
            else:
                print("Error: La nota debe estar entre 0 y 20.")
        notas.append(nota)
    estudiante = Estudiante(nombre_estudiante, notas)
    try:
        print(f"Nombre del estudiante: {estudiante.nombre}")
        print(f"Promedio de notas: {estudiante.calcularPromedio()}")
        print(f"Nota máxima: {estudiante.detectarNotaMaxima()}")
        print(f"Nota mínima: {estudiante.detectarNotaMinima()}")
    except ValueError as e:
        print(e)
