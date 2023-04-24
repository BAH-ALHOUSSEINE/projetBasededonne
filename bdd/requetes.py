import psycopg2
import psycopg2.extras
import sys
import csv
import io


# Try to connect to an existing database
print('Connexion à la base de données...')
try:
   conn = psycopg2.connect("host=pgsql dbname=melbertrand user=melbertrand password=melvin12")
except Exception as e :
   exit("Connexion impossible à la base de données: " + str(e))

print('Connecté à la base de données')
#préparation de l'exécution des requêtes (à ne faire qu'une fois)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)



cur.close()
conn.close()