# Personalized Workout Recommender
**Description**
L'application Personalized Workout Recommender est une interface web simple développée avec Flask qui permet aux utilisateurs de filtrer des exercices d'entraînement en fonction de la zone cible et du niveau de difficulté. Les données des exercices sont chargées à partir d'un fichier CSV, ce qui permet une gestion facile et flexible des exercices.
**Fonctionnalités**
-Chargement des données d'exercices à partir d'un fichier CSV.
-Filtrage des exercices par zone cible (Pectoraux, Jambes, Dos, Abdominaux).
-Filtrage des exercices par niveau de difficulté (Facile, Intermédiaire).
-Affichage des exercices recommandés dans un tableau.
**Prérequis**
Python 3.x
Flask
Pandas
**Installation**
1. Clonez le dépôt :
```   git clone <URL_DU_DEPOT>
   cd Personalized-workout-recommender
2. Installez les dépendances :
Assurez-vous d'avoir pip installé, puis exécutez :
```   pip install Flask pandas
3.Préparez le fichier CSV :
Assurez-vous que le fichier workout_data.csv est présent dans le répertoire du projet. Vous pouvez utiliser le format suivant pour le fichier CSV :
```    Exercise,Zone cible,Equipment Required,Difficulté,Reps,Sets,Duration
   Pompes,Pectoraux,Poids du corps,Facile,10,3,30s
   Squats,Jambes,Aucun,Facile,15,3,30s
   Soulevé de terre,Dos,Barre,Intermédiaire,8,4,60s
   Développé couché,Pectoraux,Barre,Intermédiaire,10,3,60s
   Tirage horizontal,Dos,Machine,Intermédiaire,12,3,45s
   Fentes,Jambes,Aucun,Facile,10,3,30s
   Planche,Abdominaux,Poids du corps,Facile,30s,3,30s
   Crunchs,Abdominaux,Aucun,Facile,15,3,30s
**Utilisation**
1.Lancez l'application :
```   python app.py
2. Accédez à l'application :
Ouvrez votre navigateur et allez à http://127.0.0.1:5000.
3. Filtrer les exercices :
    -Sélectionnez une zone cible et un niveau de difficulté dans les menus déroulants.
    -Cliquez sur le bouton "Filtrer" pour afficher les exercices correspondants.
**Contribuer**
Les contributions sont les bienvenues ! Si vous souhaitez améliorer cette application, n'hésitez pas à soumettre une demande de tirage (pull request).
**License**
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
