from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Cliquez ici pour écrire...")

        # Connecter le signal `textEdited` à une méthode
        self.line_edit.textEdited.connect(self.on_text_edited)

        # Disposition
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def on_text_edited(self, text):
        print(f"Texte modifié : {text}")


app = QApplication([])
window = MyWindow()
window.show()
app.exec_()