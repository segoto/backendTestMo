from ..models import Pokemon, Evolution, BaseStat


def get_all_pokemon():
    pokemons = Pokemon.objects.all()
    return pokemons


def get_all_evolutions():
    evolutions = Evolution.objects.all()
    return evolutions


def get_all_base_stat(i):
    base_stats = BaseStat.objects.all().filter(pokemon=i)
    return base_stats


def get_pokemon(name):
    print(name)
    pokemon = Pokemon.objects.all().get(name=name)
    print(type(pokemon))
    return pokemon


def get_evolutions(i):
    evolutions = Evolution.objects.all().filter(pokemon_from_identification=i)
    return evolutions

def get_all_base_stats():
    base_stat = BaseStat.objects.all()
    return base_stat
