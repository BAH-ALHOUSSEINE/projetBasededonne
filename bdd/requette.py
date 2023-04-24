import psycopg2
import sys
import csv
import io
import sqlite3
import psycopg2

print('Connexion à la base de données...')
try:
   conn = psycopg2.connect("host=pgsql dbname=albah user=albah password=1234")
except Exception as e :
   exit("Connexion impossible à la base de données: " + str(e))

print('Connecté à la base de données')



def get_departements_by_region(region_code):
    # Connexion à la base de données
    cur = conn.cursor()

    # Requête pour récupérer les départements de la région donnée
    query = "SELECT code, libelle FROM Departement WHERE region = ?"
    cur.execute(query, (region_code,))

    # Récupération des résultats
    departements = cur.fetchall()

    # Fermeture de la connexion et retour des résultats
    cur.close()
    conn.close()

    return departements;

def list_communes_plus_de_x_habitants(departement, x):
    # Connexion à la base de données

    # Création d'un curseur pour exécuter les requêtes
    cur = conn.cursor()
    # Exécution de la requête SQL
    cur.execute("SELECT c.code, c.libelle, s.habitants FROM Commune c INNER JOIN StatCommuneAnnee s ON c.code = s.codeCommune WHERE c.departement = ? AND s.habitants > ?", (departement, x))
    # Récupération des résultats
    resultats = cur.fetchall()
    # Fermeture de la connexion
    conn.close()
    # Retourne les résultats
    return resultats;


   

def select_top_communes(code_departement, n):
    # Connexion à la base de données
    cursor = conn.cursor()
    
    # Requête SQL pour sélectionner les communes du département et leur population
    query = """
        SELECT Commune.code, Commune.libelle, SUM(StatCommuneAnnee.habitants) as population
        FROM Commune
        INNER JOIN StatCommuneAnnee ON Commune.code = StatCommuneAnnee.codeCommune
        WHERE Commune.departement = ?
        GROUP BY Commune.code
        ORDER BY population DESC
        LIMIT ?
    """
    
    # Exécution de la requête avec les paramètres
    cursor.execute(query, (code_departement, n))
    
    # Récupération des résultats
    results = cursor.fetchall()
    
    # Fermeture de la connexion
    conn.close()
    
    # Retourne la liste des n communes les plus peuplées
    return results



resultats = get_departements_by_region("01")
print(resultats)












