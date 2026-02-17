import pandas as pd

# Charger les deux fichiers .pack
df_ids = pd.read_pickle('valuation_ids.pack')
df_refprod = pd.read_pickle('valuation_refprod.pack')

# Informations de base
print("=== valuation_ids.pack ===")
print(f"Shape: {df_ids.shape}")
print(f"Colonnes: {df_ids.columns.tolist()}")
print(f"\n{df_ids.head()}\n")
print(f"Info:\n{df_ids.info()}\n")

print("\n=== valuation_refprod.pack ===")
print(f"Shape: {df_refprod.shape}")
print(f"Colonnes: {df_refprod.columns.tolist()}")
print(f"\n{df_refprod.head()}\n")
print(f"Info:\n{df_refprod.info()}\n")

# Comparaison
print("\n=== COMPARAISON ===")
print(f"Différence de lignes: {df_ids.shape[0] - df_refprod.shape[0]}")
print(f"Différence de colonnes: {df_ids.shape[1] - df_refprod.shape[1]}")

# Colonnes en commun et différentes
common_cols = set(df_ids.columns) & set(df_refprod.columns)
only_ids = set(df_ids.columns) - set(df_refprod.columns)
only_refprod = set(df_refprod.columns) - set(df_ids.columns)

print(f"\nColonnes communes: {common_cols}")
print(f"Seulement dans valuation_ids: {only_ids}")
print(f"Seulement dans valuation_refprod: {only_refprod}")