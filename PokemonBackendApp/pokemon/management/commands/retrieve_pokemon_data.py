from django.core.management.base import BaseCommand, CommandError
from pokemon.models import Pokemon
from pokemon.models import Evolution
from pokemon.models import BaseStat
import requests


class Command(BaseCommand):
    help = 'retrieving data from pokemon api'

    def add_arguments(self, parser):
        parser.add_argument('evolution_chains_id', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        evolution_chains = kwargs['evolution_chains_id']
        get_evolution_chain(evolution_chains)


def get_pokemon_details(name):
    url = 'http://pokeapi.co/api/v2/pokemon/' + name
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        return payload


def get_evolution_chain(identification):
    url = 'https://pokeapi.co/api/v2/evolution-chain/' + str(identification[0])
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        chain = []
        name_poke = payload.get('chain').get('species').get('name')
        evolutions = payload.get('chain').get('evolves_to')
        pokemon = {'name': name_poke, 'evolutions': evolutions}
        chain.append(pokemon['name'])
        while len(evolutions):
            name_poke = pokemon['evolutions'][0]['species']['name']
            evolutions = pokemon['evolutions'][0]['evolves_to']
            pokemon = {'name': name_poke, 'evolutions': evolutions}
            chain.append(name_poke)
        pokemon_details = []
        for i in range(len(chain)):
            pokemon_details.append(get_pokemon_details(chain[i]))

        for i in range(len(pokemon_details)):
            identification = pokemon_details[i].get('id')
            name_poke = chain[i]
            height_poke = pokemon_details[i].get('height')
            weight_poke = pokemon_details[i].get('weight')
            stats = pokemon_details[i].get('stats')
            print(name_poke)
            x ={'pokemon': identification, 'name': name_poke, 'height': height_poke, 'weight': weight_poke}
            adding_pokemon = Pokemon(**x)
            adding_pokemon.save()
            for j in range(len(stats)):
                base_stat_poke = stats[j]['base_stat']
                base_stat_name = stats[j]['stat']['name']
                adding_base_stat = BaseStat(name=base_stat_name, base_stat=base_stat_poke, pokemon=adding_pokemon)
                adding_base_stat.save()

            for j in range(len(pokemon_details)):
                if i != j:
                    evolution_name = chain[j]
                    evolution_id = pokemon_details[j].get('id')
                    evolution_type_poke = 'preevolution' if j < i else 'evolution'
                    adding_evolution = Evolution(name=evolution_name, pokemon_identification=evolution_id, evolution_type=evolution_type_poke, pokemon_from_identification=adding_pokemon)
                    adding_evolution.save()
