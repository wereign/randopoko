from flask import Flask
import pokebase as pb
import random
from flask_sqlalchemy import SQLAlchemy


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

db.create_all()


class PokemonDB:
    def create_pokemons(self, number):
        for i in range(number):

            id_pokemon = random.randint(1, 300)
            tmp_pokemon = pb.sprite("pokemon", id_pokemon)

            pokemon_name = pb.pokemon(id_pokemon).name
            pokemon_img = tmp_pokemon.url
            print(pokemon_name,pokemon_img)

            pokemon = Pokemon(name=pokemon_name,img_url=pokemon_img)
            db.session.add(pokemon)
        db.session.commit()