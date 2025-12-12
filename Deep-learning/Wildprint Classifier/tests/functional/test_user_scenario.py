# Test complet comme si un utilisateur utilisait le site.

from fastapi.testclient import TestClient
from app.API.app import app

client = TestClient(app)

def test_user_uploads_image_and_gets_result():
    with open("tests/test_images/empreinte_chien.jpg", "rb") as img:
        response = client.post(
            "/fiche_animal",
            data={
                "date": "2025-09-01",
                "heure": "11:00",
                "localisation": "Forêt des pins",
                "consent": "oui"
            },
            files={"file": ("empreinte_chien.jpg", img, "image/jpeg")}
        )

    # Vérifie qu'on a une réponse cohérente
    assert response.status_code in [200, 303]
    assert "html" in response.text.lower()
