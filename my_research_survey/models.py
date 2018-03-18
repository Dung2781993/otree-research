from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'NGOC DUNG LE'

doc = """
My Research Survey
"""


class Constants(BaseConstants):
    name_in_url = 'my_simple_survey'
    players_per_group = None
    num_rounds = 1
    
    start_point = c(150)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    #this function is used for matching with teacher
    #it is in testing state
    #It works base on passing the player's chosen after flavour page run
    #But it is not working now
    def set_pay_amount(self):
        matcher = self.get_player_by_role('Student')
        header = self.gett_player_by_role('Teacher')
        if (matcher.chocolate + matcher.vanilla + matcher.stawberry + matcher.coffee + matcher.banana + matcher.walnut) == 6: 
            matcher.is_satisfied = True
        else:
            matcher.is_satisfied = False
        for player in [matcher]:
            if player.is_satisfied:
                player.payoff += Constants.start_point



class Player(BasePlayer):
    
    chocolate = models.IntegerField(choices=[1,2,3,4,5,6],)
    vanilla = models.IntegerField(choices=[1,2,3,4,5,6],)
    strawberry = models.IntegerField(choices=[1,2,3,4,5,6],)
    coffee = models.IntegerField(choices=[1,2,3,4,5,6],)
    banana = models.IntegerField(choices=[1,2,3,4,5,6],)
    walnut = models.IntegerField(choices=[1,2,3,4,5,6],)

    is_satisfied = models.BooleanField()