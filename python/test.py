import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton 
import test2

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200) # Create a button to open the second window 
        self.button = QPushButton("Open Second Window", self)
        self.button.setGeometry(50, 50, 200, 50) 
        self.button.clicked.connect(self.open_second_window) 
    def open_second_window(self): 
        self.second_window = test2.SecondWindow()
        self.second_window.show() 


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())