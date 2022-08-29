import pokebase as pb
import random
squirtle = pb.pokemon(35)
print(dir(squirtle))
# print(dir(squirtle.abilities[0]))
# print(dir(squirtle.sprites))
print(squirtle.name)
for ability in squirtle.abilities:
    print(ability.ability)

# for i in range(10):
#     id_pokemon = random.randint(1,300)
    # tmp_pokemon = pb.sprite("pokemon",id_pokemon)
    # print(tmp_pokemon.url)

print(squirtle)