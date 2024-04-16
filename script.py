from flask import Flask

# Crée une instance de l'application Flask
app = Flask(__name__)

# Route principale
@app.route('/')
def index():
    return 'Hello, World!'

# Route pour une page spécifique
@app.route('/about')
def about():
    return 'About page'

# Exécute l'application Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
