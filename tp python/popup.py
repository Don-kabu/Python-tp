import views.error      as v_err
from PyQt5 import QtCore, QtGui, QtWidgets



class error(QtWidgets.QMainWindow):
    def __init__(self ,message,er =True):
        super(error,self).__init__()
        self.ui = v_err.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.info.setText(message)
        if  not er : 
            self.ui.info.setStyleSheet("color: green;")
            self.ui.label.setPixmap(QtGui.QPixmap(":/ok/icons/circle-check.svg"))
        self.ui.btn_ok.clicked.connect(self.close)