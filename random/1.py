# Mixin para logging
class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


# Mixin para validación
class ValidationMixin:
    def validate_not_empty(self, value, field_name):
        if not value:
            raise ValueError(f"{field_name} no puede estar vacío")
        
# Mixin para serialización
class JsonMixin:
    def to_dict(self):
        return self.__dict__


# Clase principal que usa los mixins
class User(LoggerMixin, ValidationMixin, JsonMixin):
    def __init__(self, name, email):
        self.validate_not_empty(name, "Nombre")
        self.validate_not_empty(email, "Email")

        self.name = name
        self.email = email

    def create(self):
        self.log(f"Usuario {self.name} creado")


# Otra clase que reutiliza los mismos mixins
class Product(LoggerMixin, ValidationMixin, JsonMixin):
    def __init__(self, name, price):
        self.validate_not_empty(name, "Nombre")

        if price <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        self.name = name
        self.price = price

    def register(self):
        self.log(f"Producto {self.name} registrado")


# Uso del programa
if __name__ == "__main__":
    user = User("Maicol", "maicol@email.com")
    user.create()
    print(user.to_dict())

    print("-----")

    product = Product("Laptop", 2500)
    product.register()
    print(product.to_dict())