import pandas
import numpy as np
from utils.utils import ingresar_str, ingresar_nn, ingresar_ne
import matplotlib.pyplot as plt


class Estudiante:
    def __init__(self, nombre: str, lista_notas: list[float]):
        self.nombre = nombre
        self.lista_notas = lista_notas

    def calcularPromedio(self) -> float:
        return np.mean(self.lista_notas)

    def detectarNotaMaxima(self) -> float:
        if len(self.lista_notas) == 0:
            return 0.0
        return np.max(self.lista_notas)

    def detectarNotaMinima(self) -> float:
        if len(self.lista_notas) == 0:
            raise ValueError("La lista de notas está vacía.")
        return np.min(self.lista_notas)

    def mostrarNotas(self):
        if len(self.lista_notas) == 0:
            raise ValueError("La lista de notas está vacía.")
        try:
            plt.hist(
                self.lista_notas,
                bins=np.arange(0, 22) - 0.5,
                edgecolor="black",
                alpha=0.7,
            )
            plt.xticks(range(0, 21))
            plt.title(f"Histograma de notas de {self.nombre}")
            plt.xlabel("Notas")
            plt.ylabel("Frecuencia")
            plt.grid(axis="y", alpha=0.3)
            plt.show()
        except Exception as e:
            print(f"Error al mostrar el histograma: {e}")


class Curso:
    def __init__(self, lista_estudiantes):
        self.lista_estudiantes = lista_estudiantes

    def exportarEstudiantes(self):
        # dataframe de pandas
        if self.lista_estudiantes is None or len(self.lista_estudiantes) == 0:
            return pandas.DataFrame({})

        data = {
            "nombre": [estudiante.nombre for estudiante in self.lista_estudiantes],
            "promedio": [
                estudiante.calcularPromedio() for estudiante in self.lista_estudiantes
            ],
        }
        df = pandas.DataFrame(data)
        return df

    def mostrarHistograma(self, df: pandas.DataFrame):
        if len(df) == 0:
            raise ValueError("El DataFrame está vacío.")

        plt.hist(
            df["promedio"], bins=np.arange(0, 22) - 0.5, edgecolor="black", alpha=0.7
        )
        plt.xticks(np.arange(0, 21))
        plt.title("Histograma de promedios de estudiantes")
        plt.xlabel("Promedio")
        plt.ylabel("Frecuencia")
        plt.grid(axis="y", alpha=0.3)
        plt.show()


try:
    while True:
        cantidad_estudiantes = ingresar_ne("la cantidad de estudiantes")
        if cantidad_estudiantes >= 0:
            break
        else:
            print("Error: La cantidad de estudiantes no puede ser negativa.")
    lista_estudiantes = []
    for i in range(cantidad_estudiantes):
        nombre = ingresar_str(f"el nombre del estudiante {i + 1}")
        while True:
            cantidad_notas = ingresar_ne(f"la cantidad de notas del estudiante {i + 1}")
            if cantidad_notas >= 0:
                break
            else:
                print("Error: La cantidad de notas no puede ser negativa.")
        notas = []
        for j in range(cantidad_notas):
            while True:
                nota = ingresar_nn(f"la nota {j + 1} del estudiante {i + 1}")
                if nota <= 20:
                    break
                else:
                    print("Error: La nota no puede ser mayor a 20.")
            notas.append(nota)
        estudiante = Estudiante(nombre, notas)
        lista_estudiantes.append(estudiante)

    curso = Curso(lista_estudiantes)
    df_estudiantes = curso.exportarEstudiantes()
    print(df_estudiantes)

    # curso.mostrarHistograma({})

    curso.mostrarHistograma(df_estudiantes)
except Exception as e:
    print(f"Error inesperado: {e}")
