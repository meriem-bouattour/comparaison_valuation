# Comparaison de Tables Oracle ↔ PostgreSQL

Script Python pour comparer deux tables de bases de données situées dans des environnements différents (Oracle et PostgreSQL) et générer un rapport Excel détaillé.

## 📋 Description

Ce projet permet de comparer :
- **valuation_refprod** : Table Oracle (environnement refprof)
- **valuation_ids** : Table PostgreSQL (environnement ids)

Le script génère un rapport Excel complet avec plusieurs onglets contenant des analyses détaillées de la structure et des données.

## 🚀 Installation

### Prérequis

- Python 3.7 ou supérieur
- Accès aux bases de données Oracle et PostgreSQL
- Oracle Instant Client (pour la connexion Oracle)

### 1. Cloner le repository

```bash
git clone https://github.com/meriem-bouattour/comparaison_valuation.git
cd comparaison_valuation
```

### 2. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

### 3. Installer Oracle Instant Client

#### Sur Linux/macOS :

1. Télécharger Oracle Instant Client depuis : https://www.oracle.com/database/technologies/instant-client/downloads.html
2. Extraire l'archive dans `/opt/oracle/instantclient_XX_X`
3. Configurer les variables d'environnement :

```bash
export LD_LIBRARY_PATH=/opt/oracle/instantclient_XX_X:$LD_LIBRARY_PATH
export PATH=/opt/oracle/instantclient_XX_X:$PATH
```

#### Sur Windows :

1. Télécharger Oracle Instant Client
2. Extraire dans `C:\oracle\instantclient_XX_X`
3. Ajouter le chemin au PATH système

## ⚙️ Configuration

### 1. Créer le fichier `.env`

Copier le fichier d'exemple et le remplir avec vos informations :

```bash
cp .env.example .env
```

### 2. Éditer le fichier `.env`

```env
# Oracle Connection (refprof)
ORACLE_HOST=votre-serveur-oracle.com
ORACLE_PORT=1521
ORACLE_SERVICE_NAME=ORCL
ORACLE_USER=votre_utilisateur
ORACLE_PASSWORD=votre_mot_de_passe
ORACLE_TABLE=VALUATION_REFPROD

# PostgreSQL Connection (ids)
POSTGRES_HOST=votre-serveur-postgres.com
POSTGRES_PORT=5432
POSTGRES_DATABASE=votre_base
POSTGRES_USER=votre_utilisateur
POSTGRES_PASSWORD=votre_mot_de_passe
POSTGRES_SCHEMA=public
POSTGRES_TABLE=valuation_ids

# Output
EXCEL_OUTPUT_PATH=rapport_comparaison.xlsx
```

⚠️ **Sécurité** : Ne jamais committer le fichier `.env` contenant vos mots de passe !

## 📊 Utilisation

### Exécuter le script

```bash
python compare_tables.py
```

Le script va :
1. Se connecter aux deux bases de données
2. Extraire les métadonnées complètes
3. Effectuer les comparaisons
4. Générer le rapport Excel

### Exemple de sortie

```
╔═══════════════════════════════════════════════════════════════╗
║   COMPARATEUR DE TABLES ORACLE ↔ POSTGRESQL                  ║
║   Génère un rapport Excel détaillé                            ║
╚═══════════════════════════════════════════════════════════════╝

2024-02-17 10:30:15 - INFO - Connexion à Oracle...
2024-02-17 10:30:16 - INFO - ✓ Connexion Oracle établie
2024-02-17 10:30:16 - INFO - Connexion à PostgreSQL...
2024-02-17 10:30:17 - INFO - ✓ Connexion PostgreSQL établie
2024-02-17 10:30:17 - INFO - Extraction des colonnes Oracle...
2024-02-17 10:30:18 - INFO - ✓ 45 colonnes Oracle extraites
...

✓ Rapport Excel généré: rapport_comparaison.xlsx
```

## 📑 Contenu du Rapport Excel

Le rapport généré contient les onglets suivants :

### 1. **Résumé**
- Date et heure de génération
- Nombre total de colonnes dans chaque table
- Nombre total d'enregistrements
- Score de similarité global
- Résumé des différences

### 2. **Colonnes**
- Liste complète des colonnes des deux tables
- Colonnes présentes uniquement dans Oracle (en rouge)
- Colonnes présentes uniquement dans PostgreSQL (en rouge)
- Colonnes communes (en vert)

### 3. **Types de données**
- Comparaison des types de données pour chaque colonne commune
- Mapping Oracle ↔ PostgreSQL
- Compatibilité des types
- Différences de précision et de longueur
- Différences de nullabilité

### 4. **Clés et Contraintes**
- **Clés primaires (PK)** dans chaque table
- **Clés étrangères (FK)** et leurs références
- **Contraintes UNIQUE**
- Comparaison des contraintes entre les deux tables

### 5. **Index**
- Liste des index sur chaque table
- Colonnes indexées
- Type d'index (BTREE, UNIQUE, etc.)
- Comparaison des stratégies d'indexation

### 6. **Statistiques**
Pour chaque table et colonne :
- Nombre total de lignes
- Nombre de valeurs NULL
- Nombre de valeurs distinctes
- Pour les colonnes numériques : min, max, moyenne
- Pour les colonnes texte : longueur min/max

## 🎨 Formatage du Rapport

Le rapport Excel est automatiquement formaté avec :
- **En-têtes en gras** avec fond bleu
- **Couleur verte** pour les correspondances et valeurs "Oui"
- **Couleur rouge** pour les différences et valeurs "Non"
- **Colonnes auto-dimensionnées** pour une meilleure lisibilité
- **Première ligne figée** pour garder les en-têtes visibles

## 🔧 Gestion des Erreurs

Le script gère automatiquement :
- Échecs de connexion aux bases de données
- Tables inexistantes
- Colonnes avec des types de données non standards
- Erreurs de calcul de statistiques

Les messages d'erreur sont affichés dans la console avec des logs détaillés.

## 📦 Structure du Projet

```
comparaison_valuation/
├── compare_tables.py       # Script principal
├── requirements.txt        # Dépendances Python
├── .env.example           # Exemple de configuration
├── .env                   # Configuration (à créer, non versionnée)
├── README.md              # Documentation
└── rapport_comparaison.xlsx  # Rapport généré (exemple)
```

## 🔍 Dépendances

- **cx_Oracle** (≥8.3.0) : Connexion à Oracle Database
- **psycopg2-binary** (≥2.9.0) : Connexion à PostgreSQL
- **pandas** (≥1.5.0) : Manipulation de données
- **openpyxl** (≥3.1.0) : Génération de fichiers Excel
- **python-dotenv** (≥1.0.0) : Chargement des variables d'environnement

## 🐛 Dépannage

### Erreur : "cx_Oracle.DatabaseError: DPI-1047"

**Solution** : Oracle Instant Client n'est pas installé ou mal configuré.
- Vérifier l'installation d'Oracle Instant Client
- Vérifier les variables d'environnement `LD_LIBRARY_PATH` (Linux) ou `PATH` (Windows)

### Erreur : "psycopg2.OperationalError: could not connect"

**Solution** : Problème de connexion PostgreSQL.
- Vérifier les informations de connexion dans `.env`
- Vérifier que PostgreSQL est accessible depuis votre machine
- Vérifier les règles de pare-feu

### Le script est lent

**Solution** : Le calcul des statistiques peut être long pour de grandes tables.
- Les statistiques sont calculées colonne par colonne
- Pour accélérer, vous pouvez commenter la section statistiques dans le code

### Erreur de mémoire

**Solution** : Pour les très grandes tables, le script peut consommer beaucoup de mémoire.
- Augmenter la mémoire disponible pour Python
- Traiter les statistiques par lots

## 📝 Notes

- Le script fonctionne même si les tables ont des structures très différentes
- Les connexions sont automatiquement fermées à la fin de l'exécution
- Le rapport existant est écrasé à chaque exécution
- Les mots de passe ne sont jamais affichés dans les logs

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## 📄 Licence

Ce projet est sous licence MIT.

## 👤 Auteur

Meriem Bouattour

---

**Note** : Assurez-vous de ne jamais committer vos fichiers `.env` contenant des informations sensibles !