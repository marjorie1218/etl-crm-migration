# ETL CRM Migration

Pipeline de migration de données CRM (Extract - Transform - Load) simulant la migration d'un export legacy CSV vers une base de données SQLite propre, avec validation post-migration.

## Description

Ce projet simule un scénario réel de migration de données : une entreprise possède un ancien système CRM dont les données sont exportées en CSV, avec des problèmes typiques d'un vieux système (doublons, formats de date incohérents, champs vides, erreurs de formatage). Le pipeline nettoie ces données et les migre vers une base de données SQLite structurée, tout en générant un rapport de validation.

## Prérequis

- Python 3.12+
- Un environnement virtuel (`venv`)

## Installation

1. Cloner le dépôt :
```powershell
git clone https://github.com/marjorie1218/etl-crm-migration.git
cd etl-crm-migration
```

2. Créer et activer l'environnement virtuel :
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Installer les dépendances :
```powershell
pip install -r requirements.txt
```

## Utilisation

### Lancer le pipeline complet

```powershell
python main.py
```

Cette commande exécute automatiquement, dans l'ordre :
1. **Extract** — lecture du CSV source
2. **Transform** — nettoyage des noms, téléphones, dates, suppression des doublons
3. **Load** — insertion dans la base de données SQLite
4. **Validate** — comparaison source/cible et génération du rapport de migration

### Lancer une étape individuellement

```powershell
python scripts/generate_source_data.py   # génère un nouveau CSV source
python scripts/create_schema.py          # crée le schéma de la base cible
python scripts/extract.py                # extraction seule
python scripts/transform.py              # extraction + nettoyage
python scripts/load.py                   # extraction + nettoyage + chargement
python scripts/validate.py               # validation seule
```

### Réinitialiser la base de données

```powershell
Remove-Item data\target\clients.db
python scripts\create_schema.py
```

## Structure du projet

```
etl-crm-migration/
├── data/
│   ├── source/          # CSV source (legacy)
│   └── target/           # Base de données SQLite (générée)
├── reports/               # Rapport de migration (généré)
├── scripts/
│   ├── generate_source_data.py   # génère le CSV source factice
│   ├── create_schema.py          # crée le schéma de la base cible
│   ├── extract.py                # lecture du CSV source
│   ├── transform.py              # nettoyage des données
│   ├── load.py                   # chargement dans SQLite
│   └── validate.py               # validation post-migration
├── main.py                # orchestration du pipeline complet
├── requirements.txt
└── README.md
```

## Rapport de migration

Un rapport texte est généré à chaque exécution dans `reports/migration_report.txt`, contenant :
- Nombre de lignes source vs cible
- Nombre de doublons supprimés
- Emails perdus (le cas échéant)
- Statut final (PASS/FAIL)

## Statut

✅ Projet terminé — les 12 phases (0-11) sont complètes.