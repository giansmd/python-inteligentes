import numpy as np
import numpy.random as nprand
import matplotlib.pyplot as plt
from utils.utils import ingresar_ne


class SimuladorDados:
    def __init__(self):
        self.resultados = []

    def lanzar_n_dados(self, num_dados):
        # array de numpy sirve para la optimización con grandes cantidades de datos
        self.resultados = np.array([nprand.randint(1, 7) for i in range(num_dados)])
        return self.resultados

    def calcularPromedio(self):
        if len(self.resultados) == 0:
            return 0
        return np.mean(self.resultados)

    def calcularVarianza(self):
        if len(self.resultados) == 0:
            return 0
        return np.var(self.resultados)

    def calcularDistribucion(self):
        if len(self.resultados) == 0:
            return 0
        normal = np.random.normal(
            self.calcularPromedio(), np.std(self.resultados), len(self.resultados)
        )
        return normal

    def graficarDistribucion(self):
        if len(self.resultados) == 0:
            return 0
        plt.hist(self.resultados, bins=np.arange(1, 8) - 0.5, alpha=0.6, color="g", rwidth=0.8)
        plt.xticks(np.arange(1, 7))
        plt.title("Distribución de resultados de dados")
        plt.xlabel("Valor del dado")
        plt.ylabel("Frecuencia")
        plt.show()


try:
    simulador = SimuladorDados()
    n_dados = ingresar_ne("la cantidad de dados a lanzar")
    if n_dados <= 0:
        raise ValueError("El número de dados debe ser un entero positivo.")
    simulador.lanzar_n_dados(n_dados)
    print(simulador.resultados)
    print(simulador.calcularPromedio())
    print(simulador.calcularVarianza())
    print(simulador.calcularDistribucion())
    simulador.graficarDistribucion()
except Exception as e:
    print(f"Error: {e}")
