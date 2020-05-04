from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.get_pokemons, name='pokemonList'),
    path('search/', views.search, name='searchPokemon'),
    path('searchResult/', views.pokemon_searched, name='pokemonEncontrado')
]
