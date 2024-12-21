import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QHBoxLayout

#from Main_ui import Ui_MainWindow                     # note Main_ui works nicely

#from Add_Customer import Ui_Add_Customer
class Ui_Add_Customer(object):
    def setupUi(self, Add_Customer):
        Add_Customer.setObjectName("Add_Customer")
        Add_Customer.resize(1134, 605)
        Add_Customer.setGeometry(350,175,1000,600)
        Add_Customer.setStyleSheet("*{background-color: rgb(47,47,47);\n"
"}\n"
"\n"
"QLineEdit{\n"
"\n"
"background: transparent;\n"
"border: none;\n"
"color:rgb(204, 204, 203);\n"
"border-bottom: 1px solid rgb(204, 204, 203);\n"
"font:32px;\n"
"}\n"
"\n"
"\n"
"#pb_save::Pressed{\n"
"background-color: rgb(34,34,34)\n"
"}\n"
"#pb_save{\n"
"border-radius:15px;\n"
"font: 32Pt \"Century Gothic\";\n"
"color: rgb(104,104,103);\n"
"background-color: rgb(17,17,17)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Add_Customer)
        self.centralwidget.setObjectName("centralwidget")
        self.LineName = QtWidgets.QLineEdit(self.centralwidget)
        self.LineName.setGeometry(QtCore.QRect(330, 60, 501, 51))
        self.LineName.setText("")
        self.LineName.setObjectName("LineName")
        self.pb_save = QtWidgets.QPushButton(self.centralwidget)
        self.pb_save.setGeometry(QtCore.QRect(320, 450, 531, 81))
        self.pb_save.setObjectName("pb_save")
        self.LineProduct = QtWidgets.QLineEdit(self.centralwidget)
        self.LineProduct.setGeometry(QtCore.QRect(330, 160, 501, 51))
        self.LineProduct.setText("")
        self.LineProduct.setObjectName("LineProduct")
        self.LinePrice = QtWidgets.QLineEdit(self.centralwidget)
        self.LinePrice.setGeometry(QtCore.QRect(330, 260, 501, 51))
        self.LinePrice.setText("")
        self.LinePrice.setObjectName("LinePrice")
        self.LineDate = QtWidgets.QLineEdit(self.centralwidget)
        self.LineDate.setGeometry(QtCore.QRect(330, 360, 501, 51))
        self.LineDate.setText("")
        self.LineDate.setObjectName("LineDate")
        Add_Customer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Add_Customer)
        self.statusbar.setObjectName("statusbar")
        Add_Customer.setStatusBar(self.statusbar)

        self.retranslateUi(Add_Customer)
        QtCore.QMetaObject.connectSlotsByName(Add_Customer)

    def retranslateUi(self, Add_Customer):
        _translate = QtCore.QCoreApplication.translate
        self.LineName.setPlaceholderText(_translate("Add_Customer", "Customer name"))
        self.pb_save.setText(_translate("Add_Customer", "save"))
        self.LineProduct.setPlaceholderText(_translate("Add_Customer", "Product"))
        self.LinePrice.setPlaceholderText(_translate("Add_Customer", "Price"))
        self.LineDate.setPlaceholderText(_translate("Add_Customer", "Date"))

# ++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class Add_Customer(QMainWindow, Ui_Add_Customer):
    def __init__(self, parent=None):
        super(Add_Customer, self).__init__(parent)
        
        self.setupUi(self)
        
        self.pb_save.clicked.connect(self.save_clicked)
        
    def save_clicked(self):
        print(f'class Add_Customer: def save_clicked(self):')
# ++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
#        self.Main_ui = Ui_MainWindow()
#        self.Main_ui.setupUi(self)

        self.pb_Add_Customer = QtWidgets.QPushButton('CREATE TABLE', self)  # +
        self.pb_Add_Customer.clicked.connect(self.add_Customer)             # +

#        self.events()
#    def events(self):
#        self.Main_ui.pb_Add_Customer.clicked.connect(self.Add_Customer)
#        self.pb_Add_Customer.clicked.connect(self.Add_Customer)

        self.window = Add_Customer(self)                                     # +
        
    def add_Customer(self):
#        self.window = QMainWindow()
#        self.musteri_win = Ui_Add_Customer()
#        self.musteri_win.setupUi(self.window)
         
        self.window.show()
        self.hide()                                                          # +
        
        sql = sqlite3.connect("customer_databasee.db")  #sqlite")
        curs = sql.cursor()
        curs.execute("""CREATE TABLE IF NOT EXISTS products
        (id integer primary key autoincrement, name, product, price, date)""")
        curs.execute("insert into products (name) values('Ahmet')")
        sql.commit()
        sql.close()

#    def close(self):
#        self.window.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())