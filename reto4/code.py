class ItemMenu:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        if precio < 0:
            raise ValueError("Precio inválido")
        self._precio = precio

    def calcular_precio(self):
        return self._precio


class Bebida(ItemMenu):
    def __init__(self, nombre, precio, tamano):
        super().__init__(nombre, precio)
        self._tamano = tamano

    def get_tamano(self):
        return self._tamano

    def set_tamano(self, tamano):
        self._tamano = tamano

    def calcular_precio(self):
        if self._tamano == "grande":
            return self._precio * 1.2
        return self._precio


class Entrada(ItemMenu):
    def __init__(self, nombre, precio, para_compartir):
        super().__init__(nombre, precio)
        self._para_compartir = para_compartir

    def get_para_compartir(self):
        return self._para_compartir

    def set_para_compartir(self, valor):
        self._para_compartir = valor

    def calcular_precio(self):
        if self._para_compartir:
            return self._precio * 1.1
        return self._precio


class PlatoPrincipal(ItemMenu):
    def __init__(self, nombre, precio, calorias):
        super().__init__(nombre, precio)
        self._calorias = calorias

    def get_calorias(self):
        return self._calorias

    def set_calorias(self, calorias):
        self._calorias = calorias


class Orden:
    def __init__(self):
        self._items = []

    def agregar_item(self, item):
        if not isinstance(item, ItemMenu):
            raise TypeError("Solo se permiten ItemMenu")
        self._items.append(item)

    def calcular_total(self):
        total = 0
        hay_principal = any(isinstance(i, PlatoPrincipal) for i in self._items)

        for item in self._items:
            precio = item.calcular_precio()

            if hay_principal and isinstance(item, Bebida):
                precio *= 0.8

            total += precio

        return total


class Pago:
    def pagar(self, monto):
        raise NotImplementedError


class Tarjeta(Pago):
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta")


class Efectivo(Pago):
    def pagar(self, monto):
        print(f"Pagando {monto} en efectivo")


if __name__ == "__main__":
    orden = Orden()

    orden.agregar_item(Bebida("Coca-Cola", 5.0, "grande"))
    orden.agregar_item(Entrada("Nachos", 8.0, True))
    orden.agregar_item(PlatoPrincipal("Hamburguesa", 15.0, 800))

    total = orden.calcular_total()
    print("Total:", total)

    metodo_pago = Tarjeta()
    metodo_pago.pagar(total)