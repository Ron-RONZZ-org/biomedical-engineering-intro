# L'Ingénierie Biomédicale — Introduction

Présentation de ~9 minutes destinée à des étudiants en ingénierie francophones (niveau CEC-6).

## Structure du dépôt

```
├── slides/
│   └── index.html            # Diaporama reveal.js (ouvrir dans un navigateur)
├── diagrams/
│   ├── interdisciplinary.puml        # Carte mentale interdisciplinaire
│   ├── medical-device-pipeline.puml  # Pipeline de développement d'un dispositif médical
│   └── personalized-medicine.puml    # Flux de médecine personnalisée / jumeau numérique
├── visualizations/
│   ├── generate_charts.py    # Script Python (seaborn) pour générer les graphiques
│   ├── market_segments.png   # Segments du marché mondial (2023)
│   ├── biomaterials_breakdown.png  # Répartition des types de biomatériaux
│   └── growth_projection.png       # Projection de croissance 2018-2030
├── script.md                 # Script d'accompagnement (points clés + punchlines)
└── reading-list.md           # Liste de ressources pour approfondir
```

## Utilisation

### Diaporama

Ouvrir `slides/index.html` dans un navigateur moderne (Chrome, Firefox, Edge).  
Une connexion Internet est requise pour charger :
- **reveal.js** (CDN jsDelivr)
- Les **diagrammes PlantUML** (serveur plantuml.com)

Navigation : flèches ← → ou espace · Plein écran : `F` · Vue d'ensemble : `O`

### Régénérer les graphiques

```bash
pip install seaborn matplotlib numpy
python3 visualizations/generate_charts.py
```

### Modifier les diagrammes PlantUML

Les sources `.puml` se trouvent dans `diagrams/`. Pour regénérer les images :

```bash
# Via le serveur en ligne
# Encoder le fichier source sur https://www.plantuml.com/plantuml/uml/
# ou utiliser l'extension VS Code PlantUML

# Via Java (local)
java -jar plantuml.jar diagrams/*.puml
```

## Thèmes abordés

- Applications de l'ingénierie dans la médecine (dispositifs médicaux, prothèses, imagerie)
- Biomatériaux et leurs applications dans le corps humain
- Modélisation et simulation pour la médecine personnalisée

## Sources principales

Ratner *et al.* (2020) · Enderle & Bronzino (2012) · Nature Biomedical Engineering · GlobalData 2024 · OMS
