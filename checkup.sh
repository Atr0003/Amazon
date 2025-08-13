# 0) Activer l'environnement (si pas déjà fait)
source .venv/bin/activate

# 1) Installer / vérifier les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# 2) Petit stub CLI pour vérifier que ça lance (écrase le fichier si besoin)
cat > src/amazons/cli.py << 'EOF'
def main():
    print("Amazons CLI OK")

if __name__ == "__main__":
    main()
EOF

# 3) Test ultra-simple pour valider la chaîne pytest
cat > tests/test_smoke.py << 'EOF'
def test_smoke():
    assert 1 + 1 == 2
EOF

# 4) Lancer les outils qualité
ruff check src tests
mypy src || true         # (on tolère les avertissements au début)

# 5) Lancer les tests
pytest

# 6) Exécuter la CLI
python -m amazons.cli

# 7) Commit + push
git add .
git commit -m "Smoke test: CLI stub + test basique + setup outils"
# Si ton upstream n'est pas encore défini :
git push -u origin main   # remplace 'main' par le nom de ta branche si différent
