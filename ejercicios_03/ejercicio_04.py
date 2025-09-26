import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils.utils import ingresar_nn, ingresar_str


class Tienda:
    def __init__(self):
        self.ventas = pd.DataFrame()

    def registrar_venta(self, producto: str, cantidad: int, precio_unitario: float):
        nueva_venta = pd.DataFrame(
            {
                "producto": [producto],
                "cantidad": [cantidad],
                "precio_unitario": [precio_unitario],
            }
        )
        if not nueva_venta.empty:
            self.ventas = pd.concat([self.ventas, nueva_venta], ignore_index=True)

    def calcularTotalVentas(self) -> float:
        if self.ventas.empty:
            return 0.0
        self.ventas["total"] = self.ventas["cantidad"] * self.ventas["precio_unitario"]
        return self.ventas["total"].sum()

    def calcularProductoMasVendido(self) -> str:
        if self.ventas.empty:
            return ""
        producto_mas_vendido = (
            self.ventas.groupby("producto")["cantidad"].sum().idxmax()
        )
        return producto_mas_vendido

    def calcularPromedioVentasPorTransaccion(self) -> float:
        if self.ventas.empty:
            return 0.0
        self.ventas["total"] = self.ventas["cantidad"] * self.ventas["precio_unitario"]
        return np.mean(self.ventas["total"])

    def mostrarVentasPorProducto(self):
        if self.ventas.empty:
            return
        ventas_por_producto = self.ventas.groupby("producto")["cantidad"].sum()
        ventas_por_producto.plot(kind="bar", color="red")
        plt.title("Ventas por Producto")
        plt.xlabel("Producto")
        plt.ylabel("Cantidad Vendida")
        plt.grid(axis="y", alpha=0.3)
        plt.show()


try:
    tienda = Tienda()
    cantidad_ventas = ingresar_nn("la cantidad de ventas a registrar")
    for i in range(cantidad_ventas):
        producto = ingresar_str(f"el nombre del producto {i}")
        cantidad = ingresar_nn(f"la cantidad vendida de {producto}")
        while True:
            precio_unitario = float(
                input(f"Ingrese el precio unitario de {producto}: ")
            )
            if precio_unitario < 0:
                print("El precio unitario no puede ser negativo. Intente de nuevo.")
            else:
                break
        tienda.registrar_venta(producto, cantidad, precio_unitario)
    print(tienda.ventas)
    print(f"TOTAL VENTAS: {tienda.calcularTotalVentas()}")
    print(f"PRODUCTO MÁS VENDIDO: {tienda.calcularProductoMasVendido()}")
    print(
        f"PROMEDIO VENTAS POR TRANSACCIÓN: {tienda.calcularPromedioVentasPorTransaccion()}"
    )
    tienda.mostrarVentasPorProducto()
except Exception as e:
    print(f"Error: {e}")
