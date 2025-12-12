document.addEventListener('DOMContentLoaded', function () {
    const cameraButton = document.getElementById('cameraButton');
    const fileInput = document.getElementById('fileInput');
    const imageMessage = document.getElementById('image-message');

    if (cameraButton) {
        cameraButton.addEventListener('click', async () => {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                const video = document.createElement('video');
                video.srcObject = stream;
                video.play();

                // Créez un conteneur pour la vidéo et le bouton de capture
                const videoContainer = document.createElement('div');
                videoContainer.style.position = 'fixed';
                videoContainer.style.top = '0';
                videoContainer.style.left = '0';
                videoContainer.style.width = '100%';
                videoContainer.style.height = '100%';
                videoContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
                videoContainer.style.zIndex = '1000';
                videoContainer.style.display = 'flex';
                videoContainer.style.flexDirection = 'column';
                videoContainer.style.alignItems = 'center';
                videoContainer.style.justifyContent = 'center';

                video.style.maxWidth = '100%';
                video.style.maxHeight = '80%';

                const captureButton = document.createElement('button');
                captureButton.textContent = 'Prendre une photo';
                captureButton.style.marginTop = '20px';
                captureButton.style.padding = '10px 20px';
                captureButton.style.backgroundColor = '#31C48D';
                captureButton.style.color = 'white';
                captureButton.style.border = 'none';
                captureButton.style.borderRadius = '5px';
                captureButton.style.cursor = 'pointer';

                videoContainer.appendChild(video);
                videoContainer.appendChild(captureButton);
                document.body.appendChild(videoContainer);

                // Ajoutez un bouton pour fermer la caméra sans prendre de photo
                const closeButton = document.createElement('button');
                closeButton.textContent = 'Fermer';
                closeButton.style.marginTop = '10px';
                closeButton.style.padding = '10px 20px';
                closeButton.style.backgroundColor = '#ff4444';
                closeButton.style.color = 'white';
                closeButton.style.border = 'none';
                closeButton.style.borderRadius = '5px';
                closeButton.style.cursor = 'pointer';

                videoContainer.appendChild(closeButton);

                // Fonction pour capturer la photo
                captureButton.addEventListener('click', () => {
                    const canvas = document.createElement('canvas');
                    canvas.width = video.videoWidth;
                    canvas.height = video.videoHeight;
                    const context = canvas.getContext('2d');
                    context.drawImage(video, 0, 0, canvas.width, canvas.height);

                    canvas.toBlob(blob => {
                        const file = new File([blob], "capture.png", { type: "image/png" });
                        const dataTransfer = new DataTransfer();
                        dataTransfer.items.add(file);
                        fileInput.files = dataTransfer.files;
                        stream.getTracks().forEach(track => track.stop());
                        document.body.removeChild(videoContainer);
                        if (imageMessage) {
                            imageMessage.textContent = "Votre image a bien été téléchargée.";
                            imageMessage.style.color = "#31C48D";
                        }
                    }, "image/png");
                });

                // Fonction pour fermer la caméra sans capturer
                closeButton.addEventListener('click', () => {
                    stream.getTracks().forEach(track => track.stop());
                    document.body.removeChild(videoContainer);
                });

            } catch (err) {
                if (imageMessage) {
                    imageMessage.textContent = "Impossible d'accéder à la caméra : " + err;
                    imageMessage.style.color = "#ff4444";
                }
            }
        });
    }

    // Affichage du message de succès ou d'erreur lors de la sélection d'un fichier
    if (fileInput) {
        fileInput.addEventListener('change', function () {
            if (fileInput.files && fileInput.files[0]) {
                const file = fileInput.files[0];
                const validTypes = ["image/jpeg", "image/png", "image/webp", "image/jpg", "image/heic"];
                if (validTypes.includes(file.type)) {
                    if (imageMessage) {
                        imageMessage.textContent = "Votre image a bien été téléchargée.";
                        imageMessage.style.color = "#31C48D";
                    }
                } else {
                    if (imageMessage) {
                        imageMessage.textContent = "Format d'image non supporté.";
                        imageMessage.style.color = "#ff4444";
                    }
                    fileInput.value = "";
                }
            }
        });
    }
});