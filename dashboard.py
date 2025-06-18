from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from forms.product_master import ProductMasterForm
from forms.goods_receiving import GoodsReceivingForm
from forms.sales_form import SalesForm

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        layout = QVBoxLayout()

        product_btn = QPushButton("Product Master")
        product_btn.clicked.connect(self.open_product_master)
        layout.addWidget(product_btn)

        receiving_btn = QPushButton("Goods Receiving")
        receiving_btn.clicked.connect(self.open_goods_receiving)
        layout.addWidget(receiving_btn)

        sales_btn = QPushButton("Sales Form")
        sales_btn.clicked.connect(self.open_sales_form)
        layout.addWidget(sales_btn)

        self.setLayout(layout)

    def open_product_master(self):
        self.pm = ProductMasterForm()
        self.pm.show()

    def open_goods_receiving(self):
        self.gr = GoodsReceivingForm()
        self.gr.show()

    def open_sales_form(self):
        self.sf = SalesForm()
        self.sf.show()
