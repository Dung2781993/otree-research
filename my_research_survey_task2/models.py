from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'task2'
    players_per_group = None
    num_rounds = 1
#    pair = random.sample(['chocolate','vanilla','strawberry','coffee','banana','walnut'],2)
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    first_choice=models.IntegerField(initial=0)
    second_choice=models.IntegerField(initial=0)
    temp = models.IntegerField(initial=0)


class Player(BasePlayer):
    #Kind of flavour for player to rank
    chocolate = models.IntegerField(choices=[1,2,3,4,5,6],)
    vanilla = models.IntegerField(choices=[1,2,3,4,5,6],)
    strawberry = models.IntegerField(choices=[1,2,3,4,5,6],)
    coffee = models.IntegerField(choices=[1,2,3,4,5,6],)
    banana = models.IntegerField(choices=[1,2,3,4,5,6],)
    walnut = models.IntegerField(choices=[1,2,3,4,5,6],)
    
    is_satisfied = models.BooleanField()
    is_matching = models.BooleanField()
    
    first_choice = models.IntegerField(initial=0)
    second_choice = models.IntegerField(initial=0)
    
    def random_compare(self):
        pair = random.sample([self.player.chocolate,self.player.vanilla,self.player.strawberry,self.player.coffee,self.player.banana,self.player.walnut],2) 
        return pair
