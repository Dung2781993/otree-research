from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass

class Flavours(Page):
    form_model = 'player'
    form_fields = ['chocolate','vanilla','strawberry','coffee','banana','walnut']
    
    
class ResultsWaitPage(WaitPage):
    pass

#Calculation class is for group playing game
#It is in testing state
class Calculation(Page):
    def after_all_players_arrive(self):
        self.group.set_pay_amout()

class Results(Page):
    
    def vars_for_template(self):
        if (self.player.chocolate + self.player.vanilla + self.player.strawberry + self.player.coffee + self.player.banana + self.player.walnut) == 21:
            self.player.payoff += 150
            self.player.is_satisfied = True
        else:
            self.player.is_satisfied = False
        return {
                'total_payoff':self.player.payoff,
                }
                

#include ResultsWaitPage for more complex and multi-player games
page_sequence = [
    MyPage,
    Flavours,
    Results
]
