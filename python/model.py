import sqlite3

# define database 

connexion  =  sqlite3.connect("python.db")
cursor = connexion.cursor()

def getuser():
    cursor.execute('SELECT username , password FROM user;')
    return cursor.fetchall()

def is_user(username,password):
    users = getuser()
    if (username,password)  in users:
        return 1
    for user_ind in users:
        if username == user_ind[0] and not password == user_ind[1]:
            return-1
    return 0

def get_services():
    cursor.execute('''
    SELECT nom FROM SERVICE ;
''')
    ret = cursor.fetchall() 
    return([ i[0] for i in ret])


def is_empl_ind(id , nom , service):
    cursor.execute(
        """
    SELECT  e.id , e.nom , s.nom
    FROM  employe AS e  INNER JOIN SERVICE AS s
    ON e.service = e.id ;
"""
    )
    res = cursor.fetchall()
    for r in res :
        if r == (id , nom , service):
            return True
    return False

def get_user_ind(id,name,service):
    cursor.execute(f'select * from employe where id = {id}')
    employe = cursor.fetchall()
    cursor.execute(f'select nom from employe ; ')
    res = cursor.fetchall()
    cursor.execute(f'select username , password from user ; ')
    users = cursor.fetchall()
    if (name + str(id) ,"cg-"+name[:2] + str(service[:2])) in users:
        return [True , name + str(id) ,"cg-"+name[:2] + str(service[:2]) ]
        
    else :
        if employe and name :    
            try :
                cursor.execute(f" INSERT INTO user (id,username , password , employe)  VALUES ( ?,?,?,?)",(id,name + str(id) ,"cg-"+name[:2]+service[:2] ,id))
                connexion.commit()
                return [True , name + str(id) ,"cg-"+name[:2] + str(service[:2])  ]
            except  :
                return [True , '','']



def get_user_info(username):
    return '''
    cet utilisateur n'as pas de nom ni des iisqsi
    ccxcxcxcxcx*cx
    cxcccxcxcx
    cxc
    cx
    cx
    cxc
    x
    cx
    cx
    c
    xc
    xc
    xc
    xc
    xc
    xc
    x
    cx
    cx
    c
    xc
    x
    ccx
    c
    xc
    xc
    x
    c
    xc
    xc
    x
    c

    c
    x
    cx
    c
    xc
    xc
    c
    x
'''

# get_services()
# cursor.execute("""
# SELECT * 
# FROM user 
# INNER JOIN employe ON user.employe = employe.id;
# """)
# print(cursor.fetchall())



    

# connexion.close()