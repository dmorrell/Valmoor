import player, random, caves, factory, Valmoor
from string import ascii_letters, digits
from twisted.internet.protocol import ServerFactory
from twisted.conch.telnet import StatefulTelnetProtocol
from twisted.internet import reactor, task
#from mud_server import MudProtocol

class Human(player.Player):
      

    def __init__(self, game, location):
        player.Player.__init__(self, location)
        self.game = game
        self.name = " "
        self.character  = "human"
        self.team = "neutral"
        self.description = ""
        self.status = "AWAKE"
        self.hp = 150
        self.maxhp = 200
        self.armor_class = 2   
        self.attack_class = "1d4"
        self.strength = 4
        self.dexterity = 4
        self.load = 0
        self.maxload = 25
        

        if self.team == "neutral":
            self.location.players_here.append(self)

 
    
    def get_input(self):


        if self.input_list:
            return self.input_list.pop()
              
        else:
            return ""     #if no one to fight, return nothing      

    def update(self):

        self.result = self.process_input(self.input)

        monster_check = [x for x in self.location.players_here if x.character == "monster" and x.playing]
#     if a monster(s) is in the room, add them to the fight list to be attacked
        if monster_check:
                for x in monster_check:
                    if x not in self.fight_list:
                        self.fight_list.append(x)
   
        enemy_check = [x for x in self.location.players_here if (self.team != x.team) and x.playing and x.character != 'town']
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


    def deposit(self, player, noun):

  
        valid_number = self.number_test(noun)

        if valid_number >0:     
            banker_check = [x for x in self.location.players_here if x.name == "Banker"]

            if not banker_check:
                return ["There's no one here to make a deposit with"]

            elif valid_number > self.wallet:
                return ["You don't have that much money!"]

            else:
                self.wallet -= valid_number
                self.bank += valid_number

                for x in self.location.players_here:
                            if x is not self:
                                x.events.append(self.name + " deposits some money")
                return ["You deposit " + str(valid_number) + " gold coins"]

        else:
            return ["Can't deposit that"]

    def withdraw(self,player,noun):

        valid_number = self.number_test(noun)

        if valid_number >0:     

            banker_check = [x for x in self.location.players_here if x.name == "Banker"]

            if not banker_check:
                return ["You can't make a withdrawal here"]

            elif valid_number > self.bank:
                return ["You don't have that much money!"]

            else:
                self.wallet += valid_number
                self.bank -= valid_number
                for x in self.location.players_here:
                            if x is not self:
                                x.events.append(self.name + " withdraws some money")
                return ["You withdraw " + str(valid_number) + " gold coins"]
        
        else:
            return ["Can't withdraw that"]


    def number_test(self, number):
        number_split = list(number)
        check_number = [x for x in number_split if str.isdigit(x)]
        if check_number:
            join_number = int("".join(check_number))
            print "DEBUG==> number test "
            print join_number
            return join_number
        else:
            return 0
       

    def list(self,player,noun):
        print "DEBUG==> list"
        if self.location.name == "Apothecary":
            result = ["You can buy the following:\n"]
            result += ["\t'Blue' potion of healing      : 30 gold\n"]
            result += ["\t'Red' potion of strength      : 30 gold\n"]
            result += ["\t'Green' potion of dexterity   : 30 gold\n"]

        elif self.location.name == "Armory":
            result = ["You can buy the following:\n"]
            result += ["\t Wooden 'shield'   : 15 gold\n"]
            result += ["\t'Steel shield'   : 75 gold\n"]
            result += ["\t'Leather helmet'  : 20 gold\n"]
            result += ["\t'Steel Gauntlets'  : 75 gold\n"]
            result += ["\t'Steel helmet'    : 75 gold\n"]
            result += ["\t'Leather vest'    : 30 gold\n"]
            result += ["\t'Chain Mail'      : 150 gold\n"]
            result += ["\t'Plate Mail'      : 200 gold\n"]
            

        elif self.location.name == "Weapon Shop":
            result = ["You can buy the following:\n"]
            result += ["\t'Sword'        : 25 gold\n"]
            result += ["\t'Halberd'      : 75 gold\n"]
            result += ["\t Battle 'Axe'   : 150 gold\n"]
            result += ["\t'Warhammer'    : 150 gold\n"]
            result += ["\t'Mace'    : 150 gold\n"]

        else:
            result = ["Nothing to buy here"] 
        return result

    def sell(self,player,noun):


                
                print "DEBUG==> Sell"
                print self.name
                print player.name
                print noun
                
                if self not in player.inventory:
                    result = ["You don't have that to sell."]

                elif player.location.name == "Apothecary" and self.item_type == "DRINK":
                    apothecary_check = [x for x in player.location.players_here if x.name == "Apothecary"]
                    if apothecary_check:
                        result = self.do_sell(player)
                    else:
                        result = ["No one here to buy that."]


                elif player.location.name == "Armory" and self.item_type == "ARMOR":
                    armorer_check = [x for x in player.location.players_here if x.name == "Armorer"]
                    if armorer_check:
                        result = self.do_sell(player)
                    else:
                        result = ["No one here to buy that."]


                elif player.location.name == "Weapon Shop" and self.item_type == "WEAPON":
                    blacksmith_check = [x for x in player.location.players_here if x.name == "Blacksmith"]
                    if blacksmith_check:
                        result = self.do_sell(player)
                    else:
                        result = ["No one here to buy that."]

                elif player.location.name == "General Store" and self.item_type == "MISC":
                    merchant_check = [x for x in player.location.players_here if x.name == "Merchant"]
                    if merchant_check:
                        result = self.do_sell(player)
                    else:
                        result = ["No one here to buy that."]

                else:
                    result = ["You can't sell that here"]
                return result

    def do_sell(self,player):

                    player.inventory.remove(self)
                    player.wallet += self.cost
                    return ["You sell a " + str(self.name) + " for " + str(self.cost) + " gold coins"]


  
 
    def buy(self,player,noun):


        created = factory.create_object(noun, player)
#        print "DEBUG==> Buy"
 #       print str(created.name) + str(created.item_type) + str(created.cost)

     

        if created == None:
            return ["That isn't available for sale here"]
  
        elif self.name == 'Vlad':
            result = self.do_buy(created)
            return result

        elif self.location.name == "Apothecary" and created.item_type == "DRINK":
            apothecary_check = [x for x in self.location.players_here if x.name == "Apothecary"]
            if apothecary_check:
                result = self.do_buy(created)
            else:
                result = ["No one here to buy that from."]


        elif self.location.name == "Armory" and created.item_type == "ARMOR":
            armorer_check = [x for x in self.location.players_here if x.name == "Armorer"]
            if armorer_check:
                result = self.do_buy(created)
            else:
                result = ["No one here to buy that from."]


        elif self.location.name == "Weapon Shop" and created.item_type == "WEAPON":
            blacksmith_check = [x for x in self.location.players_here if x.name == "Blacksmith"]
            if blacksmith_check:
                result = self.do_buy(created)
            else:
                result = ["No one here to buy that from."]

        else:
            del created
            result = ["You can't buy that here"]
        return result


    
    def do_buy(self,created):
        if self.name == 'Vlad':
            self.inventory.append(created)
            self.location.items_here.remove(created)
            return ["You buy a " + str(created.name)]
        
        elif created.cost <= self.wallet:
            self.inventory.append(created)
            self.location.items_here.remove(created)
            self.wallet -= created.cost
            return ["You buy a " + str(created.name) + " for " + str(created.cost) + " gold coins."]
        else:
            del created
            return ["You don't have the money for that"]

    


        

    actions = ['sell', 'list', 'withdraw', 'deposit', 'buy','myteam','help', 'quit', 'describe', 'say', 'shout','inv', 'get', 'drop', 'drink', 'stats', 'kill', 'flee', 'open', 'close', 'unlock', 'sleep', 'wield', 'unwield', 'wear', 'remove']

    
