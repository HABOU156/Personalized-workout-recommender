# workout_recommender.py

import pandas as pd

def load_data(file_path):
    """Charger les données d'entraînement à partir d'un fichier CSV."""
    data = pd.read_csv(file_path)
    print("Colonnes disponibles :", data.columns)  # Affiche les colonnes
    print("Aperçu des données :", data.head())  # Affiche les premières lignes
    return data

def filter_data(data, target_area=None, difficulty=None):
    """Filtrer les données d'entraînement en fonction de la zone cible et de la difficulté."""
    if target_area:
        print("Valeurs uniques dans 'Zone cible' :", data['Zone cible'].unique())  # Affiche les valeurs uniques
        data = data[data['Zone cible'] == target_area]
    if difficulty:
        print("Valeurs uniques dans 'Difficulté' :", data['Difficulté'].unique())  # Affiche les valeurs uniques
        data = data[data['Difficulté'] == difficulty]
    return data

# Exemple d'utilisation
if __name__ == "__main__":
    # Charger les données
    workout_data = load_data('workout_data.csv')
    
    # Filtrer les données (exemple : cibler les jambes avec une difficulté intermédiaire)
    filtered_workouts = filter_data(workout_data, target_area='Jambes', difficulty='Facile')
    print(filtered_workouts)