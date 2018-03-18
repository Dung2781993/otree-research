from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass

class Flavours(Page):
    #define form field
    #include class player and its attribute as exact name
    form_model = 'player'
    form_fields = ['apple_pie','salted_coconut_and_mango_salsa','milk_chocolate_with_choc_peanut_fudge','poached_figs_in_marsala','pear_and_rhubarb','lemon']
	
class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Final(Page):
    def vars_for_template(self):
        #checking player used all number or not
        if (self.player.apple_pie + self.player.salted_coconut_and_mango_salsa + self.player.milk_chocolate_with_choc_peanut_fudge + self.player.poached_figs_in_marsala + self.player.pear_and_rhubarb + self.player.lemon) == 21:
            self.player.is_satisfied = True
        else:
            self.player.is_satisfied = False
        
        
        flavour = {'apple pie':self.player.apple_pie,
                   'salted coconut and sango salsa': self.player.salted_coconut_and_mango_salsa,
                   'milk chocolate with choc peanut fudge': self.player.milk_chocolate_with_choc_peanut_fudge,
                   'poached figs in marsala': self.player.poached_figs_in_marsala,
                   'pear and rhubarb': self.player.pear_and_rhubarb,
                   'lemon': self.player.lemon
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



page_sequence = [
    MyPage,
    Flavours,
    ResultsWaitPage,
    Final,
    ResultsWaitPage,
    Results
]
