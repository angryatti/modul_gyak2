from array import array
import random

rendabc = list(map(chr, range(ord('A'), ord('Z')+1)))
arrayofabc = list()

input("Random rendszám generátor v4:")
classice = int(input("Válaszon 1) klasszikus rendszám 2) Új rendszám"))
db = int(input("Hány darabot szeretne?"))

def negyvagy3(classice, db):
    abc = ""
    for j in range(db):
        if (classice==2):
            for i in range(4):
                valami = random.randrange(0,25)
                if (i==2):
                    abc+=" "
                abc = abc+rendabc[valami]
            valami = random.randrange(-1,999)+1
            abc = abc+"-"+str(valami).zfill(3)
            if abc not in arrayofabc:
                arrayofabc.append(abc)
            abc=""
        else:
            for i in range(3):
                valami = random.randrange(0,25)
                abc = abc+rendabc[valami]
            valami = random.randrange(-1,999)+1
            abc = abc+"-"+str(valami).zfill(3)
            if abc not in arrayofabc:
                arrayofabc.append(abc)
            abc=""            



# ennyi rendszámot generál
if (classice==1):
    negyvagy3(1,db)
else:
    negyvagy3(2,db)
    # 4-betű tartalmaz
   

# fájlba írás és a programban megjelenítés
with open('rendszamok.txt','w',encoding='utf-8') as kifile:
    for z in arrayofabc:
        print(z)
        kifile.write(z+'\n')
input("A fájlba írás megtörtént")

