import sqlie3

f="database.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()  #facilitate db ops  <-- I don't really know what that means but

def getLevel(userName):
    #code to get level that is saved in a db
