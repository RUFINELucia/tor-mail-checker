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
