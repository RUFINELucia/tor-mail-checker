# tor-mail-checker
Vérifie si une adresse email a été compromise, en la comparant à une base de données .onion (simulée).

<p align="center">
  <img src="lucia-rufine-logo.jpg" alt="lucia-rufine" width="400"/>
</p>

## Description


`tor-mail-checker` est un petit outil en Python qui permet de vérifier si une ou plusieurs adresses e‑mail figurent dans une "base" simulée de fuites hébergées sur des services .onion. Cette base est stockée localement dans le dossier `leaks/` (fichier `onion_db.txt`) pour des raisons de test et de confidentialité — il s'agit de données simulées et factices.


> ⚠️ Cet outil est conçu **uniquement** pour des démonstrations et tests. Ne l'utilise pas pour automatiser des vérifications massives sans respecter la vie privée et la loi.


## Fonctionnalités


- Vérifie une adresse e‑mail unique ou un fichier contenant des adresses.
- Recherche case-insensitive dans la base simulée (`leaks/onion_db.txt`).
- Option d'export CSV des résultats.


## Installation


1. Cloner le dépôt :

```bash
git clone https://github.com/TON_COMPTE/tor-mail-checker.git
cd tor-mail-checker
```

2. (Optionnel) Créer un environnement virtuel et installer les dépendances :

```bash
python -m venv .venv
source .venv/bin/activate  # sur Linux/macOS
.\\.venv\\Scripts\\activate   # sur Windows
pip install -r requirements.txt

Aucune dépendance externe n'est strictement requise pour la version fournie, mais le requirements.txt est présent pour évoluer.

## Usage


Vérifier une adresse :

```bash
python check_mail.py --email alice@example.onion

Vérifier plusieurs adresses depuis un fichier (une adresse par ligne) :

```bash
python check_mail.py --file my_emails.txt

Exporter le résultat au format CSV :

```bash
python check_mail.py --email bob@example.onion --output results.csv

## Fichier de fuite simulée


La base simulée se trouve dans leaks/onion_db.txt (fichiers factices). Tu peux ajouter ou modifier les lignes pour tester d'autres cas.

## License


MIT

## Avertissements


- Les données dans leaks/onion_db.txt sont fictives.
- Respecte la loi et la vie privée avant d'utiliser des outils de vérification d'adresses e-mail.
