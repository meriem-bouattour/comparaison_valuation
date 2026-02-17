# Guide de Démarrage Rapide

## Installation en 5 minutes

### 1. Cloner le projet
```bash
git clone https://github.com/meriem-bouattour/comparaison_valuation.git
cd comparaison_valuation
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Installer Oracle Instant Client

**Linux/macOS:**
```bash
# Télécharger depuis: https://www.oracle.com/database/technologies/instant-client/downloads.html
# Puis extraire et configurer:
export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_9:$LD_LIBRARY_PATH
```

**Windows:**
- Télécharger et extraire dans `C:\oracle\instantclient_21_9`
- Ajouter au PATH système

### 4. Configurer les connexions
```bash
cp .env.example .env
nano .env  # ou tout autre éditeur
```

Remplir avec vos informations:
```env
ORACLE_HOST=votre-serveur.com
ORACLE_USER=votre_user
ORACLE_PASSWORD=votre_password
# ... etc
```

### 5. Exécuter le script
```bash
python compare_tables.py
```

## Résultat

Le script génère automatiquement `rapport_comparaison.xlsx` avec 6 onglets:
1. **Résumé** - Vue d'ensemble
2. **Colonnes** - Comparaison des colonnes
3. **Types de données** - Mapping des types
4. **Clés et Contraintes** - PK, FK, UNIQUE
5. **Index** - Liste des index
6. **Statistiques** - Statistiques détaillées

## Exemple de sortie

```
╔═══════════════════════════════════════════════════════════════╗
║   COMPARATEUR DE TABLES ORACLE ↔ POSTGRESQL                  ║
║   Génère un rapport Excel détaillé                            ║
╚═══════════════════════════════════════════════════════════════╝

2024-02-17 10:30:15 - INFO - Connexion à Oracle...
2024-02-17 10:30:16 - INFO - ✓ Connexion Oracle établie
2024-02-17 10:30:16 - INFO - Connexion à PostgreSQL...
2024-02-17 10:30:17 - INFO - ✓ Connexion PostgreSQL établie
...
✓ Rapport Excel généré: rapport_comparaison.xlsx
```

## Dépannage Rapide

**Erreur: "No module named 'cx_Oracle'"**
→ `pip install -r requirements.txt`

**Erreur: "DPI-1047: Cannot locate a 64-bit Oracle Client"**
→ Installer Oracle Instant Client

**Erreur: "could not connect to server"**
→ Vérifier les informations dans `.env`

## Support

Pour plus de détails, consultez le [README.md](README.md) complet.
