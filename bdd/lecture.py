import psycopg2
import psycopg2.extras
import sys
import csv
import io


# Try to connect to an existing database
print('Connexion à la base de données...')
try:
   conn = psycopg2.connect("host=pgsql dbname=albah user=albah password=1234")
except Exception as e :
   exit("Connexion impossible à la base de données: " + str(e))

print('Connecté à la base de données')
#préparation de l'exécution des requêtes (à ne faire qu'une fois)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# #Table Region
csv_file = open('v_region_2023.csv', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'Region', sep=',', columns=('codeReg', 'libelle'))
csv_file.close()
conn.commit()

# #Table departement
csv_file = open('v_departement_2023.csv', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'Departement', sep=',', columns=('codeDep', 'codeReg', 'libelle'))
csv_file.close()
conn.commit()

# #Table commune
csv_file = open('v_commune_2023.csv', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'Commune', sep=',', null='', columns=('codeCom', 'codeDep', 'libelle'))
csv_file.close()
conn.commit()

# #Table ChefLieuRegion
csv_file = open('chefLieuReg.csv', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'ChefLieuRegion', sep=',', null='', columns=('codeReg', 'codeCom'))
csv_file.close()
conn.commit()

# #Table ChefLieuDepartement
csv_file = open('chefLieuDep.csv', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'ChefLieuDepartement', sep=',', null='', columns=('codeDep', 'codeCom'))
csv_file.close()
conn.commit()

# #Table StatCommuneAnnee
csv_file = open('stats/pop19.CSV', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'StatCommuneAnnee', sep=',', null='', columns=('id', 'annee', 'codeCom', 'valeur'))
csv_file.close()
conn.commit()

csv_file = open('stats/pop13.CSV', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'StatCommuneAnnee', sep=',', null='', columns=('id', 'annee', 'codeCom', 'valeur'))
csv_file.close()
conn.commit()

csv_file = open('stats/pop08.CSV', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'StatCommuneAnnee', sep=',', null='', columns=('id', 'annee', 'codeCom', 'valeur'))
csv_file.close()
conn.commit()

# #Table StatCommuneIntervalle
csv_file = open('stats/naiss0813.CSV', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'StatCommuneIntervalle', sep=',', null='', columns=('id', 'anneeDebut', 'anneeFin', 'codeCom', 'valeur'))
csv_file.close()
conn.commit()

csv_file = open('stats/naiss1319.CSV', 'r')
csv_reader = csv.reader(csv_file)
cur.copy_from(csv_file, 'StatCommuneIntervalle', sep=',', null='', columns=('id', 'anneeDebut', 'anneeFin', 'codeCom', 'valeur'))
csv_file.close()
conn.commit()

command = 'select * from region;'

try:
# Lancement de la requête
   cur.execute(command)
   cur.fetchall()
except Exception as e :
   #fermeture de la connexion
   cur.close()
   conn.close()
   exit("error when running: " + command + " : " + str(e))

cur.close()
conn.close()