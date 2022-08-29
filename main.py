import random
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

# Creating the database.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pokemon.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    # abilities = db.Column(db.String(300), unique=True, nullable=False)
    img_url = db.Column(db.String(300))

pokemons = []

for i in range(1,21):
    pokemon = Pokemon.query.get(i)
    pokemons.append(pokemon)


@app.route("/")
def home():
    return render_template("index.html", pokemons=pokemons,number=len(pokemons))


if __name__ == "__main__":
    app.run(debug=True)