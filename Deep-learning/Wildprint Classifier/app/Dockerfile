# app/Dockerfile

FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY API/ ./API/

# Exposer le port sur lequel l'app sera lancée
EXPOSE 8000

# Lancer l'app FastAPI via Uvicorn
CMD ["uvicorn", "API.app:app", "--host", "0.0.0.0", "--port", "8000"]
