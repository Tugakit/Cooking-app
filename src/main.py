#import mysql.connector
from Etapes import Etapes
from Ingredients import Ingredients
from Mesures import Mesures
from Nom_Types import Nom_Types
from Recettes import Recettes
from Types_Recettes import Types_Recettes

#mydb = mysql.connector.connect(
#    host="10.0.0.5",
#    user="recette",
#    password="R3c3tt3s_m1xt3",
#    database="Recettes"
#)
#mycursor = mydb.cursor()
#mycursor.execute("SHOW TABLES")
#myresult = mycursor.fetchmany(3)
#for x in myresult:
 # print(x)

r1 = Recettes(1,"Riz Nature",10 )
print (r1.nom, r1.prepa)