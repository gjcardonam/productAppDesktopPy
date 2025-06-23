from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget
)
from db.database import add_product, get_all_products

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Productos")

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nombre del producto")

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Precio")

        self.add_button = QPushButton("Agregar producto")
        self.add_button.clicked.connect(self.save_product)

        self.product_list = QListWidget()

        self.layout.addWidget(QLabel("Crear producto"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(QLabel("Lista de productos"))
        self.layout.addWidget(self.product_list)

        self.setLayout(self.layout)
        self.load_products()

    def save_product(self):
        name = self.name_input.text()
        try:
            price = float(self.price_input.text())
            add_product(name, price)
            self.name_input.clear()
            self.price_input.clear()
            self.load_products()
        except ValueError:
            pass  # Puedes agregar un popup de error si quieres

    def load_products(self):
        self.product_list.clear()
        for id, name, price in get_all_products():
            self.product_list.addItem(f"{name} - ${price:.2f}")
