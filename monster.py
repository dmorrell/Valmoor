import random
import shlex
import player

    
class Monster(player.Player):
    def __init__(self, location, name, character, description, status, hp, armor_class, attack_class, strength, dexterity, load, maxload, wanderer):
        player.Player.__init__(self, location)
        self.name = str.lower(name)
        self.character = character
        self.description = description
        self.status = status
        self.hp = hp
        self.armor_class = armor_class
        self.attack_class = attack_class
        self.strength = strength
        self.dexterity = dexterity
        self.load = load
        self.maxload = maxload
        self.wanderer = wanderer
        self.team = "monster"
        self.location.players_here.append(self)
    
        
    def get_input(self):

        if not self.playing:
            return ""

#  Add taskLoopingCall to have mosnters wander every couple of minutes
#
#        elif self.wanderer:
#            exit_options = ['up', 'down', 'north', 'south', 'east', 'west']
#            result = "go "
#            result += exit_options[random.randint(0,5)]
#            return result
        else:
            return ""

    def send_results(self):
        pass

    def update(self):
        if not self.playing:
            return ""

        self.result = self.process_input(self.input)

        human_check = [x for x in self.location.players_here if x.character == "human" and x.playing]
#     if a monster(s) is in the room, add them to the fight list to be attacked
        if human_check:
            for x in human_check:
                if x not in self.fight_list:
                    self.fight_list.append(x)
# check to see if there is anything in our fight list, if so, attack it                              
        if self.fight_list:
            enemy = self.fight_list[0]
            self.events += enemy.do_kill(self)

 
        


    def look(self, player, noun):
        return [self.description]

    def get(self, player, noun):
        if self.status == "DEAD":
            return ["Ugh, why would you want to pick up a " + self.name + "?"]
        else:
            return ["The " + self.name + " growls at you!"]
    
    actions = ['look', 'get', 'kill']
    


  
    

    
