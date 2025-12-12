# Ce test simule un utilisateur qui upload une image → l’IA prédit → la base de données est mise à jour.

from fastapi.testclient import TestClient
from app.API.app import app
import os

client = TestClient(app)

def test_upload_and_predict_and_db_integration():
    test_image_path = "tests/test_images/empreinte_chien.jpg"

    with open(test_image_path, "rb") as img:
        response = client.post(
            "/fiche_animal",
            data={
                "date": "2025-09-01",
                "heure": "10:30",
                "localisation": "Forêt test",
                "consent": "oui"
            },
            files={"file": ("empreinte_chien.jpg", img, "image/jpeg")}
        )

    # Vérifie que l’utilisateur est redirigé ou voit une fiche
    assert response.status_code in [200, 303]
