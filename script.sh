# 1) Créer et activer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# 2) Mettre pip à jour
pip install --upgrade pip

# 3) Créer la structure des dossiers
mkdir -p src/amazons tests docs

# 4) Créer les fichiers de base
touch src/amazons/__init__.py src/amazons/state.py src/amazons/rules.py src/amazons/search.py src/amazons/cli.py src/amazons/utils.py
touch tests/test_rules.py tests/test_search.py
touch README.md .gitignore requirements.txt pyproject.toml Makefile

# 5) Remplir rapidement requirements.txt avec les outils de dev
echo "pytest>=8.0
ruff>=0.4.0
mypy>=1.8.0" > requirements.txt

# 6) Remplir rapidement .gitignore
echo ".venv/
__pycache__/
*.pyc
.pytest_cache/
.DS_Store
.idea/
.vscode/" > .gitignore

# 7) Installer les dépendances
pip install -r requirements.txt

# 8) Premier commit Git
git add .
git commit -m "Initialisation du projet Amazons avec structure et outils"
