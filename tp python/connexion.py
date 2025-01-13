import model
from PyQt5 import QtCore, QtGui, QtWidgets
from  popup import error
import views.connexion  as v_conn
import views.gen        as v_gen
import views.getcon     as v_get
import user , admin




class gen(QtWidgets.QMainWindow):
    def __init__(self , username="", password = ""):
        super(gen,self).__init__()
        self.ui = v_gen.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loginbutton.clicked.connect(self.loginlink)
        self.ui.username.setText(username)
        self.ui.password.setText(password)
    

    def loginlink(self):
        self.close()
        self.windo = login()
        self.windo.show()





class login(QtWidgets.QMainWindow):
    def __init__(self):
        super(login,self).__init__()
        self.ui = v_conn.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bt_login.clicked.connect(self.login)
        self.ui.signinbutton.clicked.connect(self.signin_link)

    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        if username.strip() == "" and password =="":
            self.pop = error('viellez remplir tous les  champs')
            self.pop.show()
        elif username.strip() == "" and not password =="":    
            self.pop = error(" le nom d'utilisateur est vide ")
            self.pop.show()
        elif not username.strip() == "" and  password =="":    
            self.pop = error(" le mot de pass n'est pas rempli")
            self.pop.show()
        else :
            r = model.get_connexion(username ,password)

            match r :
                case 0 :
                    self.pop = error('le identifiants ne sont pas correcte')
                case 1 :
                    self.pop = error(" connexion avec succes " ,False)
                    self.pop.ui.btn_ok.clicked.connect(self.main_link)
                case -1 :
                    self.pop = error("le mot de passe n'est pas coreect ")
                    self.ui.password.setText("")
            self.pop.show()
    
    def main_link(self ):
        if model.is_admin(self.ui.username.text()):
            self.wind = admin.Main(self.ui.username.text())
        else :
            self.wind = user.main(self.ui.username.text())
        self.wind.show()
        self.close()
        
    def signin_link(self):
        self.close()
        self.w = GetId()
        self.w.show()




class GetId(QtWidgets.QMainWindow):
    def __init__(self):
        super(GetId,self).__init__()
        self.ui = v_get.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loginbutton.clicked.connect(self.login_link)
        self.ui.generatebutton.clicked.connect(self.generate)
        self.ui.services.addItems([""]+[i[1] for i in model.get_all_from_table("service")])

    def generate(self):
        if self.ui.name.text().strip() == '' or self.ui.numerotravail.text() == ''  or  self.ui.services.currentText() == '':
            self.er = error("tous les champs sont obligatoires")
            self.er.show()
        else :
            nom = self.ui.name.text()
            id = self.ui.numerotravail.text()
            service = self.ui.services.currentText()
            print(model.is_employe(nom , id,service))
            r = model.is_employe(nom, id, service)
            if r :
                if model.is_user(nom , id):
                    e= model.get_con_id(nom)
                    self.gen = gen(e[0] , e[1])
                    self.gen.show()
                    self.close()
                else :
                    re = model.gen_id(nom ,id,service )
                    self.gen = gen(re[0] , re[1])
                    self.gen.show()
                    self.close()

            else : 
                self.e = error("""
vous n'etes pas reconnu comme employe 
si non vous n'etes pas enrregistrer
contacter votre le departement de gestion""")
                self.e.show()

    def login_link(self):
        self.close()
        self.w = login()
        self.w.show()










        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = login()

    MainWindow.show()
    sys.exit(app.exec_())
