from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from PIL import Image
import numpy as np
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import shutil
from datetime import datetime
import tensorflow as tf

# --- Répertoires absolus ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # app/API
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
MODEL_PATH = os.path.join(BASE_DIR, "best_model.h5")
UPLOAD_FOLDER = os.path.join(STATIC_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Base de données ---
Base = declarative_base()
DB_URL = os.path.join(BASE_DIR, "infos_complementaires.db")
engine = create_engine(
    f"sqlite:///{DB_URL}", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

  
class Especes(Base):
    __tablename__ = "especes"
    espece = Column("Espèce", String, primary_key=True, index=True)
    description = Column("Description", Text)
    nom_latin = Column("Nom latin", String)
    famille = Column("Famille", String)
    taille = Column("Taille", String)
    region = Column("Région", String)
    habitat = Column("Habitat", String)
    fun_fact = Column("Fun fact", Text)
    image = Column(String)
    image_fun_fact = Column(String)

  
class PhotosUtilisateurs(Base):
    __tablename__ = "photos_utilisateurs"
    id = Column(Integer, primary_key=True, index=True)
    chemin_fichier = Column(String)
    date = Column(String)
    heure = Column(String)
    localisation = Column(String)
    espece = Column(String)
    date_ajout = Column(
        String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

# Crée les tables
Base.metadata.create_all(bind=engine)

# --- FastAPI ---
app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# --- Chargement du modèle ---
model = tf.keras.models.load_model(MODEL_PATH)
classes = [
    'Castor', 'Chat', 'Chien', 'Coyote', 'Ecureuil', 'Lapin', 'Loup', 'Lynx',
    'Ours', 'Puma', 'Rat', 'Raton laveur', 'Renard'
]

# --- Formats autorisés ---
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.heic'}

  
def allowed_file(filename):
    return any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)

# --- Routes ---
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

  
@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

  
@app.get("/mentions_legales", response_class=HTMLResponse)
async def mentions_legales(request: Request):
    return templates.TemplateResponse(
        "mentions_legales.html", {"request": request}
    )

  
@app.get("/scan", response_class=HTMLResponse)
async def scan(request: Request):
    return templates.TemplateResponse("scan.html", {"request": request})

  
@app.get("/exploration", response_class=HTMLResponse)
async def exploration(request: Request):
    return templates.TemplateResponse("exploration.html", {"request": request})

  
@app.get("/fiche_animal/{espece}", response_class=HTMLResponse)
async def fiche_animal(request: Request, espece: str):
    db = SessionLocal()
    try:
        animal_info = db.query(Especes).filter(
            Especes.espece == espece
        ).first()
        return templates.TemplateResponse(
            "fiche_animal.html",
            {
                "request": request,
                "animal_info": animal_info
            }
        )
    finally:
        db.close()

  
@app.get("/scan_oops_pas_trouve", response_class=HTMLResponse)
async def scan_oops_pas_trouve(request: Request):
    return templates.TemplateResponse(
        "scan_oops_pas_trouve.html", {"request": request}
    )

  
@app.post("/fiche_animal", response_class=HTMLResponse)
async def predict(
    request: Request,
    file: UploadFile = File(...),
    date: str = Form(...),
    heure: str = Form(...),
    localisation: str = Form(...),
    consent: str = Form(...)
):
    # Vérification stricte du type MIME
    if not allowed_file(file.filename):
        return templates.TemplateResponse(
            "scan.html",
            {
                "request": request,
                "error": (
                    "Format de fichier non accepté. Veuillez télécharger "
                    "une image au format "
                    "JPG, JPEG, PNG, WEBP ou HEIC."
                )
            }
        )

    # Sauvegarde du fichier
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Ouverture et prétraitement de l'image
        img = Image.open(file_path).convert("L")
        img = img.resize((128, 128))
        img_array = np.array(img)
        img_array = img_array.reshape(1, 128, 128, 1) / 255.0

        # Prédiction
        predictions = model.predict(img_array)
        predicted_index = int(np.argmax(predictions[0]))
        predicted_class = classes[predicted_index]

        confidence = predictions[0][predicted_index]
        if confidence < 0.2:  # seuil de confiance
            return RedirectResponse(
                request.url_for("scan_oops_pas_trouve"), status_code=303
            )

        db = SessionLocal()
        try:
            animal_info = db.query(Especes).filter(
                Especes.espece == predicted_class
            ).first()
            if not animal_info:
                return RedirectResponse(
                    request.url_for("scan_oops_pas_trouve"), status_code=303
                )

            # Enregistrement des métadonnées
            new_photo = PhotosUtilisateurs(
                chemin_fichier=file_path,
                date=date,
                heure=heure,
                localisation=localisation,
                espece=predicted_class
            )
            db.add(new_photo)
            db.commit()

            return templates.TemplateResponse(
                "fiche_animal.html",
                {
                    "request": request,
                    "animal_info": animal_info,
                    "uploaded_image_url": "/" + file_path.replace("\\", "/")
                }
            )
        finally:
            db.close()

    except Exception as e:
        print(f"Error: {e}")
        return RedirectResponse(
            request.url_for("scan_oops_pas_trouve"), status_code=303
        )
