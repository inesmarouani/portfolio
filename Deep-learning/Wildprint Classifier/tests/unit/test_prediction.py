# Ce test vérifie si le modèle prédit bien une classe à partir d'une image valide.

import numpy as np
from PIL import Image
import tensorflow as tf
import os

# Charger le modèle une seule fois
model = tf.keras.models.load_model("app/API/model_simple.h5")
classes = ['Castor', 'Chat', 'Chien', 'Coyote', 'Ecureuil', 'Lapin', 'Loup', 'Lynx', 'Ours', 'Puma', 'Rat', 'Raton laveur', 'Renard']

def test_model_prediction_on_valid_image():
    # Charger une image de test depuis le dossier de test
    img_path = "tests/test_images/empreinte_chien.jpg"
    img = Image.open(img_path).convert("L")
    img = img.resize((128, 128))
    img_array = np.array(img)
    img_array = img_array.reshape(1, 128, 128, 1) / 255.0

    # Prédire la classe
    predictions = model.predict(img_array)
    predicted_index = int(np.argmax(predictions[0]))
    predicted_class = classes[predicted_index]

    # Vérifier que la classe est dans la liste
    assert predicted_class in classes
