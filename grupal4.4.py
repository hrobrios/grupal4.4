class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Bodega:
    def __init__(self, stock):
        self.stock = stock

    def descontar_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        else:
            return False


class Sucursal(Bodega):
    def __init__(self, stock):
        super().__init__(stock)
        self.bodega = Bodega(500)

    def reponer_stock(self, cantidad):
        if self.bodega.descontar_stock(cantidad):
            self.stock += cantidad
        else:
            print("No existe stock suficiente para reponer.")

    def solicitar_reposicion(self):
        if self.stock < 50:
            print("Se está solicitando y reponiendo productos.")
            self.reponer_stock(300)


class Vendedor:
    def __init__(self, sucursal):
        self.sucursal = sucursal

    def vender(self, producto, despacho):
        self.sucursal.solicitar_reposicion()

        precio_final = producto.precio
        if despacho:
            precio_final += 5000

        valor_neto = precio_final
        impuesto = valor_neto * 0.19
        valor_total = valor_neto + impuesto

        print("Valor neto: ", valor_neto)
        print("Impuesto: ", impuesto)
        print("Despacho: ", 5000 if despacho else 0)
        print("Valor total: ", valor_total)


# Ejemplo de uso
producto1 = Producto("Producto 1", 10000)
sucursal = Sucursal(30)
vendedor = Vendedor(sucursal)

vendedor.vender(producto1, True)
