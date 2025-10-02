#!/usr/bin/env python3
"""
check_mail.py

Vérifie si une ou plusieurs adresses e-mail figurent dans une base .onion simulée
stockée dans `leaks/onion_db.txt`.

Usage:
    python check_mail.py --email alice@example.onion
    python check_mail.py --file emails.txt --output results.csv
    python check_mail.py --email bob@example.onion --quiet
"""
from pathlib import Path
import argparse
import csv
import sys

DB_PATH = Path("leaks/onion_db.txt")


def load_db(path: Path):
    """Charge la 'base' simulée et retourne un set d'adresses en minuscule."""
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as f:
        lines = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            lines.append(line.lower())
        return set(lines)


def check_email(email: str, db: set) -> bool:
    return email.strip().lower() in db


def check_file(file_path: Path, db: set):
    results = []
    if not file_path.exists():
        raise FileNotFoundError(f"Fichier non trouvé: {file_path}")
    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            email = line.strip()
            if not email:
                continue
            compromised = check_email(email, db)
            results.append((email, compromised))
    return results


def parse_args():
    parser = argparse.ArgumentParser(
        description="Vérifie si des e-mails sont présents dans une base .onion simulée."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--email", "-e", help="Adresse e-mail à vérifier")
    group.add_argument("--file", "-f", type=Path, help="Fichier contenant des e-mails (1 par ligne)")
    parser.add_argument("--output", "-o", help="Fichier CSV de sortie (optionnel)")
    parser.add_argument("--quiet", "-q", action="store_true", help="Mode silencieux (affiche moins d'information)")
    return parser.parse_args()


def main():
    args = parse_args()
    db = load_db(DB_PATH)

    if not db and not args.quiet:
        print(f"Attention : la base simulée est vide ({DB_PATH}).", file=sys.stderr)

    results = []
    if args.email:
        compromised = check_email(args.email, db)
        results = [(args.email, compromised)]
    else:
        try:
            results = check_file(args.file, db)
        except FileNotFoundError as e:
            print(str(e), file=sys.stderr)
            sys.exit(2)

    for email, compromised in results:
        if args.quiet:
            print(f"{email},{ 'yes' if compromised else 'no' }")
        else:
            status = "COMPROMI(S) ✅" if compromised else "OK ❌"
            print(f"{email}: {status}")

    if args.output:
        try:
            with open(args.output, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["email", "compromised"])
                for email, compromised in results:
                    writer.writerow([email, "yes" if compromised else "no"])
            if not args.quiet:
                print(f"Résultats enregistrés dans {args.output}")
        except Exception as e:
            print(f"Erreur lors de l'écriture du fichier {args.output}: {e}", file=sys.stderr)
            sys.exit(3)


if __name__ == "__main__":
    main()
