import xml.etree.ElementTree as ET
import pandas as pd

# Fonction pour parser XML et convertir en DataFrame
def xml_to_dataframe(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()  
    
    # Extraire les données (à adapter selon la structure de votre XML)
    data = []
    for child in root:
        row = {}
        for elem in child:
            row[elem.tag] = elem.text
        data.append(row)
    
    return pd.DataFrame(data)

# Charger les deux fichiers XML
print("Chargement des fichiers XML...")
df_ids = xml_to_dataframe('valuation_ids.pack')
df_refprod = xml_to_dataframe('valuation_refprod.pack')

# Informations de base
print("\n=== valuation_ids.pack ===")
print(f"Shape: {df_ids.shape}")
print(f"Colonnes: {df_ids.columns.tolist()}")
print(f"\n{df_ids.head()}\n")
print(f"\nInfo:")
print(df_ids.info())
print(f"\nStatistiques:")
print(df_ids.describe())

print("\n" + "="*80)
print("=== valuation_refprod.pack ===")
print(f"Shape: {df_refprod.shape}")
print(f"Colonnes: {df_refprod.columns.tolist()}")
print(f"\n{df_refprod.head()}\n")
print(f"\nInfo:")
print(df_refprod.info())
print(f"\nStatistiques:")
print(df_refprod.describe())

# Comparaison
print("\n" + "="*80)
print("=== COMPARAISON ===")
print(f"Nombre de lignes - valuation_ids: {df_ids.shape[0]}")
print(f"Nombre de lignes - valuation_refprod: {df_refprod.shape[0]}")
print(f"Différence de lignes: {df_ids.shape[0] - df_refprod.shape[0]}")

print(f"\nNombre de colonnes - valuation_ids: {df_ids.shape[1]}")
print(f"Nombre de colonnes - valuation_refprod: {df_refprod.shape[1]}")
print(f"Différence de colonnes: {df_ids.shape[1] - df_refprod.shape[1]}")

# Colonnes en commun et différentes
common_cols = set(df_ids.columns) & set(df_refprod.columns)
only_ids = set(df_ids.columns) - set(df_refprod.columns)
only_refprod = set(df_refprod.columns) - set(df_ids.columns)

print(f"\nNombre de colonnes communes: {len(common_cols)}")
print(f"Colonnes communes: {sorted(common_cols)}")
print(f"\nColonnes uniquement dans valuation_ids ({len(only_ids)}): {sorted(only_ids)}")
print(f"Colonnes uniquement dans valuation_refprod ({len(only_refprod)}): {sorted(only_refprod)}")

# Comparaison des valeurs dans les colonnes communes
if common_cols:
    print("\n" + "="*80)
    print("=== COMPARAISON DES VALEURS (colonnes communes) ===")
    for col in sorted(common_cols):
        if col in df_ids.columns and col in df_refprod.columns:
            unique_ids = df_ids[col].nunique()
            unique_refprod = df_refprod[col].nunique()
            print(f"\n{col}:")
            print(f"  - Valeurs uniques dans valuation_ids: {unique_ids}")
            print(f"  - Valeurs uniques dans valuation_refprod: {unique_refprod}")

# Sauvegarder les résultats dans un fichier
print("\n" + "="*80)
print("Sauvegarde des résultats dans comparison_results.txt...")
with open('comparison_results.txt', 'w', encoding='utf-8') as f:
    f.write("COMPARAISON DES FICHIERS .pack\n")
    f.write("="*80 + "\n\n")
    f.write(f"valuation_ids.pack: {df_ids.shape[0]} lignes, {df_ids.shape[1]} colonnes\n")
    f.write(f"valuation_refprod.pack: {df_refprod.shape[0]} lignes, {df_refprod.shape[1]} colonnes\n\n")
    f.write(f"Colonnes communes: {sorted(common_cols)}\n")
    f.write(f"Colonnes uniquement dans valuation_ids: {sorted(only_ids)}\n")
    f.write(f"Colonnes uniquement dans valuation_refprod: {sorted(only_refprod)}\n")

print("Terminé ! Résultats sauvegardés dans comparison_results.txt")