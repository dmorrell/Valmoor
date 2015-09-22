import player, random, caves
from string import ascii_letters
from twisted.internet.protocol import ServerFactory
from twisted.conch.telnet import StatefulTelnetProtocol
from twisted.internet import reactor, task
#from mud_server import MudProtocol

class Town(player.Player):
    def __init__(self, team, location, name, description, status, hp, armor_class, attack_class, strength, dexterity, wanderer):
        player.Player.__init__(self, location)
        self.name = name
        self.character  = "town"
        self.team = team
        self.description = description
        self.status = "AWAKE"
        self.hp = hp
        self.maxhp = 30
        self.armor_class = armor_class
        self.attack_class = attack_class
        self.strength = strength
        self.dexterity = dexterity
        self.wanderer = wanderer
        self.location.players_here.append(self)
   


    def get_input(self):

        if self.input_list:
            return self.input_list.pop()
              
        else:
            return ""     #if no one to fight, return nothing      

    def send_results(self):
        pass


    def update(self):

        self.result = self.process_input(self.input)

 
# check to see if there is anything in our fight list, if so, attack it                              
        if self.fight_list:
            enemy = self.fight_list[0]
            self.events += enemy.do_kill(self)

 
    

    actions = ['help', 'quit', 'name_', 'describe', 'say', 'shout','inv', 'get', 'drop', 'drink', 'stats', 'kill', 'flee', 'open', 'close', 'unlock', 'sleep', 'wield', 'unwield', 'wear', 'remove']

    
