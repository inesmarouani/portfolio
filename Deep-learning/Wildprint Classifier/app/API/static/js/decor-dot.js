(function(){
  // Récupère le conteneur des points décoratifs
  const container = document.getElementById('decorDots');
  if(!container) return; // Arrête si le conteneur n'existe pas

  // Configuration des points
  const CONFIG = {
    minSize: 35, // Taille minimale d'un point
    maxSize: 105, // Taille maximale d'un point
    colors: ['#FFD505','#C7A0FB','#31C48D'], // Couleurs possibles
    avoidPadding: 40, // Distance à éviter autour des éléments marqués
    maxAttemptsPerDot: 40 // Nombre d'essais pour placer un point sans chevaucher
  };

  // Détermine le nombre de points selon la page affichée
  const page = window.location.pathname.split('/').pop();
  const countsByPage = {
    'fiche_animal.html': 6,
    'index.html': 10,
    'exploration.html': 6,
    'scan.html': 8
  };
  CONFIG.count = countsByPage[page] || 6; // Valeur par défaut si la page n'est pas listée

  // Fonction utilitaire pour générer un nombre aléatoire entre a et b
  const rand = (a,b) => a + Math.random()*(b-a);

  // Récupère les rectangles des éléments à éviter (ceux avec l'attribut data-decor-avoid)
  function getAvoidRects(containerRect){
    const nodes = document.querySelectorAll('[data-decor-avoid]');
    return Array.from(nodes)
      .filter(n => n.getBoundingClientRect)
      .map(n => {
        const r = n.getBoundingClientRect();
        // Calcule la position relative à celle du conteneur
        return {
          left: r.left - containerRect.left,
          top: r.top - containerRect.top,
          right: r.right - containerRect.left,
          bottom: r.bottom - containerRect.top
        };
      });
  }

  // Vérifie si un point (x, y) est à l'intérieur d'un rectangle, avec un padding optionnel
  function rectContains(rect, x, y, pad=0){
    return x >= (rect.left - pad) && x <= (rect.right + pad) &&
           y >= (rect.top - pad)  && y <= (rect.bottom + pad);
  }

  // Vérifie si un point est à l'intérieur de l'un des rectangles à éviter
  function isInsideAnyAvoid(x, y, avoidRects, pad){
    return avoidRects.some(r => rectContains(r, x, y, pad));
  }

  // Fonction principale pour créer et placer les points
  function createDots(){
    container.innerHTML = ''; // Vide le conteneur avant de placer les points
    const contRect = container.getBoundingClientRect();
    if(contRect.width === 0 || contRect.height === 0) return; // Arrête si le conteneur est invisible

    const avoidRects = getAvoidRects(contRect); // Récupère les zones à éviter

    // Pour garantir que chaque couleur apparaisse au moins une fois
    const colorsToUse = [];
    CONFIG.colors.forEach(c => colorsToUse.push(c));
    while(colorsToUse.length < CONFIG.count){
      colorsToUse.push(CONFIG.colors[Math.floor(Math.random()*CONFIG.colors.length)]);
    }
    // Mélange les couleurs
    colorsToUse.sort(() => Math.random() - 0.5);

    // Calcule le nombre de colonnes et de lignes pour répartir les points en grille
    const cols = Math.ceil(Math.sqrt(CONFIG.count));
    const rows = Math.ceil(CONFIG.count / cols);
    let placed = 0;

    // Parcourt chaque cellule de la grille pour placer les points
    for(let r=0; r<rows && placed<CONFIG.count; r++){
      for(let c=0; c<cols && placed<CONFIG.count; c++){
        let attempts = 0, x, y, size;

        // Essaie de placer le point sans chevaucher les zones à éviter
        do {
          size = Math.round(rand(CONFIG.minSize, CONFIG.maxSize));
          const cellWidth = contRect.width / cols;
          const cellHeight = contRect.height / rows;

          // Position aléatoire dans la cellule
          x = c*cellWidth + rand(size/2, cellWidth - size/2);
          y = r*cellHeight + rand(size/2, cellHeight - size/2);

          attempts++;
        } while(
          isInsideAnyAvoid(x, y, avoidRects, CONFIG.avoidPadding) &&
          attempts < CONFIG.maxAttemptsPerDot
        );

        // Crée l'élément point
        const dot = document.createElement('span');
        dot.className = 'dot';

        // Attribue la couleur et la position
        const color = colorsToUse[placed];
        const leftPct = (x / contRect.width) * 100;
        const topPct  = (y / contRect.height) * 100;

        dot.style.width  = size + 'px';
        dot.style.height = size + 'px';
        dot.style.left   = leftPct + '%';
        dot.style.top    = topPct + '%';
        dot.style.backgroundColor = color;

        container.appendChild(dot); // Ajoute le point au conteneur
        placed++;
      }
    }
  }

  // Régénère les points lors du redimensionnement de la fenêtre (avec un délai pour éviter trop d'appels)
  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(createDots, 150);
  });

  // Génère les points au chargement
  createDots();
})();
