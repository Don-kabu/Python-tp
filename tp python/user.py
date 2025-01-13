from views import userask , usermain, userwherisrequest 
from popup import error
from PyQt5 import QtCore, QtGui, QtWidgets
from filter import user_session
import model


class main(QtWidgets.QMainWindow):
    def __init__(self ,username):
        super(main,self).__init__()
        self.ui = usermain.Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user_session(username)

        self.ui.username_2.setText( self.user.username)
        self.ui.usertype_2.setText(self.user.statut)
        self.ui.nombre_de_demmandes.setText(self.user.nombre_demande)
        self.ui.nombre_de_present.setText(self.user.nombre_present)
        self.ui.nombre_des_absents.setText(self.user.nombre_absent)


        self.ui.bn_home.clicked.connect(self.home)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bt_suivi.clicked.connect(self.see)


       


    def home(self) : 
        self.link = main(self.user.username)
        self.close()
        self.link.show()
    
    def new(self):
        self.link = new(self.user.username)
        self.close()
        self.link.show()
    
    def see(self):
        self.link = see(self.user.username)
        self.close()
        self.link.show()



class see (QtWidgets.QMainWindow):
    def __init__(self ,username):
        super(see ,self).__init__()
        self.ui = userwherisrequest.Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user_session(username)
        
        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)
        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bt_suivi.clicked.connect(self.see)
        print(self.user.nombre_super_valide)
        if self.user.validation_sup :
            self.ui.tableWidget.setRowCount(len(self.user.validation_sup))
            for i in range(len(self.user.validation_sup)):
                for j in range(len(self.user.validation_sup[0])):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(self.user.validation_sup[i][j])
                    print( i,j,item)
                    self.ui.tableWidget.setItem(i, j, item)
        else :
            self.ui.tableWidget.setRowCount(0)
            self.ui.label.setText("no validation yet ")
    
    def new(self):
        self.link = new(self.user.username)
        self.close()
        self.link.show()
    
    def see(self):
        self.link = see(self.user.username)
        self.close()
        self.link.show()

    def home(self) : 
        self.link = main(self.user.username)
        self.close()
        self.link.show()


class new (QtWidgets.QMainWindow):
    def __init__(self ,username):
        super(new ,self).__init__()
        self.ui = userask.Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user_session(username)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)
        
        self.ui.description.setPlaceholderText("la description du conge ")

        self.ui.datedebut.setCalendarPopup(True)
        self.ui.datefin.setCalendarPopup(True)
        self.ui.bn_home_2.clicked.connect(self.home)
        self.ui.bt_new_2.clicked.connect(self.new)
        self.ui.bt_suivi_2.clicked.connect(self.see)

        self.ui.addemployer.clicked.connect(self.add_vacation)
        self.ui.delete_2.clicked.connect(self.reset)


    def add_vacation(self):
        date_d = self.ui.datefin.date()
        date_f = self.ui.datedebut.date()
        motif = self.ui.motif.text()
        label = self.ui.conge_label.text()
        description = self.ui.description.toPlainText()

        if description.strip() ==  ""  or motif.strip() == ""  or label.strip() == "" :
            self.e = error(" veillez remplir tous les champs ")
            self.e.show()
        else : 
            if date_d == date_f :
                self.e = error(" les date ne pevent pas etre egaux")
                self.e.show()
            elif date_d < QtCore.QDate.currentDate() or date_f < QtCore.QDate.currentDate():
                self.e = error("les date ne peuvent pas etre dans le passee ")
                self.e.show()
            else :
                model.insert_demande_de_conge(self.user.id ,description,date_d.toString("dd/MM/yyyy") ,date_f.toString("dd/MM/yyyy"))
                self.wind = error("l'enregistrement fait avec success  ! " ,False)
                self.wind.show()
                self.reset()


    def reset (self):
        self.ui.datefin
        self.ui.datedebut
        self.ui.conge_label.setText("")
        self.ui.motif.setText("")
        self.ui.description.setPlainText("")
        self.ui.datedebut.setDate(QtCore.QDate.currentDate())
        self.ui.datefin.setDate(QtCore.QDate.currentDate())




    def home(self) : 
        self.link = main(self.user.username)
        self.close()
        self.link.show()
    
    def new(self):
        self.link = new(self.user.username)
        self.close()
        self.link.show()
    
    def see(self):
        self.link = see(self.user.username)
        self.close()
        self.link.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = main("kabudon")

    MainWindow.show()
    sys.exit(app.exec_())
