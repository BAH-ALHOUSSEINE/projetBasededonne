import psycopg2
import sys
import csv
import io
import sqlite3
import psycopg2

# print('Connexion à la base de données...')
# try:
#    conn = psycopg2.connect("host=pgsql dbname=albah user=albah password=1234")
# except Exception as e :
#    exit("Connexion impossible à la base de données: " + str(e))

print('Connexion à la base de données...')
try:
   conn = psycopg2.connect("host=pgsql dbname=melbertrand user=melbertrand password=melvin12")
except Exception as e :
   exit("Connexion impossible à la base de données: " + str(e))

print('Connecté à la base de données')



def get_departements_by_region(region_code):
    # Connexion à la base de données
    cur = conn.cursor()

    # Requête pour récupérer les départements de la région donnée
    query = "SELECT codeDep,libelle FROM Departement WHERE codeReg = %s"
    cur.execute(query, (region_code,))

    # Récupération des résultats
    departements = cur.fetchall()

    # Fermeture de la connexion et retour des résultats
    cur.close()
    conn.close()
    print ("codedept ,Libelle")
    for row in departements:
         print(row)
    

def list_communes_plus_de_x_habitants(departement, x):
    # Connexion à la base de données

    # Création d'un curseur pour exécuter les requêtes
    cur = conn.cursor()
    # Exécution de la requête SQL
    query="SELECT c.codeCom, c.libelle, s.valeur FROM Commune c INNER JOIN StatCommuneAnnee s ON c.code = s.codeCom WHERE c.codeDep = %s AND s.valeur > %s"
    cur.execute(query, (departement, x))
    # Récupération des résultats
    resultats = cur.fetchall()
    # Fermeture de la connexion
    conn.close()
    # Retourne les résultats
    print ("codedept ,Libelle,population")
    print("\n")
    for row in resultats:
        print(row)
        print("\n")


   

def select_top_communes(code_departement, n):
    # Connexion à la base de données
    cursor = conn.cursor()
    
    # Requête SQL pour sélectionner les communes du département et leur population
    query = """
        SELECT Commune.codeCom, Commune.libelle, SUM(StatCommuneAnnee.valeur) as population
        FROM Commune
        INNER JOIN StatCommuneAnnee ON Commune.codeCom = StatCommuneAnnee.codeCom
        WHERE Commune.codeDep = %s
        GROUP BY Commune.codeCom
        ORDER BY population DESC
        LIMIT %s
    """
    
    # Exécution de la requête avec les paramètres
    cursor.execute(query, (code_departement, n))
    
    # Récupération des résultats
    results = cursor.fetchall()
    
    # Fermeture de la connexion
    conn.close()
    
    # Retourne la liste des n communes les plus peuplées
    print ("codedept ,Libelle,population")
    for row in results:
        print(row)
        print("\n")



# resultats = get_departements_by_region("84")
print(select_top_communes("12", 10))














