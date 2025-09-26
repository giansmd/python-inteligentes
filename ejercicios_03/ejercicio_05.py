import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class Clima:
    def __init__(self):
        # lee a partir de un csv, datos diarios de temperatura y humedad (pandas)
        # formato: 2025-09-26,20,79% - fecha, temperatura, humedad
        self.datos_clima = pd.read_csv(
            "ejercicios_03/datos_clima.csv", names=["fecha", "temperatura", "humedad"]
        )
        if self.datos_clima.empty:
            raise ValueError(
                "El archivo de datos de clima está vacío o no se pudo leer."
            )

    def calcularTemperaturaMedia(self):
        # if len(self.datos_clima['temperatura']) == 0:
        #     raise ValueError("No hay datos de temperatura disponibles.")
        return np.mean(self.datos_clima["temperatura"])

    def calcularDesvEstTemperatura(self):
        return np.std(self.datos_clima["temperatura"])

    def detectarValoresAtipicos(self):
        # valores atípicos en temperatura usando el método del rango intercuartílico (IQR)
        Q1 = np.percentile(self.datos_clima["temperatura"], 25)
        Q3 = np.percentile(self.datos_clima["temperatura"], 75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = self.datos_clima[
            (self.datos_clima["temperatura"] < lower_bound)
            | (self.datos_clima["temperatura"] > upper_bound)
        ]
        if outliers.empty:
            return "No se encontraron valores atípicos."
        return outliers

    def graficarTemperaturasEnTiempo(self):
        plt.plot(
            pd.to_datetime(self.datos_clima["fecha"]), self.datos_clima["temperatura"]
        )

        # gca() devuelve los ejes actuales (x e y) a través del objeto Axes
        # set_major_locator() establece la ubicación de los ticks principales en el eje x
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))

        # cambiar rotación de las etiquetas del eje x
        plt.xticks(rotation=45)

        plt.xlabel("Fecha")
        plt.ylabel("Temperatura (°C)")
        plt.title("Temperaturas en el tiempo")
        plt.show()


try:
    clima = Clima()
    print(clima.datos_clima)
    print(f"-> Temperatura media: {clima.calcularTemperaturaMedia()} grados")
    print(
        f"-> Desviación estándar de la temperatura: {clima.calcularDesvEstTemperatura()}"
    )
    print("-> Valores atípicos en la temperatura:")
    print(clima.detectarValoresAtipicos())
    clima.graficarTemperaturasEnTiempo()
except Exception as e:
    print(f"Error: {e}")
