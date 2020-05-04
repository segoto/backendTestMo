from .logic.logic_pokemon import get_all_pokemon, get_pokemon, get_evolutions, get_all_base_stat, get_all_base_stats
from django.http import HttpResponse
from django.core import serializers
from .filter import PokemonSearchForm
from django.shortcuts import render


def get_pokemons(request):
    pokemons = get_all_base_stats()
    pokemons_list = serializers.serialize('json', pokemons)
    return HttpResponse(pokemons_list, content_type='application/json')


def search(request):
    return render(request, 'pokemon/searchForm.html')


def pokemon_searched(request):
    try:
        name = request.GET.get('name')
        pokemon = get_pokemon(name)
        evolutions = get_evolutions(pokemon.name)
        base_stats = get_all_base_stat(pokemon.name)
        context = {'pokemon': pokemon, 'evolutions': evolutions, 'base_stats': base_stats}
        return render(request, 'pokemon/PokemonSearchResult.html', context)
    except:
        return render(request, 'pokemon/pokemonNotFound.html')







