import random

class Punch:
    name = 'punch'
    pwr = 40
    type = 'attack'
    element = 'normal'

class Bulbosaur:
    name = 'bulbosaur'
    lvl = 1
    spd = 2
    health = 10 + (lvl * 1.7)
    attacks = [Punch]
    type = 'pokemon'
    element = 'grass'

class Charizard:
    name = 'charizard'
    lvl = 1
    spd = 3
    health = 10 + (lvl * 1.7)
    attacks = [Punch]
    type = 'pokemon'
    element = 'fire'

class Squirtle:
    name = 'squirtle'
    lvl = 1
    spd = 1
    health = 10 + (lvl * 1.7)
    attacks = [Punch]
    type = 'pokemon'
    element = 'water'

#currency
crncy = 100
#all pokemon
pokemon_ls = [Bulbosaur, Charizard, Squirtle]
#array for pokemon you have
pokemon_inv = []

npc_names = ['Jerry', 'Alice', 'John', 'Jerome', 'Napoleon']

def starter_pokemon():
    a = input("Pick your starter pokemon: bulbosaur, charizard, or squirtle ")
    if a == Bulbosaur.name:
        pokemon_inv.append(Bulbosaur)
        print("your starter is " + pokemon_inv[0].name)

starter_pokemon()

#function for when 'player' (you) fights the npc
def npc_fight():
    rndm_npc = random.choice(npc_names)
    print(rndm_npc + ' challenges you to a fight!')
    x = input("what would you like to do? - fight-- ")
    if x == 'fight':
        rndm_npc_pkmn = random.choice(pokemon_ls)
        print(rndm_npc + " threw out " + rndm_npc_pkmn.name)
        p1_starter_health = pokemon_inv[0].health
        npc_health = rndm_npc_pkmn.health
        #actual fighting
        while p1_starter_health > 0:
            npc_attacks = random.choice(rndm_npc_pkmn.attacks)
            p1_starter_health = round(p1_starter_health * npc_attacks.pwr/100)
            print("bulbosaur's health: " + str(p1_starter_health))
            if p1_starter_health < 1:
                print("you lost!")
                break
            npc_health = round(npc_health * pokemon_inv[0].attacks[0].pwr/100)
            print(rndm_npc + "'s health: " + str(npc_health))
            if npc_health < 1:
                print("you won!")
                break

npc_fight()
