import model


class user_session:

    def __init__(self,username):
        self.username = username
        self.name     = model.get_name(username)
        self.service  = model.get_service(username)
        self.id       = model.execute_select_query(f"select employe_id from employe WHERE nom ='{self.name}'")[0][0]
        self.grade    = model.get_grade(username)
        self.statut   = model.get_user_statut(username)
        self.nombre_absent = f"{model.get_absent_numb()}"
        self.nombre_present =f"{model.get_present_numb()}"
        self.nombre_demande =f"{model.get_demande_numb()}"
        self.nombre_super_valide = f"{model.get_super_validation_numb(self.name)}"
        self.validation_sup   = model.get_super_validation(self.name)
        self.request_signed   = model.get_request_signed()
        self.all_employe        = model.get_all_from_table("employe")
        self.all_users       = model.get_all_users()
        self.all_vacation    = model.get_all_vaction()
        self.all_vacation_request    = model.get_demandes_conge_en_cours()
        self.all_present   =  model.get_employes_non_en_conge()
        self.all_absent   =  model.get_employes_en_conge()
        self.notadmin    = model.get_admin()
        self.all_employe_name = model.get_employe_name()

    def makeadmin(self,usrname):
        return model.make_admin(usrname)

    def remove_admin(self,username):
        return model.remove_admin(username)

    def is_admin(self,username):
        return model.is_admin(username)
    def __str__(self):
        return f"""
    username : {self.username}
    statut   : {self.statut}
    nom      : {self.name}
    service  : {self.service} 
    grade    : {self.grade}
    nombre d'absent : {self.nombre_absent}
    nombre des presents : {self.nombre_present}
    nombre des demande : {self.nombre_demande}
"""




    def disconnect(self):
        self.conneted = model.connect()
        


