#!/usr/bin/env python3
"""
Script de test pour vérifier la structure du comparateur sans connexion DB
"""

import sys
import os

# Simuler les imports manquants pour les tests
class MockModule:
    """Module factice pour les tests"""
    pass

# Remplacer les imports si nécessaire
if 'cx_Oracle' not in sys.modules:
    sys.modules['cx_Oracle'] = MockModule()
    sys.modules['cx_Oracle'].Error = Exception
    sys.modules['cx_Oracle'].makedsn = lambda *args, **kwargs: 'mock_dsn'
    sys.modules['cx_Oracle'].connect = lambda *args, **kwargs: None

if 'psycopg2' not in sys.modules:
    sys.modules['psycopg2'] = MockModule()
    sys.modules['psycopg2'].Error = Exception
    sys.modules['psycopg2'].connect = lambda *args, **kwargs: None

import pandas as pd
from datetime import datetime

def test_script_structure():
    """Teste la structure du script principal"""
    print("Test 1: Vérification de l'importation du script...")
    
    try:
        # Le script doit pouvoir être importé
        import compare_tables
        print("✓ Script importable")
    except Exception as e:
        print(f"✗ Erreur d'importation: {e}")
        return False
    
    return True

def test_comparator_class():
    """Teste la classe DatabaseComparator"""
    print("\nTest 2: Vérification de la classe DatabaseComparator...")
    
    try:
        from compare_tables import DatabaseComparator
        
        # Créer une instance avec des variables d'environnement factices
        os.environ['ORACLE_HOST'] = 'localhost'
        os.environ['ORACLE_USER'] = 'test'
        os.environ['ORACLE_PASSWORD'] = 'test'
        os.environ['ORACLE_SERVICE_NAME'] = 'test'
        os.environ['POSTGRES_HOST'] = 'localhost'
        os.environ['POSTGRES_USER'] = 'test'
        os.environ['POSTGRES_PASSWORD'] = 'test'
        os.environ['POSTGRES_DATABASE'] = 'test'
        
        comparator = DatabaseComparator()
        print("✓ Classe instanciable")
        
        # Vérifier que les configurations sont chargées
        assert comparator.oracle_config['host'] == 'localhost'
        assert comparator.postgres_config['host'] == 'localhost'
        print("✓ Configuration chargée correctement")
        
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False
    
    return True

def test_comparison_logic():
    """Teste la logique de comparaison sans base de données"""
    print("\nTest 3: Vérification de la logique de comparaison...")
    
    try:
        from compare_tables import DatabaseComparator
        
        comparator = DatabaseComparator()
        
        # Créer des DataFrames factices
        oracle_cols = pd.DataFrame({
            'column_name': ['ID', 'NAME', 'DATE_CREATED', 'AMOUNT'],
            'data_type': ['NUMBER', 'VARCHAR2', 'DATE', 'NUMBER'],
            'data_length': [None, 100, None, None],
            'data_precision': [10, None, None, 15],
            'data_scale': [0, None, None, 2],
            'nullable': ['N', 'Y', 'N', 'Y'],
            'default_value': [None, None, None, None]
        })
        
        postgres_cols = pd.DataFrame({
            'column_name': ['id', 'name', 'created_at', 'price'],
            'data_type': ['integer', 'character varying', 'timestamp without time zone', 'numeric'],
            'data_length': [None, 100, None, None],
            'data_precision': [32, None, None, 15],
            'data_scale': [0, None, None, 2],
            'nullable': ['NO', 'YES', 'NO', 'YES'],
            'default_value': [None, None, None, None]
        })
        
        # Tester la comparaison des colonnes
        comparison = comparator.compare_columns(oracle_cols, postgres_cols)
        print(f"✓ Comparaison des colonnes: {len(comparison)} résultats")
        
        # Vérifier les résultats
        assert len(comparison) > 0
        assert 'column_name' in comparison.columns
        assert 'status' in comparison.columns
        
        # Tester la comparaison des types
        data_types = comparator.compare_data_types(oracle_cols, postgres_cols)
        print(f"✓ Comparaison des types: {len(data_types)} résultats")
        
        assert len(data_types) > 0
        
    except Exception as e:
        print(f"✗ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def test_type_mapping():
    """Teste le mapping des types Oracle ↔ PostgreSQL"""
    print("\nTest 4: Vérification du mapping des types...")
    
    try:
        from compare_tables import DatabaseComparator
        
        # Tester quelques correspondances
        assert DatabaseComparator._are_types_compatible('NUMBER', 'numeric')
        assert DatabaseComparator._are_types_compatible('VARCHAR2', 'character varying')
        assert DatabaseComparator._are_types_compatible('DATE', 'timestamp without time zone')
        assert DatabaseComparator._are_types_compatible('INTEGER', 'integer')
        
        # Tester une incompatibilité
        assert not DatabaseComparator._are_types_compatible('NUMBER', 'text')
        
        print("✓ Mapping des types fonctionne correctement")
        
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False
    
    return True

def test_summary_generation():
    """Teste la génération du résumé"""
    print("\nTest 5: Vérification de la génération du résumé...")
    
    try:
        from compare_tables import DatabaseComparator
        
        comparator = DatabaseComparator()
        
        # Créer des données factices complètes
        oracle_cols = pd.DataFrame({'column_name': ['ID', 'NAME']})
        postgres_cols = pd.DataFrame({'column_name': ['id', 'name', 'email']})
        
        columns_comparison = pd.DataFrame({
            'column_name': ['id', 'name', 'email'],
            'status': ['Commun', 'Commun', 'PostgreSQL uniquement']
        })
        
        all_data = {
            'oracle_columns': oracle_cols,
            'postgres_columns': postgres_cols,
            'columns_comparison': columns_comparison,
            'oracle_constraints': {
                'primary_keys': pd.DataFrame(),
                'foreign_keys': pd.DataFrame(),
                'unique_constraints': pd.DataFrame()
            },
            'postgres_constraints': {
                'primary_keys': pd.DataFrame(),
                'foreign_keys': pd.DataFrame(),
                'unique_constraints': pd.DataFrame()
            },
            'oracle_indexes': pd.DataFrame(),
            'postgres_indexes': pd.DataFrame(),
            'oracle_statistics': pd.DataFrame(),
            'postgres_statistics': pd.DataFrame()
        }
        
        summary = comparator.generate_summary(all_data)
        print(f"✓ Résumé généré: {len(summary)} lignes")
        
        assert len(summary) > 0
        assert 'Métrique' in summary.columns
        assert 'Valeur' in summary.columns
        
    except Exception as e:
        print(f"✗ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def main():
    """Exécute tous les tests"""
    print("="*60)
    print("TESTS DU COMPARATEUR DE TABLES")
    print("="*60)
    
    tests = [
        test_script_structure,
        test_comparator_class,
        test_comparison_logic,
        test_type_mapping,
        test_summary_generation
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test échoué avec exception: {e}")
            results.append(False)
    
    print("\n" + "="*60)
    print(f"RÉSULTATS: {sum(results)}/{len(results)} tests réussis")
    print("="*60)
    
    if all(results):
        print("\n✓ Tous les tests sont passés!")
        return 0
    else:
        print("\n✗ Certains tests ont échoué")
        return 1

if __name__ == '__main__':
    sys.exit(main())
