import shlex
import string
import random
import caves
from items import Item
import Valmoor
import factory

    
class Player(object):
    def __init__(self, location):
   
       self.location = location
 #     self.password = " "
 #      self.location.players_here.append(self)
       self.playing = True
       self.inventory = []
       self.events = []
       self.wielding = []
       self.wearing = []
       self.input_list = []
       self.result = []
       self.fight_list = []
       self.wallet = 0
       self.bank = 0


           
    def process_input(self, input):


        parts = shlex.split(input)
       
        if len(parts) ==0:
            return []
        if len(parts) ==1:
            parts.append("")

        verb = parts[0]
        noun = " ".join(parts[1:])

        handler = self.find_handler(verb, noun)
        if handler is None:
            return [input + " ? Huh?"]

 #       print "DEBUG==> process_input"
#        print handler
#        print self
#        print noun
#        print "DEBUG==> process_input"
        return handler(self, noun)

    def find_handler(self, verb, noun):

 #       if verb not in self.actions:
#            return "Don't know how to do that."

        if noun != "":                              # if there is input, check to see if it (player or object) is in this location and the action is valid
       


  # if you found an object they are wielding, return it
 #           print "DEBUG ==> find handler"
#            print noun
#            print verb
#            print self.name
#            print self.location.items_here

            noun = str.lower(noun)
    #        if verb == "buy":
     #           return getattr(self, verb)

      #      if verb == "deposit":
       #         return getattr(self,verb)

            wielding = [x for x in self.wielding
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb == ('unwield')]
 #           print wielding
            if len(wielding) > 0:                     
                return getattr(wielding[0], verb)

   # if you found an object they are wearing, return it
            wearing = [x for x in self.wearing
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb == 'remove']
            if len(wearing) > 0:                    
                return getattr(wearing[0], verb)



  # if you found an object they are carrying, return it *** THIS IS REALLY UGLY. FIGURE OUT BETTER LOGIC
 #           print "inventory"
 #           print self.inventory
            carrying = [x for x in self.inventory
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb == 'wear']
    
            if len(carrying) > 0: 
                return getattr(carrying[0], verb)

   
            carrying = [x for x in self.inventory
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb == 'drink']
           
            if len(carrying) > 0: 
                return getattr(carrying[0], verb)
 
            carrying = [x for x in self.inventory
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb == 'look']
           
            if len(carrying) > 0: 
                return getattr(carrying[0], verb)
      
            carrying = [x for x in self.inventory
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb == 'wield']
          
            if len(carrying) > 0:
 #               print "DEBUG==> find_handler"
 #               print getattr(carrying[0], verb)
                return getattr(carrying[0], verb)

            carrying = [x for x in self.inventory
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb == 'drop']

            if len(carrying) > 0: 
                return getattr(carrying[0], verb)


            carrying = [x for x in self.inventory
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb == 'sell']
          
            if len(carrying) > 0: 
                return getattr(carrying[0], verb)


  # if you found a player in the room, return it 
 #           player = [x for x in self.location.players_here
#                      if x is not self and
#                      str.lower(x.name) == noun and
#                      verb in x.actions]
#            if len(player) > 0:                     
#                return getattr(player[0], verb)

 # if you found an object in the room, return it 
            object = [x for x in (self.location.items_here + self.location.players_here)
                      if x is not self and
                      str.lower(x.name) == noun and
                      verb in x.actions]
 #                     verb == ('get' or 'look' or 'open' or 'close')]
 #           print "items in room"
#            print object
            if len(object) > 0:                     
                return getattr(object[0], verb)


        if verb.lower() in self.actions:              #check to see if player has available actions
            return getattr(self, verb)
        elif verb.lower() in self.location.actions:   #check to see if cave has any actions
            return getattr(self.location, verb)


        
    def get_input(self):

        if self.input_list:
            return self.input_list.pop()
        else:
            return ''   

  
    def send_results(self):

        for line in self.events:
            self.connection.msg_me(line)
        for line in self.result:
            self.connection.msg_me(line) 

    def say(self, player, noun):
        for object in self.location.players_here:
            if ('events' in dir(object) and
                object != self):
                object.events.append(self.name + " says: " + noun)
        return ["You say: " + noun]

    def shout(self, player, noun):    #object
        noun = noun.upper()
        for location in self.game.caves:
            for player in location.players_here:
                if ('events' in dir(player) and
                    player != self):
                    player.events.append(self.name + " shouts: " + noun)
        return ["You shout: " + noun]

           
    actions = ['myteam','help', 'say', 'shout', 'describe', 'quit', 'inv', 'get', 'drop', 'drink', 'stats', 'kill', 'open', 'close', 'unlock', 'lock', 'wield', 'unwield', 'wear', 'remove']

    def kill(self, player, noun):
 #       print "DEBUG ==> kill method"
 #       print self.name
 #       print player.name
 #       print noun
 #       print " <== End DEBUG  kill method"

        if self.name == player.name:
            result = ["\tYou can't attack yourself"]
            return result

        for x in player.location.players_here:
               if x.character == 'town' and x.playing:
                   x.fight_list.append(player)
        #           if x != self:
         #             message = "WE MUST DEFEND " + self.name.upper() + "!!!"
         #              x.say(player, message)

        if player not in self.fight_list:
            self.fight_list.append(player)
        if self not in player.fight_list:
            player.fight_list.append(self)

      
                   
            
  #      print "DEBUG ==> kill method fight list"
#        print self.name
##        print player.name
 #       print player.fight_list
#        print "DEBUG ==> kill method fight list"
        
        result = self.do_kill(player)
        return result

    def do_kill(self, player):

        if self.status == 'DEAD':
            return
 #       print self.inv(self)
 #       if player == self:
#            result = ["\tYou can't attack yourself"]
#            return result

        for x in player.location.players_here:
               if x.character == 'town' and x.playing:
                   x.fight_list.append(player)
             #      if x != self:
             #          message = "WE MUST DEFEND " + self.name.upper() + "!!!"
             #          x.say(player, message)

        self.status = 'FIGHT'
        player.status = 'FIGHT'
       
 ##        print self.name
#        print player.name
#        print "DEBUG ==> getting ready to check for hits"

 #line 132       
        if not self.hit_roll(player):
            for x in player.location.players_here:
               if x is self:
                   x.events.append("\t" + player.name + " missed you!")
               elif x is player:
                   result = ["\tYou missed " + self.name]
               else:
                        x.events.append("\t" + player.name + " missed hitting " + self.name)
            return result

        else:
            damage = self.damage(player)
            self.hp -= damage
     
            print self.name + "==" + str(self.hp)

            if self.hp <= 0:
 #               print "DEBUG==> do_kill < 0 hp"
#                print self.location.players_here
#                print self.name
                for x in self.location.players_here:
 #                   print x.name + "<-->" +  str(x.fight_list)
                    if self in x.fight_list and x is not self:
                        x.fight_list.remove(self)
#                    print x.name + "<-->" +  str(x.fight_list)
                
#                print "DEBUG==> do_kill < 0 hp"
                for x in player.location.players_here:
                            if x is not player or not self:
                                 x.events.append("\t" + player.name + " has killed " + self.name + "!!")
                self.events.append("\t" + player.name + " has killed you!")
                if self.character == "human":
                    player.events.append("\tYou have killed " + self.name + "!")
                else:
                     player.events.append("\tYou have killed the " + self.name + "!")
 #               print self.inventory
                
                player.status = 'AWAKE'

 
                self.die()
   
                return ""

    
            if damage >= 25 and self.status != 'DEAD':
                for x in player.location.players_here:
                    if x is self:
                        x.events.append("\t" + player.name + " OBLITERATES you!")
                    elif x is player :
                        result = ["\tYou OBLITERATE " + self.name]
                    else:
                        x.events.append("\t" + player.name + " OBLITERATES " + self.name)

            elif damage >= 12 and self.status != 'DEAD':
                for x in player.location.players_here:
                    if x is self:
                        x.events.append("\t" + player.name + " hits you REALLY hard!")
                    elif x is player :
                        result = ["\tYou hit " + self.name + " REALLY hard"]
                    else:
                        x.events.append("\t" + player.name + " hits " + self.name + " REALLY hard!")

            else:
                for x in player.location.players_here:
                    if x is self:
                        x.events.append("\t" + player.name + " hits you!")
                    elif x is player :
                        result = ["\tYou hit " + self.name]
                    else:
                        x.events.append("\t" + player.name + " hits " + self.name)
               
            if self.hp <= 25:
                self.events.append("\tYou are bleeding very badly!") 
            
            return result

    def sleep(self, player, noun):
        player.status = 'SLEEP'
        result = ["You curl up and fall asleep on the ground"]
        return result

    def flee(self, player, noun):
        print "DEBUG Flee ==>"
        print self.location.players_here
        for x in self.location.players_here:
            if x is not self and self in x.fight_list:
                print x.name
                print x.fight_list
                x.fight_list.remove(self)
 #               if self in x.fight_list:
                    
            
        self.status = 'FLEE'
        direction_choices = [x for x in self.location.tunnels if self.location.tunnels[x] is not None]
        "DEBUG==> Flee"
 #       print direction_choices
        if direction_choices:
            random.shuffle(direction_choices)
            pick_direction = direction_choices[0]
            self.location.go(self, pick_direction)   #after picking a direction call the go function to handle movement
            self.status = 'AWAKE'
            self.fight_list = []
            return ""
        else:
            result = ["There's no where to go!!!"]
            return result

    def hit_roll(self, player):

  
        roll = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
 #      print self.name + "> " + str(roll) + "--ac--" + str(self.armor_class)
#        print "the attack roll was: " + str(roll)
        if roll == 1:
            return False
        elif roll == 20:
            return True

        else:
            defense = self.armor_class + (self.dexterity - player.dexterity)
 #           print "your defense was: " + str(defense)
            if roll >= defense:
                
 #           if roll >= self.armor_class:
                return True
            

            else:
                return False
                         
                

    def damage(self, player):

    
           if player.attack_class == "2d8":
#2d8
                roll_1 = random.choice([1,2,3,4,5,6,7,8])
                roll_2 = random.choice([1,2,3,4,5,6,7,8])
                damage_roll = roll_1 + roll_2 + int(player.strength/2)
                return damage_roll
#2d6
           elif player.attack_class == "2d6":
                roll_1 = random.choice([1,2,3,4,5,6])
                roll_2 = random.choice([1,2,3,4,5,6])
                damage_roll = roll_1 + roll_2 
                return damage_roll
#1d8
           elif player.attack_class == "1d8":
                damage_roll = random.choice([1,2,3,4,5,6,7,8])
                damage_roll += int(player.strength/2)
                return damage_roll

#1d6
           elif player.attack_class == "1d6":
                damage_roll = random.choice([1,2,3,4,5,6])
                return damage_roll
#1d20            
           elif player.attack_class == "1d20":
                damage_roll = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
                damage_roll += int(player.strength/2)
                return damage_roll           
#1d12
           elif player.attack_class == "1d12":
                damage_roll = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
                return damage_roll
#1d2            
           elif player.attack_class == "1d2":
                damage_roll = random.choice([1,2])
                return damage_roll
#1d4
           else:
                player.attack_class == "1d4"
                damage_roll = random.choice([1,2,3,4])
 #              print damage_roll
                return damage_roll
        

    def help(self, player, noun):
        result = ["you have the following commands available"]
#        result += [x for x in self.actions]
 #       print self.game.player_store[self.name]   #debug
        return result

    def quit(self, player, noun):

        if self.status == 'FIGHT':
            return ["You can't do that, you're in fight!"]

        if self.wearing:
            for x in self.wearing:                  #   remove all your gear and put it into inventory
                self.inventory.append(x)               
        self.wearing = []                       #   clear what you were wearing since we put it into inventory
        if self.wielding:                       #   if you have a weapon, put it into inventory
            self.inventory.append(self.wielding[0])    
            self.wielding = []    
        
        self.game.player_store[self.name] = self.save()
 
        for x in self.location.players_here:
            x.events.append(self.name + " has quit the game")
        self.game.players.remove(self)
        self.location.players_here.remove(self)
        self.connection.transport.loseConnection()

        return ""


            
    def die(self):
        print "\t\t********** " + self.name + " has been killed at " + str(self.location) + " *****************"
 
        self.input = ""
        self.input_list = []
        self.events = []
        self.result = []


        factory.die_gold(self)    
        
        if self.wearing:
            for x in self.wearing:                  #   remove all your gear and put it into inventory
                self.inventory.append(x)               
        self.wearing = []                       #   clear what you were wearing since we put it into inventory
        if self.wielding:                       #   if you have a weapon, put it into inventory
            self.inventory.append(self.wielding[0])    
            self.wielding = []                      # clear your weapon since it is now in inventory
# Dump your inventory on the ground where you died               
        for x in self.inventory:
            self.location.items_here.append(x)
            x.location = self.location
            for y in self.location.players_here:
                if y is not self:
                    y.events.append("\t" + self.name + " drops the " + x.name)

        self.inventory = []                     #wipe out your inventory since it is now on the ground
        
        
#Monsters die and stay dead
        if self.character != 'human':
            self.playing = False
            self.status = "DEAD"           
            self.description = "A dead " + self.name + " lies here..."
            self.name = "dead " + self.name
            self.fight_list = []
#Players get resurrected in Limbo
        else:
            self.connection.msg_me("\nYou have been killed!")
            

            for x in self.location.players_here:    #cool effects of you being sent to Limbo after dying
                if x is not self:
                        x.events.append("\tThe corpse of " + self.name + " vanishes in a puff of smoke!")
            self.fight_list = []
            self.hp = 25
            self.attack_class = "1d4"
            self.location.players_here.remove(self)     #remove you from where you died and put you in Limbo
            if self.team == "red":
                self.location = self.game.red_start
     
            elif self.team == "blue":
                self.location = self.game.blue_start 
            else:
                self.location = self.game.reborn_loc
                
            self.location.players_here.append(self)
            self.status = 'AWAKE'
            self.connection.msg_me("\nThe Gods think you have fought well and decided to resurrect you to try again.")
     
        return ""


    def save(self):
         
        return {
            'name': self.name,
            'description': self.description,
 #           'location' : self.location,
            'hp' : self.hp,
            'str' : self.strength,
            'dex' : self.dexterity,
            'wallet' : self.wallet,
            'team' : self.team,
            'bank' : self.bank,
#            'password': self.password,

            'items': [(item.name)
                      for item in (self.inventory + self.wearing + self.wielding)
                      if item.item_type != 'MISC']
        }

    def load_player(self, config):                         

        self.name = config['name']
 #       self.password = config['password']
        self.description = config['description']
        self.hp = config['hp']
        self.strength = config['str']
        self.dexterity = config['dex']
        self.wallet = config['wallet']
        self.team = config['team']
        self.bank = config['bank']

 #       print "DEBUG==> Load"      
 #       print self.location.players_here   
 #       print self.team
 #       print self.location
        self.location.players_here.remove(self)
#        print self.location.players_here
        if self.team == "red":          
            self.location = self.game.red_start
        elif self.team == "blue":
            self.location = self.game.blue_start
        else:
            self.location = self.game.reborn_loc
        self.location.players_here.append(self)
#        print self.location
#        print self.location.players_here
#        print "DEBUG==> Load"
#
        for item in config['items']:
             created = factory.create_object(item, self)
             self.inventory.append(created)
             self.location.items_here.remove(created)
    
    def stats(self, player,noun):
        result = ["\t<You are " + self.name + " and belong to the  __" + self.team + "__ team>\n\n"]
        result += ["\n<hp = " + str(self.hp) + ">  <" + "str = " + str(player.strength) + "> <" + "dex = " + str(player.dexterity) + ">" +
                      " <ac = " + str(self.armor_class) + ">" + " <load = " + str(player.load) + ">" + " <attack=" + str(self.attack_class) + ">\n"]
        result += ["\n\tYou have " + str(self.wallet) + " gold coins"]
        result += ["\tYou have " + str(self.bank) + " gold coins in the bank\n"]
     
        
        if self.wielding:
            result += ["\t<You wield the " + self.wielding[0].name + ">"]
        else:
            result += ["\t<You wield no weapon>"]

        if player.wearing:
            for x in player.wearing:
                result += ["\t<You wear a " + x.name + ">"]
        else:
            result += ["\t<You aren't wearing any armor>"]

        return result


    def describe(self, player, noun):
        self.description = noun
        return ["You changed your description to '%s'" % self.description]

    def myteam(self, player, noun):

  
 #       if str.lower(noun) != ('red' or 'blue'):
#            return ["That team doesn't exist. Please choose red or blue"]

#        else:
        self.team = noun
 #       print "\t\t *********" + self.name + " has changed his team to " + self.team + "****************"
        return ["You are now on the '%s' team"  % self.team]
        

    def wield(self, player, noun):
        return ["Wield what?"]

    def wear(self, player, noun):
        return ["You don't have the " + noun]

    def remove(self, player, noun):
        return ["How? You aren't wearing that!"]

    def unwield(self, player, noun):
        return ["Unwield what?"]

    def get(self, player, noun):
       return [noun + "? I can't see that anywhere"]

    def drop(self, player, noun):
        return ["You don't have the " + noun]

    def inv(self, player, noun):
        result = ["You have:"]
        if self.inventory:
            result += [x.name for x in self.inventory]
        else:
            result = ["you aren't carrying anything"]
        return result

    def drink(self, player, noun):
        return ["You don't have the " + noun]

    def open(self, player, noun):
        return ["You can't open the " + noun]

    def close(self, player, noun):
        return ["Nothing like that here to close"]

    def unlock(self, player, noun):
        return ["You can't unlock the " + noun]
   
    def lock(self, player, noun):
        return ["You can't lock the " + noun]

    
