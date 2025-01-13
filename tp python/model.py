import sqlite3
from sqlite3 import Error
import datetime

# Fonction pour créer une connexion SQLite
def connect_to_db(db_file="python.db"):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Erreur : {e}")
        return None

# Fonction pour exécuter une requête SQL (CREATE, INSERT, UPDATE, DELETE)
def execute_modify_query(query, params=None):
    conn = connect_to_db()
    try : 
        if conn:
            cursor = conn.cursor()
            cursor.execute(query, params or [])
            conn.commit()
            conn.close()
            return 1
    except sqlite3.IntegrityError :
        print("cette enregistrent exist deja ")

# Fonction pour exécuter une requête SQL SELECT
def execute_select_query(query, params=None):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        result = cursor.fetchall()
        conn.close()
        return result

# Création des tables SQLite
def init_database():
    queries = [
        """CREATE TABLE IF NOT EXISTS service (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_service TEXT NOT NULL,
            description TEXT
        )""",
        """CREATE TABLE IF NOT EXISTS grade (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_grade TEXT NOT NULL,
            niveau INTEGER NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS employe (
            employe_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            service_id INTEGER NOT NULL,
            grade_id INTEGER NOT NULL,
            date_embauche TEXT NOT NULL,
            etat TEXT NOT NULL DEFAULT 'present',
            FOREIGN KEY (service_id) REFERENCES service(service_id),
            FOREIGN KEY (grade_id) REFERENCES grade(grade_id)
        )""",
        """CREATE TABLE IF NOT EXISTS utilisateur (
            utilisateur_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employe_id INTEGER NOT NULL,
            username   TEXT not null UNIQUE,
            email TEXT NOT NULL UNIQUE,
            mot_de_passe TEXT NOT NULL,
            role TEXT DEFAULT 'employe',
            status TEXT DEFAULT false,
            date_creation TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employe_id) REFERENCES employe(employe_id)
            
        )""",
        """CREATE TABLE IF NOT EXISTS demande_de_conge (
            demande_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employe_id INTEGER NOT NULL,
            type_conge TEXT NOT NULL,
            date_debut TEXT NOT NULL,
            date_fin TEXT NOT NULL,
            statut TEXT DEFAULT 'en_attente',
            date_demande TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employe_id) REFERENCES employe(employe_id)
        )""",
        """CREATE TABLE IF NOT EXISTS validation (
            validation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            demande_id INTEGER NOT NULL,
            valide_par INTEGER NOT NULL,
            statut_validation TEXT NOT NULL,
            date_validation TEXT DEFAULT CURRENT_TIMESTAMP,
            commentaire TEXT,
            FOREIGN KEY (demande_id) REFERENCES demande_de_conge(demande_id),
            FOREIGN KEY (valide_par) REFERENCES utilisateur(utilisateur_id)
        )""",
        """CREATE TABLE IF NOT EXISTS conge (
            conge_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employe_id INTEGER NOT NULL,
            date_debut TEXT NOT NULL,
            date_fin TEXT NOT NULL,
            type_conge TEXT NOT NULL,
            FOREIGN KEY (employe_id) REFERENCES employe(employe_id)
        )"""
    ]

    for query in queries:
        execute_modify_query(query)

# Fonctions d'insertion
def insert_utilisateur(employe_id, username , email, mot_de_passe, role="employe"):
    query = """
    INSERT INTO utilisateur (employe_id, username, email, mot_de_passe, role)
    VALUES (?, ?, ?, ? , ?)
    """
    execute_modify_query(query, (employe_id,username, email, mot_de_passe, role))

def insert_employe(nom, prenom, service_id, grade_id, date_embauche):
    query = """
    INSERT INTO employe (nom, prenom, service_id, grade_id, date_embauche)
    VALUES (?, ?, ?, ?, ?)
    """
    execute_modify_query(query, (nom, prenom, service_id, grade_id, date_embauche))

def insert_demande_de_conge(employe_id, type_conge, date_debut, date_fin):
    query = """
    INSERT INTO demande_de_conge (employe_id, type_conge, date_debut, date_fin)
    VALUES (?, ?, ?, ?)
    """
    execute_modify_query(query, (employe_id, type_conge, date_debut, date_fin))



def insert_service(service_id, nomservice, description):
    query = """
    INSERT INTO service (service_id, nom_service, description)
    VALUES (?, ?, ?)
    """
    execute_modify_query(query, (service_id, nomservice, description))



def insert_validation(demande_id, valide_par, statut_validation, commentaire=None):
    query = """
    INSERT INTO validation (demande_id, valide_par, statut_validation, commentaire)
    VALUES (?, ?, ?, ?)
    """
    execute_modify_query(query, (demande_id, valide_par, statut_validation, commentaire))

def insert_conge(employe_id, date_debut, date_fin, type_conge):
    query = """
    INSERT INTO conge (employe_id, date_debut, date_fin, type_conge)
    VALUES (?, ?, ?, ?)
    """
    execute_modify_query(query, (employe_id, date_debut, date_fin, type_conge))

# Requêtes de visualisation
def get_all_from_table(table_name):
    query = f"SELECT * FROM {table_name}"
    return execute_select_query(query)

def get_employes_en_conge():
    query = """
    SELECT e.nom, e.prenom, c.date_debut, c.date_fin, c.type_conge
    FROM conge c
    JOIN employe e ON c.employe_id = e.employe_id
    """
    return execute_select_query(query)

def get_employes_non_en_conge():
    query = """
    SELECT e.nom, e.prenom
    FROM employe e
    WHERE e.employe_id NOT IN (SELECT employe_id FROM conge)
    """
    return execute_select_query(query)

def get_demandes_conge_en_cours():
    query = """
    SELECT d.demande_id, e.nom, e.prenom, d.type_conge, d.date_debut, d.date_fin, d.statut
    FROM demande_de_conge d
    JOIN employe e ON d.employe_id = e.employe_id
    WHERE d.statut = 'en_attente'
    """
    return execute_select_query(query)

def get_request_signed():
    query = """
    SELECT d.demande_id, e.nom, e.prenom, d.type_conge, d.date_debut, d.date_fin, d.statut
    FROM demande_de_conge d
    JOIN employe e ON d.employe_id = e.employe_id
    WHERE d.statut = 'valide'
    """
    return execute_select_query(query)

def get_connexion(username , password):
    query = f"""
    SELECT username , mot_de_passe 
    FROM  utilisateur

"""
    res = execute_select_query(query)


    if (username,password) in res:
        return 1
    elif username in [i[0] for i in res]:
        print("i")
        return -1
    else :
        return 0


def gen_id(nom , id ,service):
    all = execute_select_query(f"SELECT e.employe_id , e.nom , e.prenom ,s.nom_service , e.grade_id  FROM employe AS e INNER JOIN service AS s ON s.service_id = e.service_id  WHERE e.nom = '{nom}' and e.employe_id = {id}")[0]
    username = f"{all[1]}{all[0]}{all[2]}"
    password = f"{len(all[1])}{all[2][:5]}{all[3]}"
    insert_utilisateur( id , username , "" ,password)
    return (username ,password)

def get_con_id (name):
    
    query = f"""
    SELECT u.username , u.mot_de_passe 
    FROM  utilisateur AS u  INNER JOIN employe AS e
    ON u.employe_id = e.employe_id
    WHERE  e.nom = '{name}'

"""
    r = execute_select_query(query)
    return r[0]

def get_name (username):
    query = f"""
    SELECT e.nom
    FROM utilisateur AS u INNER JOIN employe AS e
    ON u.employe_id = e.employe_id
    where u.username = '{username}'
    """
    return execute_select_query(query)[0][0]

def get_employe_name():
    
    query = f"""
    SELECT nom
    FROM employe 
    """
    return [i [0] for i in execute_select_query(query)]

def get_service(username):
    query = f"""
    SELECT s.nom_service
    FROM utilisateur AS u INNER JOIN employe AS e 
    ON u.employe_id = e.employe_id   
    INNER JOIN  service AS s
    ON s.service_id = e.service_id   

    where u.username = '{username}'
    """
    return execute_select_query(query)[0][0]



def get_grade(username):
    query = f"""
    SELECT g.nom_grade
    FROM utilisateur AS u INNER JOIN employe AS e 
    ON u.employe_id = e.employe_id   
    INNER JOIN  grade AS g
    ON e.grade_id = g.grade_id   
    where u.username = '{username}'
    """
    return execute_select_query(query)[0][0]

def get_user_statut(username):
    query = f"""
    SELECT role
    FROM utilisateur 
    where username = '{username}'
    """
    return execute_select_query(query)[0][0]



def get_all_vaction():
    query = f"""
    SELECT  e.nom , c.type_conge ,c.date_debut, c.date_fin
    FROM conge as c
    INNER JOIN employe as e ON e.employe_id = c.employe_id
    """

    return execute_select_query(query)


def get_all_users():
    query = f"""
    SELECT u.username , e.nom , u.email ,u.role , u.date_creation
    FROM utilisateur as u
    INNER JOIN employe as e ON e.employe_id = u.employe_id
    """

    return execute_select_query(query)

def get_present_numb():
    query = f"""
    SELECT COUNT(*)
    FROM employe INNER JOIN conge 
    ON employe.employe_id =  conge.employe_id
    where (date_debut - date_fin ) > 0 
    """
    return execute_select_query(query)[0][0]



def get_absent_numb():
    query = f"""
    SELECT COUNT(*)
    FROM employe INNER JOIN conge 
    ON employe.employe_id =  conge.employe_id
    where (date_debut - date_fin ) <= 0 
    """
    return execute_select_query(query)[0][0]


def get_super_validation(name):
    query = f"""
    SELECT v.commentaire , c.nom,v.date_validation
    FROM validation as v INNER JOIN  demande_de_conge as d 
    on v.demande_id = d.demande_id
    INNER JOIN employe AS c ON e.employe_id  = v.valide_par
    INNER JOIN employe AS e ON e.employe_id  = d.employe_id

    WHERE e.nom  = '{name}'
"""
    # INNER JOIN employe AS c ON e.employe_id  = v.valide_par
    return execute_select_query(query)


def get_super_validation_numb(name):
    query = f"""
    SELECT COUNT(*)
    FROM validation as v INNER JOIN  demande_de_conge as d 
    on v.demande_id = d.demande_id
    INNER JOIN employe AS e on e.employe_id  = d.employe_id
    WHERE e.nom  = '{name}'
"""
    return execute_select_query(query)[0][0]

def get_demande_numb() : 
    query = f"""
    SELECT COUNT(*)
    FROM employe INNER JOIN conge 
    ON employe.employe_id =  conge.employe_id
    where (date_debut - date_fin ) <= 0 
    """
    return execute_select_query(query)[0][0]





def is_user(name , id) -> bool:
    query = f"""
    SELECT *
    FROM utilisateur as u  INNER JOIN employe as e
    ON u.employe_id = e.employe_id
    WHERE e.nom = '{name}' AND e.employe_id = {id}
"""
    r = execute_select_query(query) 
    print(r)  
    if r :
        return True
    return False


def is_employe(nom_emplo , id_emplo , nom_service):
    query = f"""
    SELECT *
    FROM employe AS e INNER JOIN service AS s 
    ON e.service_id = s.service_id
    WHERE e.nom = '{nom_emplo}' AND e.employe_id = '{id_emplo}'  AND s.nom_service = '{nom_service}'
"""
    r = execute_select_query(query)
    if r :
        return True
    return False




def is_admin(username):
    query = f"""
SELECT role
FROM  utilisateur
WHERE  username ='{username}'"""
    r =execute_select_query(query)[0][0]
    if r == "admin":
        return True
    return False




def get_admin():
    query = """
    select username
    from utilisateur 
      """

    return [i[0] for i in execute_select_query(query)]

def make_admin(username):

    query  = f"""
UPDATE utilisateur
SET role = 'admin'
WHERE username = '{username}'
"""
    execute_modify_query(query)


def remove_admin(username):

    query  = f"""
UPDATE utilisateur
SET role = 'employe'
WHERE username = '{username}'
"""
    execute_modify_query(query)


# Initialisation de la base de données

# init_database()

# insert_conge(1,'10/10/2024','12/12/2025','la casa de papel')
# insert_utilisateur(1, ' kabudon','kabu7don19@gmail.com','Python12@','admin')
# insert_employe('kabu dianzambi' , 'don' , 1,1,'22/01/2005')
# insert_service(1,'informatique' , 'lorem  ceci estle departement den l')
# insert_demande_de_conge(1,'maladie' , datetime.datetime.strftime(datetime.datetime.today(),"%Y / %m / %d") ,datetime.datetime.strftime(datetime.datetime.today(),"%Y / %m / %d"))

# print(get_name(" kabudon "))
# print(get_service(" kabudon "))
# print(get_present_numb())
# print(get_all_from_table('service'))
# print(is_user('kabu dianzambi' , 2))
# print(is_employe("kabu dianzambi" , 1,"informatique"))
print(make_admin("kabudon"))
print(get_admin())