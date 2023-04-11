# Ouvrir le fichier CSV en mode lecture
with open('v_commune_2023.csv', 'r') as file:
    # Lire toutes les lignes du fichier
    lines = file.readlines()

# Créer une liste pour stocker les nouvelles lignes
new_lines = []

# Parcourir toutes les lignes du fichier
for line in lines:
    # Séparer la ligne en valeurs de colonnes en utilisant la virgule comme séparateur
    columns = line.strip().split(',')
    # Vérifier si la valeur dans la colonne spécifiée est différente de la valeur à supprimer
    if columns[1] != '':
        # Si oui, ajouter la ligne à la liste des nouvelles lignes
        new_lines.append(line)

# Écrire les nouvelles lignes dans un nouveau fichier CSV
with open('v_commune_2023.csv', 'w') as new_file:
    # Écrire les nouvelles lignes dans le fichier
    new_file.writelines(new_lines)