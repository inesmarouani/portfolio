document.addEventListener("DOMContentLoaded", function () {
  fetch("../components/header.html")
    .then(response => {
      if (!response.ok) {
        throw new Error("Erreur lors du chargement du header.");
      }
      return response.text();
    })
    .then(data => {
      document.getElementById("insert-header").innerHTML = data;
    })
    .catch(error => {
      console.error("Erreur :", error);
    });
});
