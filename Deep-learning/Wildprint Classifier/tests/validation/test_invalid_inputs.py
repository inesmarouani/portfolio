# Ce test vérifie le comportement du endpoint /fiche_animal lorsqu’un fichier envoyé n’est pas une image.

from fastapi.testclient import TestClient
from app.API.app import app

client = TestClient(app)

def test_invalid_file_format():
    response = client.post(
        "/fiche_animal",
        data={
            "date": "2025-09-01",
            "heure": "12:00",
            "localisation": "Forêt bidon",
            "consent": "oui"
        },
        files={"file": ("fake.txt", b"ceci n'est pas une image", "text/plain")}
    )

    # Doit renvoyer une erreur plutôt qu'une redirection
    assert response.status_code == 400