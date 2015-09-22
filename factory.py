import items

    
def create_object(item, player):

#Weapons
    print "DEBUG==> create object"
    print item
    print player.name
    
    if item == "sword":
        sword = items.Weapon("sword", "A simple long 'sword'", 2, player.location, "WEAPON", 25, attack_roll = "1d8")
        return sword

    if item == "warhammer":
        warhammer = items.Weapon("warhammer", "A large, steel 'warhammer'", 6, player.location, "WEAPON", 150, attack_roll = "1d20")   
        return warhammer

    if item == "axe":
        battle_axe = items.Weapon("axe", "A wicked looking battle 'axe'", 5, player.location, "WEAPON", 150, attack_roll = "2d8")
        return battle_axe

    if item == "halberd":
        halberd = items.Weapon("halberd", "A well polished 'halberd'", 3, player.location, "WEAPON", 75, attack_roll = "1d12")
        return halberd
    if item == "mace":
        mace = items.Weapon("Mace", "A wicked looking spiked 'mace' lies here", 3, cave_1000, "WEAPON", 150, attack_roll = "2d8")
        return mace

    
#Armor
    if item == "shield":
        wooden_shield = items.Armor("shield", "A worn looking wooden 'shield'", 1, player.location, "ARMOR", 15, "shield", armor_class = 1) 
        return wooden_shield
    if item == "steel shield":
        steel_shield = items.Armor("steel shield", "A lightly used 'steel shield'", 5, player.location, "ARMOR", 75, "shield", armor_class = 3)
        return steel_shield
    if item == "leather helmet":
        leather_helmet = items.Armor("leather helmet", "A rough looking 'leather helmet'", 1, player.location, "ARMOR", 20, "helmet", armor_class = 1)
        return leather_helmet
    if item == "steel helmet":
        steel_helmet = items.Armor("steel helmet", "A burnished 'steel helmet'", 2, player.location, "ARMOR", 75, "helmet", armor_class = 3)
        return steel_helmet
    if item == "leather vest":
        leather_vest = items.Armor("leather vest", "A rough looking 'leather vest'", 2, player.location, "ARMOR", 30,  "chest", armor_class = 2)
        return leather_vest
    if item == "wolf cloak":
        wolf_cloak = items.Armor("wolf cloak", "a beautiful 'wolf cloak' lies here", 2, player.location, "ARMOR", 50, "cloak", armor_class = 2)
        return wolf_cloak
    if item == "chain mail":
        chain_mail = items.Armor("chain mail", "A set of used 'chain mail'", 5, player.location, "ARMOR", 150, "chest", armor_class = 5)
        return chain_mail
    if item == "plate mail":
        plate_mail = items.Armor("plate mail", "A well made set of 'plate mail'", 7, player.location, "ARMOR", 200, "chest", armor_class = 7)
        return plate_mail
    if item == "dragon plate":
        dragon_plate = items.Armor("Dragon Plate", "A gleaming set of 'dragon plate' armor", 5, player.location, "ARMOR", 300, "chest", armor_class = 7)
        return dragon_plate
    if item == "steel gauntlets":
        steel_gauntlets = items.Armor("steel gauntlets", "Shiny 'steel gauntlets' lie here", 5, cave_1000, "ARMOR", 75, "gloves", armor_class = 3)
        return steel_gauntlets
   
    
#Potions
    if item == "blue":
        blue_potion = items.Drink("blue", "A dusty bottle with a clear 'blue' liquid inside", 1, player.location, "DRINK", 10, 0, 0, 60)   #health
        return blue_potion
    if item == "red":
        red_potion = items.Drink("red", "A clear bottle with a glowing 'red' liquid inside", 1, player.location, "DRINK", 30, 1, 0, 0)    #strength
        return red_potion
    if item == "green":
        green_potion = items.Drink("green", "An old bottle with a dark 'green' liquid inside", 1, player.location, "DRINK", 30, 0, 1, 0)   #dexterity
        return green_potion
    if item == "purple":
        purple_potion = items.Drink("purple", "An faintly glowing bottle with a 'purple' liquid inside", 1, player.location, "DRINK", 100, 100, 100, 100)   #dexterity
        return purple_potion    

    return None


def die_gold(player):
        gold = items.Gold("gold", "'gold' coins", 0, player.location, "GOLD", 0, player.wallet)
        player.wallet = 0
        print "DEBUG==> die gold" + str(gold.value)
        if gold.value > 0:
            for y in player.location.players_here:
                if y is not player:
                    y.events.append("\t" + player.name + " drops some gold")
        else:
            player.location.items_here.remove(gold)
            del gold
    

#Misc
   
 #       crown = items.Item("gold crown", "A shiny 'gold crown'", 1, cave_33, "MISC")
    ##   iron_key = items.Item("iron key", "A rusty 'iron key'", 1, cave_1000, "MISC")
      #  silver_key = items.Item("silver key", "A gleaming 'silver key'", 1, cave_1000, "MISC")
       # golden_key = items.Item("golden key", "A solid 'golden key'", 1, cave_1000, "MISC")
