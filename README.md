# backendTestMo
Create a Django command that retrieves data from pokeapi.co and stores it in a local database. In additon, you may find information about the pokemon.

## Running instructions
1. clone the repository.
2. access to the PokemonBackendApp
3. run pip install -r requirements.txt
4. run python manage.py makemigrations
5. run python manage.py migrate
6. run python manage.py retrieve_pokemon_data {insert number of a valid pokemon chain, 10 is pichu, pikachu, raichu for example}
7. run python manage.py runserver 0.0.0.0:8000
