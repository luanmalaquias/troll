from apptheyrdead.brain.entidade import randomizarEntidade
from apptheyrdead.brain import *
from django.db import models

class Entidade(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="name")
    gen = models.CharField(max_length=50, null=False, blank=False, verbose_name="gen")
    entity_class = models.CharField(max_length=50, null=False, blank=False, verbose_name="entity class")
    age = models.IntegerField(null=False, blank=False, verbose_name="age")
    totalPoints = models.IntegerField(null=False, blank=False, verbose_name="total points")
    level = models.IntegerField(null=False, blank=False, verbose_name="level")
    strength = models.IntegerField(null=False, blank=False, verbose_name="strength")
    constitution = models.IntegerField(null=False, blank=False, verbose_name="constitution")
    dexterity = models.IntegerField(null=False, blank=False, verbose_name="dexterity")
    intelligence = models.IntegerField(null=False, blank=False, verbose_name="intelligence")
    wisdom = models.IntegerField(null=False, blank=False, verbose_name="wisdom")
    charisma = models.IntegerField(null=False, blank=False, verbose_name="charisma")

    def __str__(self):
        return str(f'{self.name}, {self.entity_class}')

def refreshEntity(tipo, sorte):    
    entidadeBanco = getOrCreateEntity()

    if tipo == "human":
        entidadeCriada = randomizarEntidade("human", sorte)
    elif tipo == "weak":
        entidadeCriada = randomizarEntidade("weak", sorte)
    elif tipo == "strong":
        entidadeCriada = randomizarEntidade("strong", sorte)
    
    entidadeBanco.name = entidadeCriada[0]
    entidadeBanco.gen = entidadeCriada[1]
    entidadeBanco.entity_class = entidadeCriada[2]
    entidadeBanco.age =  entidadeCriada[3]
    entidadeBanco.totalPoints =  entidadeCriada[4]
    entidadeBanco.level =  entidadeCriada[5]
    entidadeBanco.strength =  entidadeCriada[6]
    entidadeBanco.constitution =  entidadeCriada[7]
    entidadeBanco.dexterity =  entidadeCriada[8]
    entidadeBanco.intelligence =  entidadeCriada[9]
    entidadeBanco.wisdom =  entidadeCriada[10]
    entidadeBanco.charisma =  entidadeCriada[11]

    entidadeBanco.save()


def zerar():
    entidade = Entidade.objects.get(pk=1)
    entidade.name = ""
    entidade.gen = ""
    entidade.entity_class = ""
    entidade.age = 0
    entidade.totalPoints = 0
    entidade.level = 0
    entidade.strength = 0
    entidade.constitution = 0
    entidade.dexterity = 0
    entidade.intelligence = 0
    entidade.wisdom = 0
    entidade.charisma = 0
    entidade.save()

def getOrCreateEntity():
    query = Entidade.objects.all()
    if len(query) == 0:
        entidadeBanco = Entidade(
            name="", 
            gen="", 
            entity_class="", 
            age=0, 
            totalPoints=0, 
            level=0, 
            strength=0, 
            constitution=0, 
            dexterity=0, 
            intelligence=0, 
            wisdom=0, 
            charisma=0
        )
        entidadeBanco.save()
    entidadeBanco = Entidade.objects.get(pk=1)
    return entidadeBanco