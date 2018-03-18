from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Flavours(Page):
    form_model = 'player'
    form_fields = ['chocolate','vanilla','strawberry','coffee','banana','walnut']

    

class Results(Page):
    def vars_for_template(self):
        if (self.player.first_choice > self.player.second_choice) and (self.group.temp > 0):
            if self.player.is_satisfied:
                self.player.payoff +=200
            else:
                self.player.payoff +=0
        elif (self.player.first_choice < self.player.second_choice) and (self.group.temp < 0):
            if self.player.is_satisfied:
                self.player.payoff +=200
            else:
                self.player.payoff +=0
        else:
            self.player.payoff +=0
        
        return {
                'total_payoff':self.player.payoff,
                '1st': self.session.config['first_choice'],
                '2nd': self.session.config['second_choice'],
                'all_players': self.player.in_all_rounds(),
                'group_choice': self.group.temp,
                'player_first_choice': self.player.first_choice,
                'player_second_choice': self.player.second_choice,
                }
class Final(Page):
    def vars_for_template(self):
        #checking player used all number or not
        if (self.player.chocolate + self.player.vanilla + self.player.strawberry + self.player.coffee + self.player.banana + self.player.walnut) == 21:
            self.player.is_satisfied = True
        else:
            self.player.is_satisfied = False
        
        
        flavour = {'chocolate':self.player.chocolate,
                   'vanilla': self.player.vanilla,
                   'strawberry': self.player.strawberry,
                   'coffee': self.player.coffee,
                   'banana': self.player.banana,
                   'walnut': self.player.walnut
                   }
        self.player.first_choice = flavour[(self.session.config['first_choice']).lower()]
        self.player.second_choice = flavour[(self.session.config['second_choice']).lower()]
        
        
        if self.player.first_choice > self.player.second_choice:
            self.group.temp +=1
        if self.player.first_choice < self.player.second_choice:
            self.group.temp -=1
        
        return {
                'all_players': self.player.in_all_rounds(),
                'satisfied': self.player.is_satisfied,
                'group_choice': self.group.temp,
                'player_first_choice': self.player.first_choice,
                'player_second_choice': self.player.second_choice,
                }


page_sequence = [
    MyPage,
    Flavours,
    ResultsWaitPage,
    Final,
    ResultsWaitPage,
    Results
]
