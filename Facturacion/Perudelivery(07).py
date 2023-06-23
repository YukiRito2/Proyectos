from tkinter import *


class FacturacionElectronica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Facturación Electrónica")
        self.ventana.config(bg="#F5F5F5")

        # Variables de control
        self.items = []
        self.subtotales = []

        # Etiquetas
        etiqueta_producto = Label(
            ventana,
            text="Producto:",
            bg="#F5F5F5",
            fg="#333333",
            font=("Arial", 12, "bold"),
        )
        etiqueta_producto.grid(row=0, column=0, padx=10, pady=10)

        etiqueta_cantidad = Label(
            ventana,
            text="Cantidad:",
            bg="#F5F5F5",
            fg="#333333",
            font=("Arial", 12, "bold"),
        )
        etiqueta_cantidad.grid(row=0, column=1, padx=10, pady=10)

        etiqueta_precio = Label(
            ventana,
            text="Precio:",
            bg="#F5F5F5",
            fg="#333333",
            font=("Arial", 12, "bold"),
        )
        etiqueta_precio.grid(row=0, column=2, padx=10, pady=10)

        etiqueta_subtotal = Label(
            ventana,
            text="Subtotal:",
            bg="#F5F5F5",
            fg="#333333",
            font=("Arial", 12, "bold"),
        )
        etiqueta_subtotal.grid(row=0, column=3, padx=10, pady=10)

        etiqueta_igv = Label(
            ventana,
            text="IGV Total:",
            bg="#F5F5F5",
            fg="#333333",
            font=("Arial", 12, "bold"),
        )
        etiqueta_igv.grid(row=0, column=4, padx=10, pady=10)

        # Entradas
        self.entradas_productos = []
        self.entradas_cantidad = []
        self.entradas_precios = []
        self.entradas_subtotales = []
        self.entradas_igv = []

        for i in range(10):
            entrada_producto = Entry(
                ventana, bg="#FFFFFF", fg="#333333", font=("Arial", 12)
            )
            entrada_producto.grid(row=i + 1, column=0, padx=10, pady=5)
            self.entradas_productos.append(entrada_producto)

            entrada_cantidad = Entry(
                ventana, bg="#FFFFFF", fg="#333333", font=("Arial", 12)
            )
            entrada_cantidad.grid(row=i + 1, column=1, padx=10, pady=5)
            self.entradas_cantidad.append(entrada_cantidad)

            entrada_precio = Entry(
                ventana, bg="#FFFFFF", fg="#333333", font=("Arial", 12)
            )
            entrada_precio.grid(row=i + 1, column=2, padx=10, pady=5)
            self.entradas_precios.append(entrada_precio)

            entrada_subtotal = Entry(
                ventana,
                state="readonly",
                bg="#F5F5F5",
                fg="#333333",
                font=("Arial", 12),
            )
            entrada_subtotal.grid(row=i + 1, column=3, padx=10, pady=5)
            self.entradas_subtotales.append(entrada_subtotal)

            entrada_igv = Entry(
                ventana,
                state="readonly",
                bg="#F5F5F5",
                fg="#333333",
                font=("Arial", 12),
            )
            entrada_igv.grid(row=i + 1, column=4, padx=10, pady=5)
            self.entradas_igv.append(entrada_igv)

            # Asociar eventos de actualización a las entradas de cantidad y precio
            entrada_cantidad.bind("<KeyRelease>", self.actualizar_subtotal)
            entrada_precio.bind("<KeyRelease>", self.actualizar_subtotal)

        # Botones
        boton_calcular = Button(
            ventana,
            text="Calcular",
            command=self.calcular_total,
            bg="#4CAF50",
            fg="#FFFFFF",
            font=("Arial", 14, "bold"),
        )
        boton_calcular.grid(row=11, column=0, columnspan=5, padx=10, pady=10)

        boton_limpiar = Button(
            ventana,
            text="Limpiar",
            command=self.limpiar_datos,
            bg="#FF0000",
            fg="#FFFFFF",
            font=("Arial", 14, "bold"),
        )
        boton_limpiar.grid(row=12, column=0, columnspan=5, padx=10, pady=10)

        # Etiqueta de total y IGV total
        self.etiqueta_total = Label(
            ventana,
            text="Total: S/.0",
            bg="#F5F5F5",
            fg="#333333",
            font=("Arial", 16, "bold"),
        )
        self.etiqueta_total.grid(row=13, column=0, columnspan=5, padx=10, pady=10)

        self.etiqueta_igv_total = Label(
            ventana,
            text="IGV Total: S/.0",
            bg="#F5F5F5",
            fg="#333333",
            font=("Arial", 16, "bold"),
        )
        self.etiqueta_igv_total.grid(row=14, column=0, columnspan=5, padx=10, pady=10)

    def calcular_total(self):
        total = 0
        total_igv = 0

        # Actualizar los subtotales antes de realizar los cálculos
        self.actualizar_subtotal(
            event=None
        )  # Llamada vacía para actualizar todas las entradas

        for i in range(len(self.entradas_productos)):
            producto = self.entradas_productos[i].get()
            cantidad_str = self.entradas_cantidad[i].get()
            precio_str = self.entradas_precios[i].get()

            try:
                cantidad = int(cantidad_str)
            except ValueError:
                cantidad = 0

            try:
                precio = float(precio_str)
            except ValueError:
                precio = 0.0

            subtotal = self.calcular_subtotal(cantidad, precio)
            igv = subtotal * 0.18  # IGV del 18%
            total += subtotal
            total_igv += igv

            self.subtotales.append(subtotal)
            self.items.append((producto, cantidad, precio, subtotal))

            # Actualizar entrada de subtotal
            self.entradas_subtotales[i].config(state="normal")
            self.entradas_subtotales[i].delete(0, END)
            self.entradas_subtotales[i].insert(0, str(subtotal))
            self.entradas_subtotales[i].config(state="readonly")

            # Actualizar entrada de IGV
            self.entradas_igv[i].config(state="normal")
            self.entradas_igv[i].delete(0, END)
            self.entradas_igv[i].insert(0, str(round(igv, 2)))
            self.entradas_igv[i].config(state="readonly")

        # Actualizar etiquetas de total y IGV total
        self.etiqueta_total.config(text=f"Total: S/.{total:.2f}")
        self.etiqueta_igv_total.config(text=f"IGV Total: S/.{total_igv:.2f}")

    def calcular_subtotal(self, cantidad, precio):
        subtotal = cantidad * precio
        return subtotal

    def actualizar_subtotal(self, event):
        # Obtener el índice de la entrada que desencadenó el evento
        widget_actual = self.ventana.focus_get()
        if (
            widget_actual not in self.entradas_cantidad
            and widget_actual not in self.entradas_precios
        ):
            return  # Salir si el widget actual no es una entrada de cantidad o precio

        index = None
        for i in range(len(self.entradas_cantidad)):
            if (
                widget_actual is self.entradas_cantidad[i]
                or widget_actual is self.entradas_precios[i]
            ):
                index = i
                break

        if index is None:
            return  # Salir si no se encuentra el índice

        # Obtener los valores de cantidad y precio correspondientes al índice
        cantidad_str = self.entradas_cantidad[index].get()
        precio_str = self.entradas_precios[index].get()

        try:
            cantidad = int(cantidad_str)
        except ValueError:
            cantidad = 0

        try:
            precio = float(precio_str)
        except ValueError:
            precio = 0.0

        subtotal = self.calcular_subtotal(cantidad, precio)

        # Actualizar entrada de subtotal
        self.entradas_subtotales[index].config(state="normal")
        self.entradas_subtotales[index].delete(0, END)
        self.entradas_subtotales[index].insert(0, str(subtotal))
        self.entradas_subtotales[index].config(state="readonly")

        # Actualizar entrada de IGV
        igv = subtotal * 0.18  # IGV del 18%
        self.entradas_igv[index].config(state="normal")
        self.entradas_igv[index].delete(0, END)
        self.entradas_igv[index].insert(0, str(round(igv, 2)))
        self.entradas_igv[index].config(state="readonly")

    def limpiar_datos(self):
        for entrada_producto in self.entradas_productos:
            entrada_producto.delete(0, END)

        for entrada_cantidad in self.entradas_cantidad:
            entrada_cantidad.delete(0, END)

        for entrada_precio in self.entradas_precios:
            entrada_precio.delete(0, END)

        for entrada_subtotal in self.entradas_subtotales:
            entrada_subtotal.config(state="normal")
            entrada_subtotal.delete(0, END)
            entrada_subtotal.config(state="readonly")

        for entrada_igv in self.entradas_igv:
            entrada_igv.config(state="normal")
            entrada_igv.delete(0, END)
            entrada_igv.config(state="readonly")

        self.etiqueta_total.config(text="Total: S/.0")
        self.etiqueta_igv_total.config(text="IGV Total: S/.0")


# Crear la ventana principal
ventana_principal = Tk()

# Crear una instancia de la interfaz de facturación electrónica
facturacion = FacturacionElectronica(ventana_principal)

# Ejecutar el bucle principal de la ventana
ventana_principal.mainloop()
