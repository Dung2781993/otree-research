from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_research_survey_task3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    first_choice=models.IntegerField(initial=0)
    second_choice=models.IntegerField(initial=0)
    temp = models.IntegerField(initial=0)


class Player(BasePlayer):
    #Kind of flavour for player to rank
    apple_pie = models.IntegerField(choices=[1,2,3,4,5,6],)
    salted_coconut_and_mango_salsa = models.IntegerField(choices=[1,2,3,4,5,6],)
    milk_chocolate_with_choc_peanut_fudge = models.IntegerField(choices=[1,2,3,4,5,6],)
    poached_figs_in_marsala = models.IntegerField(choices=[1,2,3,4,5,6],)
    pear_and_rhubarb = models.IntegerField(choices=[1,2,3,4,5,6],)
    lemon = models.IntegerField(choices=[1,2,3,4,5,6],)
    
    is_satisfied = models.BooleanField()
    is_matching = models.BooleanField()
    
    first_choice = models.IntegerField(initial=0)
    second_choice = models.IntegerField(initial=0)
