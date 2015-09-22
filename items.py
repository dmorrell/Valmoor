import factory

class Item(object):
        def __init__ (self, name, description, weight, location, item_type, cost):
            self.name = name
            self.description = description
            self.location = location
            self.weight = weight
            self.item_type = item_type                      # WEAPON,ARMOR, DRINK, MISC, DOOR
            self.cost = cost
            location.items_here.append(self)

        actions = ['buy', 'look', 'get', 'drop', 'drink', 'open', 'close', 'unlock', 'lock', 'wield', 'unwield', 'wear', 'remove']



   #     def buy(self,player,noun):
    #        created = factory.create_object(noun, player)
     #       self.inventory.append(created)
      #      self.location.items_here.remove(created)


        def look(self, player, noun):
            return [self.description]


        def get(self, player, noun):

 #           if player.status == 'FIGHT':
#                    return ["\tYou can't get that right now, you're fighting!!"]

 #           if self.location is player:
#                return ["\tYou already have the " + self.name]
            if self.weight >= player.strength:
                return ["\tYou aren't strong enough to pick up the " +
                                self.name]

 #           if player.load + self.weight > player.maxload:
#                    return ["\tYou can't carry anymore!"]
           
            self.location.items_here.remove(self)

            if self.item_type == 'GOLD':
                    player.wallet += self.value
            else:
                    
                    self.location = player
                    player.inventory.append(self)
                    player.load += self.weight
                    
            for x in player.location.players_here:
                    if x is not player:
                         x.events.append(player.name + " picks up the " + self.name)
                    else:
                         pass
            return ["\tYou pick up the " + self.name]



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



        def wield(self, player, noun):

            if player.wielding:
                   return ["\tYou are already wielding the " + player.wielding[0].name]
            if self is player.wielding:
                   return ["\tYou already wield a " + self.name]

            if self.weight >= player.strength:
                return ["\tYou aren't strong enough to pick wield the " +
                                self.name]
            if self not in player.inventory:
                   return ["\tyou don't have the " + self.name]
            if self.item_type == "WEAPON":
                   player.inventory.remove(self)
                   player.wielding.append(self)
                   player.attack_class = self.attack_roll
                   for x in player.location.players_here:
                            if x is not player:
                                 x.events.append(player.name + " wields the " + self.name)
                            else:
                                 pass
                   result = ["\tYou wield the " + self.name]
            else:
                   result = ["\tYou can't wield that!"]
            return result

        def unwield(self, player, noun):

            if not player.wielding:
                   return ["\tYou aren't wielding anything"]
 #    
            else:
                   player.wielding.remove(self)
                   player.inventory.append(self)
                   
                   player.attack_class = "1d4"                 # bare-handed attack value
                   for x in player.location.players_here:
                            if x is not player:
                                 x.events.append(player.name + " unwields the " + self.name)
                            else:
                                 pass
                   return ["\tYou unwield the " + self.name]

        def wear(self, player, noun):

              if self.item_type != "ARMOR":
                     return ["\tYou can't wear that.\n"]
              if self in player.wearing:
                     return ["\tYou are already wearing that.\n"]
              if self not in player.inventory:
                      return ["\tYou don't have the " + self.name]

              already_wearing = [x for x in player.wearing
                                 if self.body_location is x.body_location]

              if already_wearing:
                      return ["\tYou are already wearing something for your " + self.body_location]


              else:
                     if self.body_location == "helmet":
                            result = ["\tYou put the " + self.name + " on your head\n"]

                     if self.body_location == "shield":
                            result = ["\tYou put the " + self.name + " on your arm\n"]

                     if self.body_location == "chest":
                            result = ["\tYou put the " + self.name + " on your chest\n"]

                     if self.body_location == "cloak":
                            result = ["\tYou put on the " + self.name + "\n"]

                     player.inventory.remove(self)
                     player.wearing.append(self)
                     player.armor_class += self.armor_class
                     for x in player.location.players_here:
                            if x is not player:
                                 x.events.append(player.name + " wears the " + self.name)
                            else:
                                 pass
              return result

        def remove(self, player, noun):


            if self not in player.wearing:
                   return ["\tYou aren't wearing that"]
 #    
            else:
                   player.wearing.remove(self)
                   player.inventory.append(self)
                   player.armor_class -= self.armor_class
                   for x in player.location.players_here:
                            if x is not player:
                                 x.events.append(player.name + " removes the " + self.name)
                            else:
                                 pass
                   return ["\tYou take off the " + self.name]
            
           

        def drop(self, player, noun):
            
            if self in player.wielding:
                   return ["You need to unwield the " + self.name + " before you can drop it\t"]
            if self in player.wearing:
                   return ["You need to stop wearing the " + self.name + " before you can drop it\t"]
            if self not in player.inventory:
                return ["\tYou don't have the " + self.name]

            player.inventory.remove(self)
            player.location.items_here.append(self)
            self.location = player.location
            player.load -= self.weight
            for x in player.location.players_here:
                    if x is not player:
                         x.events.append(player.name + " drops up the " + self.name)
                    else:
                         pass
            return ["You drop the " + self.name]

        def drink(self, player, noun):
                if self not in player.inventory:
                        return ["you don't have the " + self.name]

                if self.strength_mod > 0:
                        player.strength += self.strength_mod
                        player.maxload = player.strength * 2
                        result = ["You drink the " + self.name + "...You feel stronger!!"]
                if self.dexterity_mod > 0:
                        player.dexterity += self.dexterity_mod
                        result = ["You drink the " + self.name + " potion and you feel more coordinated."]

                if self.healing > 0:
                        player.hp += self.healing
                        result = ["You drink the " + self.name + " potion and you feel better."]
                        if player.hp > player.maxhp:
                                player.hp = player.maxhp
                for x in player.location.players_here:
                    if x is not player:
                         x.events.append(player.name + " drinks a " + self.name)
                    else:
                         pass
                
                player.inventory.remove(self)
                player.load -= self.weight
                del self

                return result

        def open(self, player, noun):

                if self.state is 'OPEN':
                        result = ["The door is already open"]

                elif self.lock_status == 'LOCKED':
                        result = ["The door appears to be locked"]

                else:
                        self.state = 'OPEN'
                        self.location.tunnels[self.cave_to_direction] = self.cave_to
                        pair = self.door_pair[0]
                        pair.state = 'OPEN'
                        pair.location.tunnels[pair.cave_to_direction] = pair.cave_to
                        for x in player.location.players_here:
                            if x is not player:
                                 x.events.append(player.name + " opens the " + self.name)
                            else:
                                 pass

                        result = ["You open the door"]
                return result


        def close(self, player, noun):
                if self.state is 'CLOSED':
                        result = ["The " + self.name + " is already closed"]
                else:
                        self.state = 'CLOSED'
                        self.location.tunnels[self.cave_to_direction] = 'door'
                        pair = self.door_pair[0]
                        pair.state = 'CLOSED'
                        pair.location.tunnels[pair.cave_to_direction] = 'door'
                        for x in player.location.players_here:
                            if x is not player:
                                 x.events.append(player.name + " closes the " + self.name)
                            else:
                                 pass
                        result = ["You close the " + self.name]
                return result

        def unlock(self, player, noun):
                if self.lock_status is 'UNLOCKED':
                        result = ["The " + self.name + " is already unlocked"]
                        
                elif self.key not in player.inventory:
                        result = ["You don't have the key to open this door"]
                else:
                        self.lock_status = 'UNLOCKED'
                        pair = self.door_pair[0]
                        pair.lock_status = 'UNLOCKED'
                        for x in player.location.players_here:
                            if x is not player:
                                 x.events.append(player.name + " unlocks the " + self.name)
                            else:
                                 pass
                        result = ["You unlock the door"]
                return result                        

        def lock(self, player, noun):
                if self.lock_status is 'LOCKED':
                        result = ["The " + self.name + " is already locked"]
                        
                elif self.state is 'OPEN':
                        result = ["You need to close the " + self.name + " before you can lock it"]
                elif self.key not in player.inventory:
                        result = ["You don't have the key to lock this door"]
                else:
                        self.lock_status = 'LOCKED'
                        pair = self.door_pair[0]
                        pair.lock_status = 'UNLOCKED'
                        for x in player.location.players_here:
                            if x is not player:
                                 x.events.append(player.name + " locks the " + self.name)
                            else:
                                 pass
                        result = ["You lock the door"]
                return result 



class Weapon(Item):
        def __init__ (self, name, description, weight, location, item_type, cost, attack_roll):
            Item.__init__ (self, name, description, weight, location, item_type, cost)

            self.attack_roll = attack_roll

  
 

class Armor(Item):
       
        def __init__ (self, name, description, weight, location, item_type, cost, body_location, armor_class):
            Item.__init__ (self, name, description, weight, location, item_type, cost)

            self.armor_class = armor_class
            self.body_location = body_location


class Drink(Item):
        def __init__ (self, name, description, weight, location, item_type, cost, strength_mod, dexterity_mod, healing):
            Item.__init__ (self, name, description, weight, location, item_type, cost)

            self.strength_mod = strength_mod
            self.dexterity_mod = dexterity_mod
            self.healing = healing


class Door(Item):
        def __init__(self, name, description, weight, location, item_type, cost, state, lock_status, key, cave_to, cave_to_direction):
            Item.__init__ (self, name, description, weight, location, item_type, cost)
       
            self.state = state                                  # whether door is open or closed
            self.lock_status = lock_status                      #is door locked or unlocked
            self.key = key                                      #type of key needed to unlock
            self.cave_to = cave_to                              #connecting cave
            self.cave_to_direction = cave_to_direction             #direction of connecting cave
            self.door_pair = [] 

class Gold(Item):
        def __init__ (self, name, description, weight, location, item_type, cost, value):
            Item.__init__ (self, name, description, weight, location, item_type, cost)

            self.value = value
        
                        
                        
                        
                
                




        
        
