# Ouvrir le fichier CSV en mode lecture
with open('pop19.CSV', 'r') as file:
    # Lire toutes les lignes du fichier
    lines = file.readlines()

# Créer une liste pour stocker les nouvelles lignes
new_lines = []

# Parcourir toutes les lignes du fichier
for line in lines:
    line2 = "population,2019,"+line
    new_lines.append(line2)

# Écrire les nouvelles lignes dans un nouveau fichier CSV
with open('pop19.CSV', 'w') as new_file:
    # Écrire les nouvelles lignes dans le fichier
    new_file.writelines(new_lines)

# Ouvrir le fichier CSV en mode lecture
with open('pop13.CSV', 'r') as file:
    # Lire toutes les lignes du fichier
    lines = file.readlines()

# Créer une liste pour stocker les nouvelles lignes
new_lines = []

# Parcourir toutes les lignes du fichier
for line in lines:
    line2 = "population,2013,"+line
    new_lines.append(line2)

# Écrire les nouvelles lignes dans un nouveau fichier CSV
with open('pop13.CSV', 'w') as new_file:
    # Écrire les nouvelles lignes dans le fichier
    new_file.writelines(new_lines)

# Ouvrir le fichier CSV en mode lecture
with open('pop08.CSV', 'r') as file:
    # Lire toutes les lignes du fichier
    lines = file.readlines()

# Créer une liste pour stocker les nouvelles lignes
new_lines = []

# Parcourir toutes les lignes du fichier
for line in lines:
    line2 = "population,2008,"+line
    new_lines.append(line2)

# Écrire les nouvelles lignes dans un nouveau fichier CSV
with open('pop08.CSV', 'w') as new_file:
    # Écrire les nouvelles lignes dans le fichier
    new_file.writelines(new_lines)


# Ouvrir le fichier CSV en mode lecture
with open('naiss1319.CSV', 'r') as file:
    # Lire toutes les lignes du fichier
    lines = file.readlines()

# Créer une liste pour stocker les nouvelles lignes
new_lines = []

# Parcourir toutes les lignes du fichier
for line in lines:
    line2 = "naissance,2013,2019,"+line
    new_lines.append(line2)

# Écrire les nouvelles lignes dans un nouveau fichier CSV
with open('naiss1319.CSV', 'w') as new_file:
    # Écrire les nouvelles lignes dans le fichier
    new_file.writelines(new_lines)


# Ouvrir le fichier CSV en mode lecture
with open('naiss0813.CSV', 'r') as file:
    # Lire toutes les lignes du fichier
    lines = file.readlines()

# Créer une liste pour stocker les nouvelles lignes
new_lines = []

# Parcourir toutes les lignes du fichier
for line in lines:
    line2 = "naissance,2008,2013,"+line
    new_lines.append(line2)

# Écrire les nouvelles lignes dans un nouveau fichier CSV
with open('naiss0813.CSV', 'w') as new_file:
    # Écrire les nouvelles lignes dans le fichier
    new_file.writelines(new_lines)