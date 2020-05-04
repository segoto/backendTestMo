from django.db import models

# Create your models here.


class Pokemon(models.Model):
    pokemon = models.IntegerField()
    name = models.CharField(max_length=70, primary_key=True)
    height = models.FloatField()
    weight = models.FloatField()
    @classmethod
    def create(cls, identification, name, height,weight):
        pokemon = cls(pokemon_identification=identification, name=name, height=height, weight=weight)
        return pokemon


class BaseStat(models.Model):
    name = models.CharField(max_length=70)
    base_stat = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    @classmethod
    def create(cls, name, base_stat, pokemon):
        base_stat_new = cls(name=name, base_stat=base_stat, pokemon=pokemon)
        return base_stat_new


class Evolution(models.Model):
    evolution_type = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    pokemon_identification = models.IntegerField()
    pokemon_from_identification = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    @classmethod
    def create(cls, evolution_type, name, pokemon_identification, pokemon_from_identification):
        evol = cls(evolution_type=evolution_type, name=name, pokemon_identification=pokemon_identification, pokemon_from_identification=pokemon_from_identification)
        return evol
