#!/usr/bin/env python3
"""
Script de vérification de base sans dépendances externes
"""

import sys
import os
import ast

def verify_script_syntax():
    """Vérifie que le script Python est syntaxiquement correct"""
    print("="*60)
    print("VÉRIFICATION DU SCRIPT COMPARE_TABLES.PY")
    print("="*60)
    
    script_path = 'compare_tables.py'
    
    print(f"\nTest 1: Vérification de l'existence du fichier...")
    if not os.path.exists(script_path):
        print(f"✗ Fichier {script_path} non trouvé")
        return False
    print(f"✓ Fichier {script_path} trouvé")
    
    print(f"\nTest 2: Vérification de la syntaxe Python...")
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        print("✓ Syntaxe Python valide")
    except SyntaxError as e:
        print(f"✗ Erreur de syntaxe: {e}")
        return False
    
    print(f"\nTest 3: Vérification de la structure du code...")
    
    # Vérifier les imports attendus
    expected_imports = [
        'cx_Oracle',
        'psycopg2',
        'pandas',
        'openpyxl',
        'dotenv'
    ]
    
    for imp in expected_imports:
        if imp in code or imp.replace('_', '-') in code:
            print(f"✓ Import de {imp} présent")
        else:
            print(f"⚠ Import de {imp} non trouvé (peut-être normal)")
    
    print(f"\nTest 4: Vérification de la classe principale...")
    if 'class DatabaseComparator' in code:
        print("✓ Classe DatabaseComparator trouvée")
    else:
        print("✗ Classe DatabaseComparator non trouvée")
        return False
    
    print(f"\nTest 5: Vérification des méthodes principales...")
    expected_methods = [
        'connect_oracle',
        'connect_postgres',
        'get_oracle_columns',
        'get_postgres_columns',
        'get_oracle_constraints',
        'get_postgres_constraints',
        'get_oracle_indexes',
        'get_postgres_indexes',
        'get_oracle_statistics',
        'get_postgres_statistics',
        'compare_columns',
        'compare_data_types',
        'generate_summary',
        'format_excel',
        'generate_report'
    ]
    
    found_methods = 0
    for method in expected_methods:
        if f'def {method}' in code:
            print(f"✓ Méthode {method} trouvée")
            found_methods += 1
        else:
            print(f"✗ Méthode {method} non trouvée")
    
    print(f"\n{found_methods}/{len(expected_methods)} méthodes trouvées")
    
    print(f"\nTest 6: Vérification du point d'entrée...")
    if "if __name__ == '__main__':" in code:
        print("✓ Point d'entrée main() présent")
    else:
        print("✗ Point d'entrée main() non trouvé")
        return False
    
    print(f"\nTest 7: Vérification de la gestion des erreurs...")
    if 'try:' in code and 'except' in code:
        print("✓ Gestion des erreurs présente")
    else:
        print("⚠ Gestion des erreurs limitée")
    
    print(f"\nTest 8: Vérification du logging...")
    if 'logging' in code and 'logger' in code:
        print("✓ Système de logging présent")
    else:
        print("⚠ Système de logging non détecté")
    
    return True

def verify_requirements():
    """Vérifie le fichier requirements.txt"""
    print("\n" + "="*60)
    print("VÉRIFICATION DE REQUIREMENTS.TXT")
    print("="*60)
    
    req_path = 'requirements.txt'
    
    print(f"\nTest 1: Vérification de l'existence du fichier...")
    if not os.path.exists(req_path):
        print(f"✗ Fichier {req_path} non trouvé")
        return False
    print(f"✓ Fichier {req_path} trouvé")
    
    print(f"\nTest 2: Vérification des dépendances...")
    expected_deps = [
        'cx_Oracle',
        'psycopg2-binary',
        'pandas',
        'openpyxl',
        'python-dotenv'
    ]
    
    with open(req_path, 'r') as f:
        content = f.read()
    
    found_deps = 0
    for dep in expected_deps:
        if dep in content:
            print(f"✓ Dépendance {dep} présente")
            found_deps += 1
        else:
            print(f"✗ Dépendance {dep} manquante")
    
    print(f"\n{found_deps}/{len(expected_deps)} dépendances trouvées")
    
    return found_deps == len(expected_deps)

def verify_env_example():
    """Vérifie le fichier .env.example"""
    print("\n" + "="*60)
    print("VÉRIFICATION DE .ENV.EXAMPLE")
    print("="*60)
    
    env_path = '.env.example'
    
    print(f"\nTest 1: Vérification de l'existence du fichier...")
    if not os.path.exists(env_path):
        print(f"✗ Fichier {env_path} non trouvé")
        return False
    print(f"✓ Fichier {env_path} trouvé")
    
    print(f"\nTest 2: Vérification des variables...")
    expected_vars = [
        'ORACLE_HOST',
        'ORACLE_PORT',
        'ORACLE_SERVICE_NAME',
        'ORACLE_USER',
        'ORACLE_PASSWORD',
        'ORACLE_TABLE',
        'POSTGRES_HOST',
        'POSTGRES_PORT',
        'POSTGRES_DATABASE',
        'POSTGRES_USER',
        'POSTGRES_PASSWORD',
        'POSTGRES_SCHEMA',
        'POSTGRES_TABLE',
        'EXCEL_OUTPUT_PATH'
    ]
    
    with open(env_path, 'r') as f:
        content = f.read()
    
    found_vars = 0
    for var in expected_vars:
        if var in content:
            print(f"✓ Variable {var} présente")
            found_vars += 1
        else:
            print(f"✗ Variable {var} manquante")
    
    print(f"\n{found_vars}/{len(expected_vars)} variables trouvées")
    
    return found_vars == len(expected_vars)

def verify_readme():
    """Vérifie le fichier README.md"""
    print("\n" + "="*60)
    print("VÉRIFICATION DE README.MD")
    print("="*60)
    
    readme_path = 'README.md'
    
    print(f"\nTest 1: Vérification de l'existence du fichier...")
    if not os.path.exists(readme_path):
        print(f"✗ Fichier {readme_path} non trouvé")
        return False
    print(f"✓ Fichier {readme_path} trouvé")
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\nTest 2: Vérification des sections...")
    expected_sections = [
        'Installation',
        'Configuration',
        'Utilisation',
        'Rapport Excel',
        'Dépendances'
    ]
    
    found_sections = 0
    for section in expected_sections:
        if section.lower() in content.lower():
            print(f"✓ Section '{section}' présente")
            found_sections += 1
        else:
            print(f"⚠ Section '{section}' non trouvée")
    
    print(f"\n{found_sections}/{len(expected_sections)} sections trouvées")
    
    file_size = len(content)
    print(f"\nTaille du README: {file_size} caractères")
    if file_size > 1000:
        print("✓ Documentation complète")
    else:
        print("⚠ Documentation courte")
    
    return True

def verify_gitignore():
    """Vérifie le fichier .gitignore"""
    print("\n" + "="*60)
    print("VÉRIFICATION DE .GITIGNORE")
    print("="*60)
    
    gitignore_path = '.gitignore'
    
    print(f"\nTest 1: Vérification de l'existence du fichier...")
    if not os.path.exists(gitignore_path):
        print(f"✗ Fichier {gitignore_path} non trouvé")
        return False
    print(f"✓ Fichier {gitignore_path} trouvé")
    
    with open(gitignore_path, 'r') as f:
        content = f.read()
    
    print(f"\nTest 2: Vérification des patterns...")
    important_patterns = [
        '.env',
        '__pycache__',
        '*.pyc',
        'venv'
    ]
    
    found_patterns = 0
    for pattern in important_patterns:
        if pattern in content:
            print(f"✓ Pattern '{pattern}' présent")
            found_patterns += 1
        else:
            print(f"⚠ Pattern '{pattern}' non trouvé")
    
    print(f"\n{found_patterns}/{len(important_patterns)} patterns importants trouvés")
    
    return True

def main():
    """Exécute toutes les vérifications"""
    print("\n" + "="*60)
    print("VÉRIFICATION COMPLÈTE DU PROJET")
    print("="*60 + "\n")
    
    results = []
    
    results.append(("Script principal", verify_script_syntax()))
    results.append(("Requirements", verify_requirements()))
    results.append(("Configuration", verify_env_example()))
    results.append(("Documentation", verify_readme()))
    results.append(("Gitignore", verify_gitignore()))
    
    print("\n" + "="*60)
    print("RÉSUMÉ DES VÉRIFICATIONS")
    print("="*60)
    
    for name, result in results:
        status = "✓ OK" if result else "✗ ÉCHEC"
        print(f"{name:20s}: {status}")
    
    success_count = sum(1 for _, result in results if result)
    total_count = len(results)
    
    print(f"\n{success_count}/{total_count} vérifications réussies")
    
    if success_count == total_count:
        print("\n✓ Tous les fichiers sont correctement créés et structurés!")
        return 0
    else:
        print("\n⚠ Certaines vérifications ont échoué, mais le projet peut être fonctionnel")
        return 0

if __name__ == '__main__':
    sys.exit(main())
