import player, random, caves
from string import ascii_letters
from twisted.internet.protocol import ServerFactory
from twisted.conch.telnet import StatefulTelnetProtocol
from twisted.internet import reactor, task
#from mud_server import MudProtocol

class Soldier(player.Player):
    def __init__(self, team, location, name, description, status, hp, armor_class, attack_class, strength, dexterity, wanderer):
        player.Player.__init__(self, location)
        self.name = name
        self.character  = "soldier"
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
        self.wallet = 0
        self.location.players_here.append(self)
   


    def get_input(self):

        if self.input_list:
            return self.input_list.pop()
              
        else:
            return ""     #if no one to fight, return nothing      

    def send_results(self):
        pass

    def update(self):

        if not self.playing:
            return ""

        self.result = self.process_input(self.input)

 #       monster_check = [x for x in self.location.players_here if x.character == "monster" and x.playing]
#     if a monster(s) is in the room, add them to the fight list to be attacked
#        if monster_check:
#            for x in monster_check:
#                if x not in self.fight_list:
#                    self.fight_list.append(x)

        enemy_check = [x for x in self.location.players_here if (x.character == "human" and x.playing and (self.team != x.team))]
#     if a enemy is in the room, add them to the fight list to be attacked
        if enemy_check:
            for x in enemy_check:
                if x not in self.fight_list:
                    self.fight_list.append(x)
 #           warning = "We have intruders at the " + self.location.name
#            self.shout(player, warning)
                    
# check to see if there is anything in our fight list, if so, attack it                              
        if self.fight_list:
            enemy = self.fight_list[0]
            self.events += enemy.do_kill(self)

 
    

    actions = ['myteam','help', 'quit', 'describe', 'say', 'shout','inv', 'get', 'drop', 'drink', 'stats', 'kill', 'flee', 'open', 'close', 'unlock', 'sleep', 'wield', 'unwield', 'wear', 'remove']

    
