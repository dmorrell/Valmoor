from random import choice, shuffle
import items
import Valmoor
import copy

class Cave(object):

    directions = {'north' : 'None',
                  'south' : 'None',
                  'east' : 'None',
                  'west' : 'None',
                  'up' : 'None',
                  'down' : 'None'}

    
    
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.items_here = []
        self.players_here = []
        self.tunnels = {}


    def __repr__(self):
        return "<" + self.name + ">"


    def look(self, player, noun):

        if noun == str.lower(player.name):
            result = [player.description]
        elif noun == "":
            result = ["\n" + self.name]
            if len(self.items_here or self.players_here) > 0:
                for x in self.players_here:
                    if x.name != player.name:
                        if x.character == 'human':
                            result += ["\t" + x.name + " stands here"]
                        else:
                            result += ["\t" + x.description]
                result += ["\t" + x.description for x in self.items_here if 'name' in dir(x)]
                result += self.exits(player,noun)
        else:
            result = [noun + "\t? I can't see that anywhere...\n"]

        return result

    

    
    def go(self, player, noun):
     
        if player.status == 'FIGHT':
            return ["You can't walk away, you're in a fight!"]
        if noun not in self.directions:
            return ["that isn't a valid direction"]
        if self.tunnels[noun] is None:
            return ["That way seems blocked"]



        if self.tunnels[noun] is 'door':
            return ["You need to open the door first..."]
        self.players_here.remove(player)
        self.tunnels[noun].players_here.append(player)
        player.location = self.tunnels[noun]

        if player.status == 'FLEE':
            for x in self.players_here:
                x.events.append("\tThe " + player.name + " flees " + noun)
            for x in self.tunnels[noun].players_here:
                if x is not player:
                    x.events.append("\tThe " + player.name + " arrives")
            player.events.append("\tYou flee " + noun)
            result = self.tunnels[noun].look(player, "")

        else:
            result = ["\t\nYou go " + noun + "\n\n"]
            for x in self.players_here:
                if x.character == "monster":
                    x.events.append("\tThe " + player.name + " leaves " + noun)
                else:
                    x.events.append("\t" + player.name + " leaves " + noun)
            for x in self.tunnels[noun].players_here:
                if x is not player:
                    if x.character == "monster":
                        x.events.append("\tThe " + player.name + " leaves " + noun)
                    else:
                        x.events.append("\t" + player.name + " arrives")
            result += self.tunnels[noun].look(player, "")
        return result
        

# call this function to find exits when fleeing since it returns no formatting
    def find_exits(self):
        result = [x for x in self.tunnels if self.tunnels[x] is not None]
        return result



    def exits(self, player, noun):


        result = ["\t\nYou see the following exits: "]
        options = [x for x in self.tunnels if self.tunnels[x] is not None]
        
        for y in options:
            if self.tunnels[y] is 'door':
                result += ["\tYou see a door to the " + y]
   
            else:
                result += ["\t" + y + " \t- " + self.tunnels[y].name]
                
        result += "\n"
        return result

    actions = ['look', 'go', 'exits']



    

