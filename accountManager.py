#Manages the account info tables in the db
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



''' 
1. authenticate: authenticate credentials
2. register: make sure username not used
'''

#authenticate user returns true if authentication worked

def authenticate(user,password):

    f="sqlite3 database.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()  #facilitate db ops  <-- I don't really know what that means but ok
    isLogin = False #Default to false; login info correct?
    loginStatusMessage = "" #what's wrong
    messageNumber = 0 #represents what kind of error it is
    makeTable = 'IF NOT EXISTS CREATE TABLE users(username text, password text)'
    c.execute(makeTable)
    db.commit()
    checkUser = 'SELECT * FROM users WHERE username=="%s";' % (user)  #checks if the user is in the database
    c.execute(checkUser)
    l = c.fetchone() #listifies the results
    if l == None:
        isLogin = False
        messageNumber = 0
        loginStatusMessage = "user does not exist"
    elif l[1] == passHash:
        isLogin = True
        messageNumber = 1
        loginStatusMessage = "login info correct"
    else:
        isLogin = False
        messageNumber = 2
        loginStatusMessage = "wrong password"

    db.commit() #save changes
    db.close()  #close database
    return messageNumber

#returns true if register worked
def register(user,password,pwd):    #user-username, password-password, pwd-retype
    f="sqlite3 database.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()  #facilitate db ops  <-- I don't really know what that means but ok
    makeTable = 'IF NOT EXISTS CREATE TABLE users(username text, password text)'
    isRegister = False #defualt not work
    registerStatus = ""
    messageNumber = 0 #for message


    checkUser = 'SELECT * FROM users WHERE username=="%s";' % (user)  #checks if the user is in the database
    c.execute(checkUser)
    l = c.fetchone() #listifies the results

    if l != None:
        isRegister = False
        messageNumber = 0
        registerStatus = "username taken"
    elif (len(password) < 8 or len(pwd) < 8 ):
        isRegister = False
        messageNumber = 3 #two is already used below :/
        registerStatus = "password too short"
    elif (password != pwd):
        isRegister = False
        messageNumber = 1
        registerStatus = "passwords do not match"
    elif (password == pwd):
        insertUser = 'INSERT INTO users VALUES ("%s","%s");' % (user,password) #sqlite code for inserting new user

        c.execute(insertUser)

        isRegister = True
        messageNumber = 2
        registerStatus = "user %s registered!" % (user)

    db.commit() #save changes
    db.close()  #close database
    return messageNumber

register("bayle","bss","bss")
