
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from views import adminmainwind , adminask_for_vacation,adminnew ,adminnew_admin ,adminNewTypeOfVacation ,adminsee,adminew_service,adminaddemploye
from filter import user_session
from connexion import error
from user import new
import model




class AdminActions(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(AdminActions,self).__init__()
        self.ui = adminnew.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)


        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

        self.ui.ar_add_emp.mousePressEvent = lambda event :  self.add_employe_() if event.button() == Qt.LeftButton else None
        self.ui.ar_add_admin.mousePressEvent = lambda event :  self.add_admin() if event.button() == Qt.LeftButton else None
        self.ui.ar_add_cong.mousePressEvent = lambda event :  self.add_conge() if event.button() == Qt.LeftButton else None
        self.ui.ar_add_service.mousePressEvent = lambda event :  self.add_service() if event.button() == Qt.LeftButton else None
        self.ui.ar_ajouter_promotion.mousePressEvent = lambda event :  self.add_promotion() if event.button() == Qt.LeftButton else None
        self.ui.ar_new_demande.mousePressEvent = lambda event :  self.add_demande() if event.button() == Qt.LeftButton else None

    def add_employe_(self):
        self.close()
        self.wind = AddEmploye(self.user.username)
        self.wind.show()
        print("employe pressed")

    def add_promotion(self):
        self.err = error("ce service est indesponible pour l'instant ")
        self.err.show()
        print("promotion pressed")



    def add_demande(self):
        self.err = error("ce service est indesponible pour l'instant ")
        self.err.show()
        print("demande pressed")



    def add_service(self):
        self.wind = addservice(self.user.username)
        self.wind.show()
        self.close()
        pass

    def add_conge(self):
        self.wind = Add_conge(self.user.username)
        self.wind.show()
        self.close()
        print("conge pressed")


    def add_admin(self):
        self.wind = AddAdmin(self.user.username)
        self.wind.show()
        self.close()
        print("admin pressed")
        



    
    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()






class Main(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(Main,self).__init__()
        self.ui = adminmainwind.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)
        self.ui.nombre_de_demmandes.setText(self.user.nombre_demande)
        self.ui.nombre_de_present.setText(self.user.nombre_present)
        self.ui.nombre_des_absents.setText(self.user.nombre_absent)
        self.ui.nombre_de_demmandes.setText(self.user.nombre_demande)
        self.ui.nombre_de_present.setText(self.user.nombre_present)
        self.ui.nombre_des_absents.setText(self.user.nombre_absent)
        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

        self.ui.demandes.mousePressEvent 

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()











class AddEmploye(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(AddEmploye,self).__init__()
        self.ui = adminaddemploye.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        self.ui.delete_2.clicked.connect(self.reset)
        self.ui.addemployer.clicked.connect(self.add_employe)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)


    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()




    def reset(self):
        self.ui.nom.setText("")
        self.ui.postnom.setText("")
        self.ui.prenom.setText("")
        self.ui.adresse.setText("")
        self.ui.email.setText("")
        self.ui.numerotel.setText("")
        self.ui.grade.setText("")

    def add_employe(self):
        if self.verify() : 
            pass

    def verify(self):
        message = ""
        ret = False
        self.ui.nom
        if self.ui.postnom & self.ui.prenom & self.ui.adresse & self.ui.email & self.ui.numerotel & self.ui.grade : 
            message = " un de champ est vide"
            ret = False





class NewType(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(AddEmploye,self).__init__()
        self.ui = adminaddemploye.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()








class addservice(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(addservice,self).__init__()
        self.ui = adminew_service.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        self.ui.chief.addItems(self.user.all_employe_name)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)
        self.ui.delete_2.clicked.connect(self.reset)
        self.ui.addemployer.clicked.connect(self.add_service)

    def add_service(self):
        if self.ui.chief.currentText().strip() == "" or self.ui.description.toPlainText() == ""  or self.ui.nom_service == "" :
            self.err= error("verifiez la saisi \n tous les champs sont oblogatoires")
            self.err.show()
        else :
            pass

    def reset(self):
        # self.ui.chief.
        self.ui.description.setPlainText("")
        self.ui.nom_service.setText("")

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()










class AddAdmin(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(AddAdmin,self).__init__()
        self.ui = adminnew_admin.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)
        self.ui.comboBox.addItems([""] + self.user.notadmin)

        self.ui.addemployer.clicked.connect(self.ok)
        self.ui.delete_2.clicked.connect(self.remove)

    def ok(self):
        self.selected_empl = self.ui.comboBox.currentText()
        if self.selected_empl.strip() == "":
            self.er = error("veillez selectionner un employer")
            self.er.show()
        else : 
            if self.user.is_admin(self.selected_empl):
                self.er = error(f"{self.selected_empl} est deja un admin " )
                self.er.show()
            else :
                self.er = error(f"{self.selected_empl} est desormais admin " ,False)
                self.user.makeadmin(self.selected_empl)
                self.er.show()

    def remove(self):
        self.selected_empl = self.ui.comboBox.currentText()
        if self.selected_empl.strip() == "":
            self.er = error("veillez selectionner un employer")
            self.er.show()
        else : 
            if not self.user.is_admin(self.selected_empl):
                self.er = error(f"{self.selected_empl} n'est deja pas un  admin")
                self.user.remove_admin(self.selected_empl)
                self.er.show()
            else :
                self.er = error(f"{self.selected_empl} n'est plus admin" ,False)
                self.er.show()




    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()










class Add_conge(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(Add_conge,self).__init__()
        self.ui = adminask_for_vacation.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)


        self.ui.addemployer.clicked.connect(self.add_vacation)
        self.ui.delete_2.clicked.connect(self.reset)


    def add_vacation(self):
        date_d = self.ui.datefin.date()
        date_f = self.ui.datedebut.date()
        motif = self.ui.motif.text()
        label = self.ui.nom.text()
        description = self.ui.plainTextEdit.toPlainText()

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
        self.ui.nom.setText("")
        self.ui.motif.setText("")
        self.ui.plainTextEdit.setPlainText("")
        self.ui.datedebut.setDate(QtCore.QDate.currentDate())
        self.ui.datefin.setDate(QtCore.QDate.currentDate())


    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()










class see(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(see,self).__init__()
        self.ui = adminsee.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ch_data  = []
        self.ch_fields = []

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

        self.ui.bt_absents.clicked.connect(self.all_absents)
        self.ui.bt_pressents.clicked.connect(self.all_presents)
        self.ui.bt_allusers.clicked.connect(self.all_users)
        self.ui.bt_allasks.clicked.connect(self.all_ask)
        self.ui.bt_all_cvacations.clicked.connect(self.all_vacations)
        self.all_users()
        self.ui.lineEdit.textEdited.connect(self.on_text_edited)



    def on_text_edited(self):
        tex_ch = self.ui.lineEdit.text()
        tex_ch = str(tex_ch)
        _data  = []
        if tex_ch.strip() == "":
            self.ui.print_data(self.fields ,self.data)
        else :
                
            for i in self.data :
                s = False
                for j in i:
                    if tex_ch in j :
                        s = True
                if s :
                    _data.append(i)
                    s = False
            self.ui.print_data(self.fields , _data)




    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()


    def desable(self):

        buttons = [
            self.ui.bt_absents,
            self.ui.bt_all_cvacations,
            self.ui.bt_pressents,
            self.ui.bt_allasks,
            self.ui.bt_allusers,
        ]
        for b in buttons :
            b.setStyleSheet(
                "QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}"
            )

    def active(self ,button :QtWidgets.QPushButton):

          button.setStyleSheet(
                "QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(0,143,150);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(0,0,0,0);\n"

"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(0,143,150);\n"

"}")

    def all_users(self):
        self.desable()
        self.active(self.ui.bt_allusers)
        self.data = self.user.all_users
        self.ui.print_data(['username' , 'nom' , 'mail' ,'role' , 'date_creation'],self.user.all_users)
        self.fields = ['username' , 'nom' , 'mail' ,'role' , 'date_creation']

    def all_absents(self):
        self.desable()
        self.active(self.ui.bt_absents)
        self.data = self.user.all_absent
        self.ui.print_data(['nom', 'prenom', 'date_debut', 'date_fin', 'type_conge'],self.user.all_absent)
        self.fields = ['nom', 'prenom', 'date_debut', 'date_fin', 'type_conge']

    def all_presents(self):
        self.desable()
        self.active(self.ui.bt_pressents)
        self.data = self.user.all_present
        self.ui.print_data(['nom', 'prenom'],self.user.all_present)
        self.fields = ['nom', 'prenom']

    def all_vacations(self):
        self.desable()
        self.active(self.ui.bt_all_cvacations)
        self.data = self.user.all_vacation
        self.ui.print_data(['nom' , 'type_conge' ,'date_debut', 'date_fin'] ,  self.user.all_vacation)
        self.fields = ['nom' , 'type_conge' ,'date_debut', 'date_fin']



    def all_ask(self):
        self.desable()
        self.active(self.ui.bt_allasks)
        self.data = self.user.all_vacation_request
        self.ui.print_data(['demande_id','nom','prenom', 'type_conge', 'date_debut', 'date_fin', 'statut'],self.user.all_vacation_request)
        self.fields = ['demande_id','nom','prenom', 'type_conge', 'date_debut', 'date_fin', 'statut']










class Dash(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(Dash,self).__init__()
        self.ui = adminask_for_vacation.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = see("kabudon")


    MainWindow.show()
    sys.exit(app.exec_())