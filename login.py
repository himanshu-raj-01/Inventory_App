from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from dashboard import Dashboard
import sqlite3

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operator Login")
        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        conn = sqlite3.connect("db/app.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM operators WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            self.dashboard = Dashboard()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
