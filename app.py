
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Charger les données
def load_data(file_path):
    """Charger les données d'entraînement à partir d'un fichier CSV."""
    data = pd.read_csv(file_path)
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    workout_data = load_data('workout_data.csv')
    filtered_workouts = workout_data

    if request.method == 'POST':
        target_area = request.form.get('target_area')
        difficulty = request.form.get('difficulty')

        # Filtrer les données
        if target_area:
            filtered_workouts = filtered_workouts[filtered_workouts['Zone cible'] == target_area]
        if difficulty:
            filtered_workouts = filtered_workouts[filtered_workouts['Difficulté'] == difficulty]

    return render_template('index.html', workouts=filtered_workouts)

if __name__ == '__main__':
    app.run(debug=True)