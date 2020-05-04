from django import forms
from .models import Pokemon


class PokemonSearchForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            'name'
        ]
        labels = {
            'name': 'Nombre',
        }