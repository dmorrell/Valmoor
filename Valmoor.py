import random
import caves, copy, town, factory
import monster, humans, items, player, time, soldiers 
import os
import pickle

class Game(object):
    def __init__(self):

        
        cave_0 = caves.Cave(
                "limbo",
                "nothing here to see"
                )

#Valmoor
        cave_1 = caves.Cave(
                "Stables",
                "The kings stable's are ",
                )
        
        cave_2 = caves.Cave(
                "Castle Gates",
                " ",
                )

        cave_3 = caves.Cave(
                "Guard Shack",
                " ",
                )
        
        cave_4 = caves.Cave(
                "Soldier's Barracks",
                " ",
                )
        cave_5 = caves.Cave(
                "Infirmary",
                " ",
                )
        
        cave_6 = caves.Cave(
                "Western Hallway",
                " ",
                )
        cave_7 = caves.Cave(
                "West side of Courtyard",
                " ",
                )
        
        cave_8 = caves.Cave(
                "Central Courtyard",
                " ",
                )

        cave_9 = caves.Cave(
                "East Side of Courtyard",
                " ",
                )
        
        cave_10 = caves.Cave(
                "Eastern Hallway",
                " ",
                )

        cave_11 = caves.Cave(
                "Armory",
                " ",
                )
        
        cave_12 = caves.Cave(
                "Wizard's Tower",
                " ",
                )
        cave_13 = caves.Cave(
                "Tapestry Room",
                " ",
                )
        
        cave_14 = caves.Cave(
                "Library",
                " ",
                )
        cave_15 = caves.Cave(
                "Entrance Hall",
                " ",
                )
        
        cave_16 = caves.Cave(
                "Alcove",
                " ",
                )

        cave_17 = caves.Cave(
                "Game Room",
                " ",
                )
        
        cave_18 = caves.Cave(
                "Eastern Tower",
                " ",
                )

        cave_19 = caves.Cave(
                "Art Collection",
                " ",
                )
        
        cave_20 = caves.Cave(
                "Trophy Room",
                " ",
                )
        cave_21 = caves.Cave(
                "Grand Ballroom",
                " ",
                )
        
        cave_22 = caves.Cave(
                "Council Chambers",
                " ",
                )
        cave_23 = caves.Cave(
                "Reception",
                " ",
                )
        
        cave_24 = caves.Cave(
                "Servant's Quarters",
                " ",
                )

        cave_25 = caves.Cave(
                "King's Waiting Room",
                " ",
                )
        
        cave_26 = caves.Cave(
                "King's Study",
                " ",
                )


        cave_27 = caves.Cave(
                "Throne Room",
                " ",
                )

        cave_28= caves.Cave(
                "Main Treasury",
                " ",
                )
        
        cave_29 = caves.Cave(
                "Dining Hall",
                " ",
                )
        cave_30 = caves.Cave(
                "Kitchen",
                " ",
                )
        
        cave_31 = caves.Cave(
                "King's Bedroom",
                " ",
                )
        cave_32 = caves.Cave(
                "King's Tower",
                " ",
                )
        
        cave_33 = caves.Cave(
                "Secret Treasury",
                " ",
                )

        cave_34 = caves.Cave(
                "Balcony",
                " ",
                )
        
        cave_35 = caves.Cave(
                "Storage",
                " ",
                )

#Forest
        cave_101 = caves.Cave(
                "Western Pine Forest",
                " ",
                )
        
        cave_102 = caves.Cave(
                "Eastern Pine forest",
                " ",
                )

        cave_103 = caves.Cave(
                "Orange Orchard",
                " ",
                )
        
        cave_104 = caves.Cave(
                "Western Evergreen Forest",
                " ",
                )
        cave_105 = caves.Cave(
                "Middle Evergreen Forest",
                " ",
                )
        
        cave_106 = caves.Cave(
                "Eastern Evergreen Forest",
                " ",
                )
        cave_107 = caves.Cave(
                "South West Pine Forest",
                " ",
                )
        
        cave_108 = caves.Cave(
                "South East Pine Forest",
                " ",
                )

        cave_109 = caves.Cave(
                "Southern Orange Orchard",
                " ",
                )
        
        cave_110 = caves.Cave(
                "South East Evergreen Forest ",
                " ",
                )

        cave_111 = caves.Cave(
                "Bottom Middle Evergreen Forest",
                " ",
                )
        
        cave_112 = caves.Cave(
                "South East Evergreen Forest",
                " ",
                )
        cave_113 = caves.Cave(
                "Dragon Pass",
                "You see burning and smoking rocks leading up into the mountains",
                )
        
        cave_114 = caves.Cave(
                "Dead Forest",
                "The leaves on all the trees are rotting and making a horrific smell",
                )
        cave_115 = caves.Cave(
                "Birch Wood Forest",
                " ",
                )
        
        cave_116 = caves.Cave(
                "Jagged trail",
                "A rocky, jagged trail that is difficult to walk on leads around the mountain",
                )

        cave_117 = caves.Cave(
                "Caverns",
                "Numerous caverns are visible from the trail",
                )
        
        cave_118 = caves.Cave(
                "Valmoor Entrance",
                "You see the ruined castle of Valmoor in the distance",
                )

        cave_119 = caves.Cave(
                "Trap",
                "There is burning lava everywhere ",
                )
        
        cave_120 = caves.Cave(
                "Goblin Cave",
                "It appears as if some goblin's have made a camp here. They may be back soon...",
                )
        cave_121 = caves.Cave(
                "Ancient Cemetary",
                "The remanants of a very old cemetary lie among the open space",
                )
        
        cave_122 = caves.Cave(
                "Mt.Superior Valley",
                " ",
                )
        cave_123 = caves.Cave(
                "Wolve's Den",
                "This appears to be the den of a large pack of wolves ",
                )
        
        cave_124 = caves.Cave(
                "Entrance to Castle Dorlaan",
                " ",
                )

        cave_125 = caves.Cave(
                "Entrance to Castle Crydee",
                " ",
                )
        
        cave_126 = caves.Cave(
                "Deserted Farm",
                " ",
                )


        cave_127 = caves.Cave(
                "Busch Forest",
                " ",
                )

        cave_128= caves.Cave(
                "Large Oak Tree",
                "A massive oak tree that must be more than 400 years old stands in the middle of the forest",
                )
        
        cave_129 = caves.Cave(
                "Eagle's Nest",
                " ",
                )
        cave_130 = caves.Cave(
                "Kingdom of Dorlaan",
                "You see Castle Dorlaan in the distance.",
                )
        
        cave_131 = caves.Cave(
                "Kingdom of Cyrdee",
                "You see castle Cyrdee in the distance",
                )
        cave_132 = caves.Cave(
                "Witch Doctor's Hut",
                "A dilapidated shack is in the clearing surrounded by skulls and bones",
                )
        
        cave_133 = caves.Cave(
                "Eastern Battlefield",
                "A large battle was recently fought here. Broken armor and dead bodies are strewn everywhere",
                )

        cave_134 = caves.Cave(
                "Temple Altar",
                "The stone Altar of the Dark God Oquen is before you",
                )
        
        cave_135 = caves.Cave(
                "Ruined Temple",
                "The remains of the temple of Oquen are in front of you",
                )

        cave_136 = caves.Cave(
                "Edge of Forest",
                "You see the back gate of Castle Dorlaan",
                )

#Cyrdee
        cave_201 = caves.Cave(
                "Entrance Hall",
                "Welcome to Red Castle",
                )
        
        cave_202 = caves.Cave(
                "West Hall",
                " ",
                )

        cave_203 = caves.Cave(
                "Soldier Barracks",
                " ",
                )
        
        cave_204 = caves.Cave(
                "Narrow Tunnel",
                " ",
                )
        cave_205 = caves.Cave(
                "Infirmary",
                " ",
                )
        
        cave_206 = caves.Cave(
                "Central Chambers",
                " ",
                )
        cave_207 = caves.Cave(
                "Troll's Lair",
                " ",
                )
        
        cave_208 = caves.Cave(
                "Northern Courtyard",
                " ",
                )

        cave_209 = caves.Cave(
                "East Side of Courtyard",
                " ",
                )
        
        cave_210 = caves.Cave(
                "Queen Bedroom",
                " ",
                )

        cave_211 = caves.Cave(
                "Dressing Room",
                " ",
                )
        
        cave_212 = caves.Cave(
                "East Hallway",
                " ",
                )
        cave_213 = caves.Cave(
                "Tapestry Room",
                " ",
                )
        
        cave_214 = caves.Cave(
                "Library",
                " ",
                )
        cave_215 = caves.Cave(
                "Battle Arena",
                " ",
                )
        
        cave_216 = caves.Cave(
                "East Hall",
                " ",
                )

        cave_217 = caves.Cave(
                "Game Room",
                " ",
                )
        
        cave_218 = caves.Cave(
                "Captain's Living Area",
                " ",
                )

        cave_219 = caves.Cave(
                "Art Collection",
                "You hear a faint ticking ",
                )
        
        cave_220 = caves.Cave(
                "Trophy Room",
                " ",
                )
        cave_221 = caves.Cave(
                "Kitchen",
                " ",
                )
        
        cave_222 = caves.Cave(
                "Dining Hall",
                " ",
                )
        cave_223 = caves.Cave(
                "Reception",
                " ",
                )
        
        cave_224 = caves.Cave(
                "Storage area",
                " ",
                )

        cave_225 = caves.Cave(
                "Entrance to staircase",
                " ",
                )
				
	cave_226 = caves.Cave(
                "Top of staircase",
                " ",
                )

        cave_227 = caves.Cave(
                "Cave 227",
                " ",
                )
        
        cave_228 = caves.Cave(
                "Cave 228",
                " ",
                )

        cave_229 = caves.Cave(
                "Cave 229",
                " ",
                )
        
        cave_230 = caves.Cave(
                "Cave 230",
                " ",
                )
        cave_231 = caves.Cave(
                "Cave 231",
                " ",
                )
        
        cave_232 = caves.Cave(
                "Cave 232",
                " ",
                )
        cave_233 = caves.Cave(
                "Cave 233",
                " ",
                )
        
        cave_234 = caves.Cave(
                "Cave 234",
                " ",
                )

        cave_235 = caves.Cave(
                "Cave 235",
                " ",
                )
        
        cave_236 = caves.Cave(
                "Cave 236",
                " ",
                )

        cave_237 = caves.Cave(
                "237",
                " ",
                )
        
        cave_238 = caves.Cave(
                "238",
                " ",
                )
        cave_239 = caves.Cave(
                "239",
                " ",
                )
        
        cave_240 = caves.Cave(
                "240",
                " ",
                )
        cave_241 = caves.Cave(
                "241",
                " ",
                )
        
        cave_242 = caves.Cave(
                "242",
                " ",
                )

        cave_243 = caves.Cave(
                "243",
                " ",
                )
        
        cave_244 = caves.Cave(
                "244",
                " ",
                )

        cave_245 = caves.Cave(
                "245",
                " ",
                )
        
        cave_246 = caves.Cave(
                "246",
                " ",
                )
        cave_247 = caves.Cave(
                "247",
                " ",
                )
        
        cave_248 = caves.Cave(
                "248",
                " ",
                )
        cave_249 = caves.Cave(
                "249",
                " ", 
                )
        
        cave_250 = caves.Cave(
                "Staircase to Floor 3",
                " ",
                )
				
	cave_251 = caves.Cave(
                "3rd Floor",
                "nothing here to see"
                )

        cave_252 = caves.Cave(
                "Upper Hallway",
                "Beginning Hallway ",
                )
        
        cave_253 = caves.Cave(
                "Ballroom",
                "where special events go on ",
                )

        cave_254 = caves.Cave(
                "Kitchen",
                " where the servants make the food ",
                )
        
        cave_255 = caves.Cave(
                "Servants room",
                "where the servants sleep ",
                )
        cave_256 = caves.Cave(
                "Grand bathroom",
                "where the guests go to the bathroom ",
                )
        
        cave_257 = caves.Cave(
                "Hallway of past Kings and Queens ",
                "pictures of past Kings and Queens on the wall ",
                )
        cave_258 = caves.Cave(
                "Gym",
                "where the people of the royal family workout ",
                )
        
        cave_259 = caves.Cave(
                "Spa",
                "where the Queen and the daughter get a spa ",
                )

        cave_260 = caves.Cave(
                "Bowling alley",
                "where they play bowling",
                )
        
        cave_261 = caves.Cave(
                "Grocery store",
                "where they get thier food ",
                )

        cave_262 = caves.Cave(
                "Armory",
                " where the armor is held ",
                )
        
        cave_263 = caves.Cave(
                "Sniper Tower",
                "where the snipers guard the castle ",
                )
        cave_264 = caves.Cave(
                "Trophy room ",
                "where all the trophys are held ",
                )
        
        cave_265 = caves.Cave(
                "Library",
                "where they get and read their books ",
                )
        cave_266 = caves.Cave(
                "Movie theater",
                "where they watch movies ",
                )
        
        cave_267 = caves.Cave(
                "Office of the King and Queen",
                "where they do all of their work ",
                )

        cave_268 = caves.Cave(
                "Game Room",
                "where they play games ",
                )
        
        cave_269 = caves.Cave(
                "Aquatic center",
                "where they go swimming ",
                )

        cave_270 = caves.Cave(
                "Art Collection",
                "where they art is held ",
                )
        
        cave_271 = caves.Cave(
                "Classroom",
                "where the kids go to school everyday ",
                )
        cave_272 = caves.Cave(
                "Guest's room",
                "where the guests sleep",
                )
        
        cave_273 = caves.Cave(
                "The Royal dog's room",
                "where the Royal dog sleeps",
                )
        cave_274 = caves.Cave(
                "Kids room",
                "where the kids sleep ",
                )
        
        cave_275 = caves.Cave(
                "King and Queen's room",
                "where the King and Queen sleep ",
                )

#Dorlaan

        cave_301 = caves.Cave(
                "Grand Entryway",
                "The best exploreres will be tested today. ",
                )
        
        cave_302 = caves.Cave(
                "Swampy Garden",
                "Garden filled with moss and murky waters. ",
                )

        cave_303 = caves.Cave(
                "West Dining Hall",
                "Informal dinners are held on these maple wood tables. ",
                )
        
        cave_304 = caves.Cave(
                "Dusty Cafeteria",
                "Large Parties are held here. Nothing has been here in 764 years. ",
                )
        cave_305 = caves.Cave(
                "Library",
                "Shelves filled with every kind of book possible.",
                )
        
        cave_306 = caves.Cave(
                "Western Hallway",
                "Your getting close. ",
                )
        cave_307 = caves.Cave(
                "Old Infirmary",
                "Doctors office.. from 200 years ago. ",
                )
        
        cave_308 = caves.Cave(
                "Dusty Office",
                "The principal's office after he took 5 years off. ",
                )

        cave_309 = caves.Cave(
                "Classroom",
                "Where the kids learn. ",
                )
        
        cave_310 = caves.Cave(
                "School Entrance",
                "Where the kids enter in disgust. ",
                )

        cave_311 = caves.Cave(
                "Centeral Headquarters",
                "Main office and storage of castle. ",
                )
        
        cave_312 = caves.Cave(
                "Law Enfocement Office",
                "Court cases are held here. ",
                )
        cave_313 = caves.Cave(
                "Rusty Dungeon",
                "Imprisoning Theifs since Castle opening..  ",
                )
        
        cave_314 = caves.Cave(
                "Secret Hideout",
                "You aren't supposed to be here.",
                )
        cave_315 = caves.Cave(
                "East Way",
                "Passage way in the castle. ",
                )
        
        cave_316 = caves.Cave(
                "Outdated store",
                "A store that went out of buisness.. a long time ago.",
                )

        cave_317 = caves.Cave(
                "East Entrance",
                "Adventures await. ",
                )
        
        cave_318 = caves.Cave(
                "Bankhouse",
                "Currency Storage. ",
                )

        cave_319 = caves.Cave(
                "East Dining Hall",
                "The most formal and fancy dining room in the land. ",
                )
        
        cave_320 = caves.Cave(
                "Side Throne",
                "Wanna be king's Private Area.. Off limits.",
                )
        cave_321 = caves.Cave(
                "Key to the future.",
                "Nothing to see here. ",
                )
        
        cave_322 = caves.Cave(
                "Auditorium",
                "Shows for the king are preformed here. ",
                )
        cave_323 = caves.Cave(
                "Dirty Cave",
                "Trashy cave, nobody likes it here. ",
                )
        
        cave_324 = caves.Cave(
                "Empty Hole",
                "Hole in the ground, dirt and air. ",
                )

        cave_325 = caves.Cave(
                "Ghetto Closet",
                "You must be skilled to get here, but are you a real adventurer? ",
                )

        cave_326 = caves.Cave(
                "Entry Hall",
                "A long passageway"
                )

        cave_327 = caves.Cave(
                "Dusty Cave",
                "A slient cave ",
                )
        
        cave_328 = caves.Cave(
                "Closet",
                "Many clothes surrond you ",
                )

        cave_329 = caves.Cave(
                "Junkyard",
                "Piles of trash is lying around you ",
                )
        
        cave_330 = caves.Cave(
                "Dome",
                "A large glass dome ",
                )
        cave_331 = caves.Cave(
                "Ball Room",
                "Music fills the air ",
                )
        
        cave_332 = caves.Cave(
                "Deep Hallway",
                "A bed feeling in sticking in your stomach ",
                )
        cave_333 = caves.Cave(
                "High Point",
                "Overlook the castle ",
                )
        
        cave_334 = caves.Cave(
                "School Room",
                "A thick chalkboard awaits you ",
                )

        cave_335 = caves.Cave(
                "Training Room",
                "The smell of sweat fills the air ",
                )
        
        cave_336 = caves.Cave(
                "Sleeping Quarters",
                "Many beds are filled in long rows ",
                )

        cave_338 = caves.Cave(
                "Peasant Room",
                "Cleaning supplies are before you ",
                )

        cave_337 = caves.Cave(
                "Dungeon",
                " ",
                )
        
        cave_339 = caves.Cave(
                "Bathroom",
                "The sound of water drips in your ear ",
                )
        cave_340 = caves.Cave(
                "Fields",
                "Wide fields of grass ",
                )
        
        cave_341 = caves.Cave(
                "Garden",
                "Flowers are blooming ",
                )
        cave_342 = caves.Cave(
                "Fountain",
                "A large fountain ",
                )
        
        cave_343 = caves.Cave(
                "Library",
                "Shelves of vast variety of books ",
                )

        cave_344 = caves.Cave(
                "Theater",
                "A huge stage, with empty rows of seats ",
                )
        
        cave_345 = caves.Cave(
                "Monstorus Beast",
                "Roarr! A sounds booms through the air ",
                )

        cave_346 = caves.Cave(
                "Wine Cellar",
                "Imported wine is shelved in coolers ",
                )
        
        cave_347 = caves.Cave(
                "Corridor",
                "Too silent to be real ",
                )
        cave_348 = caves.Cave(
                "Abandon Room",
                "Scraps of paper lay on the floor ",
                )
        
        cave_349 = caves.Cave(
                "Children Room",
                "Fun toys and dolls are scattered in the floor ",
                )
        cave_350 = caves.Cave(
                "Courtyard",
                "Picnic tables are beamed on by the sun ",
                )

        cave_351 = caves.Cave(
                "murky pond",
                "nothing to see here"
                )

        cave_352 = caves.Cave(
                "dirty lake",
                "nothing to see here ",
                )
        
        cave_353 = caves.Cave(
                "dark closet",
                "nothing to see here ",
                )

        cave_354 = caves.Cave(
                "kitchen",
                "watch out",
                )
        
        cave_355 = caves.Cave(
                "moldy dock",
                "close",
                )
        cave_356 = caves.Cave(
                "living room",
                "you are dead",
                )
        
        cave_357 = caves.Cave(
                "banquet room",
                "how are you here",
                )
        cave_358 = caves.Cave(
                "main throne",
                "watch out",
                )
        
        cave_359 = caves.Cave(
                "office",
                " close",
                )

        cave_360 = caves.Cave(
                "bedroom",
                " nothing to do here",
                )
        
        cave_361 = caves.Cave(
                "locker room",
                " way off",
                )

        cave_362 = caves.Cave(
                "stage",
                "far far away",
                
                )
        
        cave_363 = caves.Cave(
                "weight room",
                " a little farther",
                )
        cave_364 = caves.Cave(
                "bar",
                " wrong way",
                )
        
        cave_365 = caves.Cave(
                "Sacred Balcony",
                " right path",
                )
        cave_366 = caves.Cave(
                "ski resort",
                "keep going ",
                )
        
        cave_367 = caves.Cave(
                "stroage room",
                " got you",
                )

        cave_368 = caves.Cave(
                "furnace",
                " keep going",
                )
        
        cave_369 = caves.Cave(
                "fire pit",
                "nothing to see here",
                )

        cave_370 = caves.Cave(
                "room of the press",
                "nothing to see here",
                )
        
        cave_371 = caves.Cave(
                "chapel",
                "right way ",
                )
        cave_372 = caves.Cave(
                "green house",
                "wrong way",
                )
        
        cave_373 = caves.Cave(
                "shed",
                "wrong way",
                )
        cave_374 = caves.Cave(
                "out house",
                "keep going ",
                )
        
        cave_375 = caves.Cave(
                "lab",
                "keep trying ",
                )
        

        

#MISC


        cave_800 = caves.Cave(
                "Dragon's Lair",
                " ",
                )

        cave_900 = caves.Cave(
                "Path to the Kingdom of Rhonea",
                " ",
                )
        cave_400 = caves.Cave(
                "Dark Elves Kingdom",
                " ",
                )

#Village
        cave_501 = caves.Cave(
                "Temple of Dranyst",
                " ",
                )
        
        cave_502 = caves.Cave(
                "Alley",
                " ",
                )

        cave_503 = caves.Cave(
                "Apothecary",
                " ",
                )
        
        cave_504 = caves.Cave(
                "Weapon Shop",
                " ",
                )
        cave_505 = caves.Cave(
                "North Main Street",
                " ",
                )
        
        cave_506 = caves.Cave(
                "Gildra's Tavern",
                " ",
                )
        cave_507 = caves.Cave(
                "Armory",
                " ",
                )
        
        cave_508 = caves.Cave(
                "Town Square",
                " ",
                )

        cave_509 = caves.Cave(
                "Bank",
                " ",
                )
        
        cave_510 = caves.Cave(
                "General Store",
                " ",
                )

        cave_511 = caves.Cave(
                "South Main Street",
                " ",
                )
        
        cave_512 = caves.Cave(
                "Eastern Quarter",
                " ",
                )
        cave_513 = caves.Cave(
                "Town Hall",
                " ",
                )
        
        cave_514 = caves.Cave(
                "Sheriff's Office",
                " ",
                )
        cave_515 = caves.Cave(
                "Southern Gates",
                " ",
                )
        
        cave_516 = caves.Cave(
                "Kerelle's Hotel",
                " ",
                )

        cave_517 = caves.Cave(
                "Mayor's Office",
                " ",
                )
        
        cave_518 = caves.Cave(
                "Entrance to the town of Broaven",
                " ",
                )
    #Sewers

        cave_601 = caves.Cave(
                "Northeast Corner",
                " ",
                )
        
        cave_602 = caves.Cave(
                "Sewer Rat's Lair",
                " ",
                )

        cave_603 = caves.Cave(
                "Sewer Entrance",
                " ",
                )
        
        cave_604 = caves.Cave(
                "Muddy Tunnel",
                " ",
                )
        cave_605 = caves.Cave(
                "Mud Monster ",
                " ",
                )
        
        cave_606 = caves.Cave(
                "Dead End",
                " ",
                )
        cave_607 = caves.Cave(
                "Northern Flooded Tunnel",
                " ",
                )
        
        cave_608 = caves.Cave(
                "Collapsed Tunnel",
                " ",
                )

        cave_609 = caves.Cave(
                "Northern Sewer Junction",
                " ",
                )
        
        cave_610 = caves.Cave(
                "Moldy Tunnel",
                " ",
                )

        cave_611 = caves.Cave(
                "Damp Turn",
                " ",
                )
        
        cave_612 = caves.Cave(
                "Mocker's Hideout",
                " ",
                )
        cave_613 = caves.Cave(
                "Southern Flooded Tunnel",
                " ",
                )
        
        cave_614 = caves.Cave(
                "Collapsed Wall",
                " ",
                )
        cave_615 = caves.Cave(
                "Empty Passage",
                " ",
                )
        
        cave_616 = caves.Cave(
                "Long Tunnel",
                "",
                )

        cave_617 = caves.Cave(
                "Eastern Sewer Junction",
                "",
                )
        
        cave_618 = caves.Cave(
                "Thieve's Den",
                "",
                )

        cave_619 = caves.Cave(
                "Sunken Floor",
                "",
                )
        
        cave_620 = caves.Cave(
                "Murky Pool",
                "",
                )
        cave_621 = caves.Cave(
                "Southern Sewer Junction",
                "",
                )
        
        cave_622 = caves.Cave(
                "Sloped Passage",
                " ",
                )
        cave_623 = caves.Cave(
                "Rotting Debris",
                " ",
                )
        
        cave_624 = caves.Cave(
                "Bone Pile",
                "A pile of human bones is stacked up along the wall  ",
                )

        cave_625 = caves.Cave(
                "Snake Skin",
                "A very large snake skin lies on the floor",
                )
        
        cave_626 = caves.Cave(
                "Musty Tunnel",
                " ",
                )


        cave_627 = caves.Cave(
                "Dark Corridor",
                " ",
                )

        cave_628= caves.Cave(
                "Goblin Caves",
                "You are in a corridor that stretches for a distance into the darkness",
                )
        
        cave_629 = caves.Cave(
                "Goblin Caves",
                " ",
                )
        cave_630 = caves.Cave(
                "Dark Cavern",
                "",
                )
        
        cave_631 = caves.Cave(
                "Anaconda Lair",
                " ",
                )
        cave_632 = caves.Cave(
                "Blackened Walls",
                "",
                )
        
        cave_633 = caves.Cave(
                "Dripping Ceiling",
                "",
                )

        cave_634 = caves.Cave(
                "Goblin Treasure Room",
                "",
                )
        
        cave_635 = caves.Cave(
                "Goblin Temple",
                " ",
                )

        cave_636 = caves.Cave(
                "Goblin Leader's Cave",
                " ",
                )


        cave_1000 = caves.Cave(
                "Dump",
                " ",
                )
#Valmoor
        cave_0.tunnels = {'north' : None , 'south' : cave_2, 'east' : None, 'west': None, 'up' : None, 'down' : None}       
        cave_1.tunnels = {'north' : None , 'south' : cave_7, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_2.tunnels = {'north' : None , 'south' : cave_8, 'east' : cave_3, 'west': cave_118, 'up' : None, 'down' : None} 
        cave_3.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_2, 'up' : None, 'down' : None}
        cave_4.tunnels = {'north' : None , 'south' : cave_10, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_5.tunnels = {'north' : None , 'south' : None, 'east' :  cave_6, 'west': None, 'up' : None, 'down' : None}
        cave_6.tunnels = {'north' : None , 'south' : cave_13, 'east' : cave_7, 'west': cave_5, 'up' : None, 'down' : None}
        cave_7.tunnels = {'north' : cave_1 , 'south' : None, 'east' : cave_8, 'west': cave_6, 'up' : None, 'down' : None}
        cave_8.tunnels = {'north' : cave_2 , 'south' : cave_15, 'east' : cave_9, 'west': cave_7, 'up' : None, 'down' : None}  
        cave_9.tunnels = {'north' : None , 'south' : cave_16, 'east' : cave_10, 'west': cave_8, 'up' : None, 'down' : None}
        cave_10.tunnels = {'north' : cave_4 , 'south' : cave_17, 'east' : 'door', 'west': cave_9, 'up' : None, 'down' : None} 
        cave_11.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': 'door', 'up' : None, 'down' : None}
        cave_12.tunnels = {'north' : None, 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : 'door'}
        cave_13.tunnels = {'north' : cave_6 , 'south' : cave_19, 'east' : None, 'west': None, 'up' : 'door', 'down' : None}  
        cave_14.tunnels = {'north' : None , 'south' : None, 'east' : cave_15, 'west': None, 'up' : None, 'down' : None}
        cave_15.tunnels = {'north' : cave_8 , 'south' : None, 'east' : cave_16, 'west': cave_14, 'up' : None, 'down' : None}
        cave_16.tunnels = {'north' : cave_9 , 'south' : None, 'east' : cave_17, 'west': cave_15, 'up' : None, 'down' : None}  
        cave_17.tunnels = {'north' : cave_10 , 'south' : cave_23, 'east' : None , 'west': cave_16, 'up' : 'door', 'down' : None}
        cave_18.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : 'door'} 
        cave_19.tunnels = {'north' : cave_13 , 'south' : 'door', 'east' : cave_20, 'west': None, 'up' : None, 'down' : None}
        cave_20.tunnels = {'north' : None , 'south' : None, 'east' : cave_21, 'west': cave_19, 'up' : None, 'down' : None}
        cave_21.tunnels = {'north' : None , 'south' : cave_27, 'east' : cave_22, 'west': cave_20, 'up' : None, 'down' : None}
        cave_22.tunnels = {'north' : None , 'south' : None, 'east' : cave_23, 'west': cave_21, 'up' : None, 'down' : None}
        cave_23.tunnels = {'north' : cave_17 , 'south' : cave_29, 'east' : cave_24, 'west': cave_22, 'up' : None, 'down' : None}
        cave_24.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_23, 'up' : None, 'down' : None}        
        cave_25.tunnels = {'north' : 'door', 'south' : cave_31, 'east' : cave_26, 'west': None, 'up' : None, 'down' : None}
        cave_26.tunnels = {'north' : None , 'south' : None, 'east' : cave_27, 'west': cave_25, 'up' : None, 'down' : None}  
        cave_27.tunnels = {'north' : cave_21 , 'south' : None, 'east' : 'door', 'west': cave_26, 'up' : None, 'down' : None} 
        cave_28.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': 'door', 'up' : None, 'down' : None}
        cave_29.tunnels = {'north' : cave_23 , 'south' : cave_34, 'east' : cave_30, 'west': None, 'up' : None, 'down' : None}
        cave_30.tunnels = {'north' : None , 'south' : cave_35, 'east' : None, 'west': cave_29, 'up' : None, 'down' : None}  
        cave_31.tunnels = {'north' : cave_25 , 'south' : None, 'east' : cave_32, 'west': None, 'up' : None, 'down' : None}
        cave_32.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_31, 'up' : None, 'down' : None}       
        cave_33.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': None, 'up' : 'door', 'down' : None}  
        cave_34.tunnels = {'north' : cave_29 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_35.tunnels = {'north' : cave_30 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}
#Forest
        cave_101.tunnels = {'north' : None , 'south' : cave_107, 'east' : cave_102, 'west': None, 'up' : None, 'down' : None}
        cave_102.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_101, 'up' : None, 'down' : None} 
        cave_103.tunnels = {'north' : cave_518 , 'south' : cave_109, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_104.tunnels = {'north' : None , 'south' : cave_110, 'east' : cave_105, 'west': None, 'up' : None, 'down' : None}
        cave_105.tunnels = {'north' : None , 'south' : None, 'east' :  cave_106, 'west': cave_104, 'up' : None, 'down' : None}
        cave_106.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_105, 'up' : None, 'down' : None}
        cave_107.tunnels = {'north' : cave_101 , 'south' : cave_113, 'east' : cave_108, 'west': None, 'up' : None, 'down' : None}
        cave_108.tunnels = {'north' : None , 'south' : cave_114, 'east' : cave_109, 'west': cave_107, 'up' : None, 'down' : None}  
        cave_109.tunnels = {'north' : cave_103 , 'south' : cave_115, 'east' : cave_110, 'west': cave_108, 'up' : None, 'down' : None}
        cave_110.tunnels = {'north' : cave_104 , 'south' : None, 'east' : cave_111, 'west': cave_109, 'up' : None, 'down' : None} 
        cave_111.tunnels = {'north' : None , 'south' : cave_117, 'east' : None, 'west': cave_110, 'up' : None, 'down' : None}
        cave_112.tunnels = {'north' : None, 'south' : cave_118, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_113.tunnels = {'north' : cave_107 , 'south' : None, 'east' : cave_114, 'west': cave_800, 'up' : None, 'down' : None}  
        cave_114.tunnels = {'north' : cave_108 , 'south' : cave_120, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_115.tunnels = {'north' : cave_109 , 'south' : cave_121, 'east' : cave_116, 'west': None, 'up' : None, 'down' : None}
	cave_116.tunnels = {'north' : None, 'south' : None, 'east' : cave_117, 'west' : cave_115, 'up' : None, 'down' : None}        
	cave_117.tunnels = {'north' : cave_111 , 'south' : cave_123, 'east' : cave_118 , 'west': cave_116, 'up' : None, 'down' : None}
	cave_118.tunnels = {'north' : cave_112 , 'south' : None, 'east' : cave_2, 'west': cave_117, 'up' : None, 'down' : None}        
	cave_119.tunnels = {'north' : None , 'south' : None, 'east' : cave_120, 'west': None, 'up' : None, 'down' : None}     
   	cave_120.tunnels = {'north' : cave_114 , 'south' : cave_126, 'east' : cave_121, 'west': cave_119, 'up' : None, 'down' : cave_630}
        cave_121.tunnels = {'north' : cave_115 , 'south' : cave_127, 'east' : cave_122, 'west': cave_120, 'up' : None, 'down' : None}       
	cave_122.tunnels = {'north' : None , 'south' : None, 'east' : cave_123, 'west': cave_121, 'up' : None, 'down' : None}        
	cave_123.tunnels = {'north' : cave_117 , 'south' : None, 'east' : cave_124, 'west': cave_122, 'up' : None, 'down' : None}       
	cave_124.tunnels = {'north' : None , 'south' : None, 'east' : cave_301, 'west': cave_123, 'up' : None, 'down' : None}               
	cave_125.tunnels = {'north' : None  , 'south' : cave_131, 'east' : cave_126, 'west': cave_201, 'up' : None, 'down' : None}        
	cave_126.tunnels = {'north' : cave_120 , 'south' : cave_132, 'east' : None, 'west': cave_125, 'up' : None, 'down' : None}          
	cave_127.tunnels = {'north' : cave_121 , 'south' : cave_133, 'east' : cave_128, 'west': None, 'up' : None, 'down' : None}         
	cave_128.tunnels = {'north' : None , 'south' : None, 'east' : cave_129, 'west': cave_127, 'up' : None, 'down' : None}       
	cave_129.tunnels = {'north' : None , 'south' : cave_135, 'east' : cave_130, 'west': cave_128, 'up' : None, 'down' : None}       
	cave_130.tunnels = {'north' : None , 'south' : None, 'east' : cave_326, 'west': cave_129, 'up' : None, 'down' : None}          
	cave_131.tunnels = {'north' : cave_125 , 'south' : None, 'east' : None, 'west': cave_221, 'up' : None, 'down' : None}        
	cave_132.tunnels = {'north' : cave_126 , 'south' : None, 'east' : cave_133, 'west': None, 'up' : None, 'down' : None}               
	cave_133.tunnels = {'north' : cave_127 , 'south' : None, 'east' : None, 'west': cave_132, 'up' : None, 'down' : None}          
	cave_134.tunnels = {'north' : None , 'south' : None, 'east' : cave_135, 'west': None, 'up' : None, 'down' : None}        
	cave_135.tunnels = {'north' : cave_129 , 'south' : None, 'east' : cave_136, 'west': cave_134, 'up' : None, 'down' : None}  
        cave_136.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west' : cave_135, 'up' : None, 'down' : None}
        cave_800.tunnels = {'north' : None , 'south' : None, 'east' : cave_113, 'west' : None, 'up' : None, 'down' : None}
        cave_900.tunnels = {'north' : cave_131 , 'south' : None, 'east' : None, 'west' : None, 'up' : None, 'down' : None}
        cave_400.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west' : None, 'up' : None, 'down' : cave_130}

#Crydee

        cave_201.tunnels = {'north' : None , 'south' : cave_125, 'east' : 'door', 'west': cave_202, 'up' : None, 'down' : None}
        cave_202.tunnels = {'north' : None , 'south' : None, 'east' : cave_201, 'west': cave_203, 'up' : None, 'down' : None} 
        cave_203.tunnels = {'north' : 'door' , 'south' : None, 'east' : cave_202, 'west': cave_204, 'up' : None, 'down' : None}
        cave_204.tunnels = {'north' : cave_207 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_205.tunnels = {'north' : cave_206, 'south' : 'door', 'east' :  cave_215, 'west': None, 'up' : None, 'down' : None}
        cave_206.tunnels = {'north' : 'door' , 'south' : cave_205, 'east' : cave_209, 'west': 'door', 'up' : None, 'down' : None}
        cave_207.tunnels = {'north' : cave_204 , 'south' : None, 'east' : 'door', 'west': None, 'up' : None, 'down' : None}
        cave_208.tunnels = {'north' : cave_223 , 'south' : 'door', 'east' : None, 'west': None, 'up' : None, 'down' : None}  
        cave_209.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_206, 'up' : None, 'down' : None}
        cave_210.tunnels = {'north' : None , 'south' : None, 'east' : cave_214, 'west': None, 'up' : None, 'down' : None} 
        cave_211.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_214, 'up' : None, 'down' : None}
        cave_212.tunnels = {'north' : None , 'south' : None, 'east' : cave_217, 'west': cave_216, 'up' : None, 'down' : None}
        cave_213.tunnels = {'north' : cave_214 , 'south' : None, 'east' : cave_222, 'west': None, 'up' : None, 'down' : None}  
        cave_214.tunnels = {'north' : None , 'south' : cave_213, 'east' : cave_211, 'west': cave_210, 'up' : None, 'down' : None}
        cave_215.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_205, 'up' : None, 'down' : None}
        cave_216.tunnels = {'north' : cave_219 , 'south' : None, 'east' : cave_212, 'west': 'door', 'up' : None, 'down' : None}  
        cave_217.tunnels = {'north' : cave_218 , 'south' : None, 'east' : None , 'west': cave_212, 'up' : None, 'down' : None}
        cave_218.tunnels = {'north' : cave_221, 'south' : cave_217, 'east' : None, 'west': cave_220, 'up' : None, 'down' : None} 
        cave_219.tunnels = {'north' : None , 'south' : cave_216, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_220.tunnels = {'north' : cave_222 , 'south' : None, 'east' : cave_218, 'west': cave_214, 'up' : None, 'down' : None}
        cave_221.tunnels = {'north' : None , 'south' : cave_218, 'east' : None, 'west': cave_222, 'up' : None, 'down' : None}
        cave_222.tunnels = {'north' : None , 'south' : cave_220, 'east' : cave_221, 'west': cave_213, 'up' : None, 'down' : None}
        cave_223.tunnels = {'north' : cave_224 , 'south' : cave_208, 'east' : cave_225, 'west': None, 'up' : None, 'down' : None}
        cave_224.tunnels = {'north' : None , 'south' : cave_223, 'east' : None, 'west': None, 'up' : None, 'down' : None}        
        cave_225.tunnels = {'north' : None, 'south' : None, 'east' : None, 'west': cave_223, 'up' : cave_226, 'down' : None}
        cave_226.tunnels = {'north' : None , 'south' : None, 'east' : cave_228, 'west': None, 'up' : None, 'down' : cave_225}
        cave_227.tunnels = {'north' : None, 'south' : 'door', 'east' : 'door', 'west': None, 'up' : None, 'down' : None} 
        cave_228.tunnels = {'north' : None , 'south' : None, 'east' : cave_230, 'west': cave_226, 'up' : None, 'down' : None}
        cave_229.tunnels = {'north' : None , 'south' : cave_232, 'east' : cave_231, 'west': 'door', 'up' : None, 'down' : None}
        cave_230.tunnels = {'north' : None , 'south' : cave_231, 'east' :  None, 'west': cave_228, 'up' : None, 'down' : None}
        cave_231.tunnels = {'north' : cave_230 , 'south' : cave_233, 'east' : cave_234, 'west': cave_229, 'up' : None, 'down' : cave_131}
        cave_232.tunnels = {'north' : cave_229 , 'south' : cave_236, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_233.tunnels = {'north' : cave_231 , 'south' : cave_237, 'east' : cave_240, 'west': None, 'up' : None, 'down' : None}  
        cave_234.tunnels = {'north' : cave_235 , 'south' : cave_240, 'east' : cave_241, 'west': cave_231, 'up' : None, 'down' : None}
        cave_235.tunnels = {'north' : None , 'south' : cave_234, 'east' : None, 'west': None, 'up' : None, 'down' : None} 
        cave_236.tunnels = {'north' : cave_232 , 'south' : None, 'east' : cave_237, 'west': cave_238, 'up' : None, 'down' : None}
        cave_237.tunnels = {'north' : cave_233, 'south' : None, 'east' : cave_239, 'west': cave_236, 'up' : None, 'down' : None}
        cave_238.tunnels = {'north' : None , 'south' : None, 'east' : cave_236, 'west': None, 'up' : None, 'down' : None}  
        cave_239.tunnels = {'north' : cave_240 , 'south' : None, 'east' : cave_244, 'west': cave_237, 'up' : None, 'down' : None}
        cave_240.tunnels = {'north' : cave_234 , 'south' : cave_239, 'east' : cave_245, 'west': cave_233, 'up' : None, 'down' : None}
        cave_241.tunnels = {'north' : 'door', 'south' : None, 'east' : None, 'west': cave_234, 'up' : None, 'down' : None}  
        cave_242.tunnels = {'north' : None , 'south' : 'door', 'east' : cave_243 , 'west': None, 'up' : None, 'down' : None}
        cave_243.tunnels = {'north' : None , 'south' : cave_246, 'east' : None, 'west': cave_242, 'up' : None, 'down' : None} 
        cave_244.tunnels = {'north' : cave_245 , 'south' : None, 'east' : cave_248, 'west': cave_239, 'up' : None, 'down' : None} 
        cave_245.tunnels = {'north' : None , 'south' : cave_244, 'east' : cave_247, 'west': cave_240, 'up' : None, 'down' : None}
        cave_246.tunnels = {'north' : cave_243 , 'south' : cave_247, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_247.tunnels = {'north' : cave_246 , 'south' : cave_248, 'east' : None, 'west': cave_245, 'up' : None, 'down' : None}
        cave_248.tunnels = {'north' : cave_247 , 'south' : cave_249, 'east' : None, 'west': cave_244, 'up' : None, 'down' : None}
        cave_249.tunnels = {'north' : cave_248 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}        
        cave_250.tunnels = {'north' : 'door', 'south' : None, 'east' : None, 'west': None, 'up' : cave_251, 'down' : None}
	cave_251.tunnels = {'north' : None , 'south' : cave_256, 'east' : cave_252, 'west': None, 'up' : None, 'down' : cave_250}       
        cave_252.tunnels = {'north' : None , 'south' : cave_257, 'east' : None, 'west': cave_251, 'up' : None, 'down' : None}
        cave_253.tunnels = {'north' : None , 'south' : cave_258, 'east' : None, 'west': None, 'up' : None, 'down' : None} 
        cave_254.tunnels = {'north' : None , 'south' : cave_259, 'east' : cave_255, 'west': None, 'up' : None, 'down' : None}
        cave_255.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_254, 'up' : None, 'down' : None}
        cave_256.tunnels = {'north' : cave_251 , 'south' : cave_261, 'east' :  cave_257, 'west': None, 'up' : None, 'down' : None}
        cave_257.tunnels = {'north' : cave_252 , 'south' : cave_262, 'east' : None, 'west': cave_256, 'up' : None, 'down' : None}
        cave_258.tunnels = {'north' : cave_253 , 'south' : cave_263, 'east' : cave_259, 'west': None, 'up' : None, 'down' : None}
        cave_259.tunnels = {'north' : cave_254 , 'south' : cave_264, 'east' : None, 'west': cave_258, 'up' : None, 'down' : None}  
        cave_260.tunnels = {'north' : None , 'south' : cave_265, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_261.tunnels = {'north' : cave_256 , 'south' : None, 'east' : cave_262, 'west': None, 'up' : None, 'down' : None} 
        cave_262.tunnels = {'north' : cave_257 , 'south' : cave_267, 'east' : cave_263, 'west': cave_261, 'up' : None, 'down' : None}
        cave_263.tunnels = {'north' : cave_258, 'south' : cave_268, 'east' : None, 'west': cave_262, 'up' : None, 'down' : None}
        cave_264.tunnels = {'north' : cave_259 , 'south' : None, 'east' : cave_265, 'west': None, 'up' : None, 'down' : None}  
        cave_265.tunnels = {'north' : cave_260 , 'south' : cave_270, 'east' : None, 'west': cave_264, 'up' : None, 'down' : None}
        cave_266.tunnels = {'north' : None , 'south' : cave_271, 'east' : cave_267, 'west': None, 'up' : None, 'down' : None}
        cave_267.tunnels = {'north' : cave_262 , 'south' : cave_272, 'east' : None, 'west': cave_266, 'up' : None, 'down' : None}  
        cave_268.tunnels = {'north' : cave_263 , 'south' : cave_273, 'east' : cave_269 , 'west': None, 'up' : None, 'down' : None}
        cave_269.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_268, 'up' : None, 'down' : None} 
        cave_270.tunnels = {'north' : cave_265 , 'south' : cave_275, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_271.tunnels = {'north' : cave_266 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_272.tunnels = {'north' : cave_267 , 'south' : None, 'east' : cave_273, 'west': None, 'up' : None, 'down' : None}
        cave_273.tunnels = {'north' : cave_268 , 'south' : None, 'east' : None, 'west': cave_272, 'up' : None, 'down' : None}
        cave_274.tunnels = {'north' : None , 'south' : None, 'east' : cave_275, 'west': None, 'up' : None, 'down' : None}
        cave_275.tunnels = {'north' : cave_270 , 'south' : None, 'east' : None, 'west': cave_274, 'up' : None, 'down' : None} 
#Dorlaan

        cave_301.tunnels = {'north' : None , 'south' : cave_302, 'east' : None, 'west': cave_124, 'up' : None, 'down' : None}
        cave_302.tunnels = {'north' : cave_301 , 'south' : cave_303, 'east' : cave_304, 'west': None, 'up' : None, 'down' : None} 
        cave_303.tunnels = {'north' : cave_302 , 'south' : None, 'east' : cave_305, 'west': None, 'up' : None, 'down' : None}
        cave_304.tunnels = {'north' : None , 'south' : cave_305, 'east' : None, 'west': cave_302, 'up' : None, 'down' : None}
        cave_305.tunnels = {'north' : cave_304 , 'south' : None, 'east' :  cave_306, 'west': cave_303, 'up' : None, 'down' : None}
        cave_306.tunnels = {'north' : cave_307 , 'south' : None, 'east' : None, 'west': cave_305, 'up' : None, 'down' : None}
        cave_307.tunnels = {'north' : cave_308 , 'south' : cave_306, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_308.tunnels = {'north' :  None, 'south' : cave_307, 'east' : cave_309, 'west': None, 'up' : None, 'down' : None}  
        cave_309.tunnels = {'north' : None , 'south' : cave_310, 'east' : cave_308 , 'west': None, 'up' : None, 'down' : None}
        cave_310.tunnels = {'north' : cave_309 , 'south' : cave_311, 'east' : None, 'west': None, 'up' : None, 'down' : None} 
        cave_311.tunnels = {'north' : cave_310 , 'south' : cave_312, 'east' : cave_15, 'west': cave_306, 'up' : None, 'down' : None}
        cave_312.tunnels = {'north' : cave_311, 'south' : None, 'east' : None, 'west': cave_313, 'up' : None, 'down' : None }
        cave_313.tunnels = {'north' : None , 'south' : cave_314, 'east' : cave_312, 'west': None, 'up' : None, 'down' : None}  
        cave_314.tunnels = {'north' : cave_313 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_315.tunnels = {'north' : cave_316 , 'south' : None, 'east' : None, 'west': cave_311, 'up' : None, 'down' : None}
        cave_316.tunnels = {'north' : cave_318 , 'south' : cave_315, 'east' : None, 'west': None, 'up' : None, 'down' : None}  
        cave_317.tunnels = {'north' : cave_319 , 'south' : cave_322, 'east' : None , 'west': cave_315, 'up' : None, 'down' : None}
        cave_318.tunnels = {'north' : None , 'south' : cave_316, 'east' : None, 'west': None, 'up' : None, 'down' : None } 
        cave_319.tunnels = {'north' : cave_320 , 'south' : cave_317, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_320.tunnels = {'north' : None , 'south' : cave_319, 'east' : None, 'west': cave_321, 'up' : None, 'down' : None}
        cave_321.tunnels = {'north' : None , 'south' : None , 'east' : cave_320, 'west': None, 'up' : None, 'down' : None}
        cave_322.tunnels = {'north' : cave_317 , 'south' : cave_325, 'east' : None, 'west': cave_323, 'up' : None, 'down' : None}
        cave_323.tunnels = {'north' :  None, 'south' : cave_324, 'east' : cave_322, 'west':None , 'up' : None, 'down' : None}
        cave_324.tunnels = {'north' : cave_323 , 'south' : 'door', 'east' : None, 'west': cave_23, 'up' : None, 'down' : None}        
        cave_325.tunnels = {'north' : cave_322, 'south' : cave_329, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_326.tunnels = {'north' : None , 'south' : cave_331, 'east' : cave_327, 'west': cave_130, 'up' : None, 'down' : None}       
        cave_327.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_326, 'up' : None, 'down' : None}
        cave_328.tunnels = {'north' : 'door' , 'south' : cave_333, 'east' : cave_329, 'west': None, 'up' : None, 'down' : None} 
        cave_329.tunnels = {'north' : cave_325 , 'south' : cave_334, 'east' : None, 'west': cave_328, 'up' : None, 'down' : None}
        cave_330.tunnels = {'north' : None , 'south' : cave_335, 'east' : None, 'west': None, 'up' : None, 'down' : cave_343}
        cave_331.tunnels = {'north' : cave_326 , 'south' : cave_336, 'east' :  cave_332, 'west': None, 'up' : None, 'down' : None}
        cave_332.tunnels = {'north' : None , 'south' : cave_337, 'east' : cave_333, 'west': cave_331, 'up' : None, 'down' : None}
        cave_333.tunnels = {'north' : cave_328 , 'south' : 'door', 'east' : cave_334, 'west': cave_332, 'up' : None, 'down' : None}
        cave_334.tunnels = {'north' : cave_329 , 'south' : cave_339, 'east' : cave_335, 'west': cave_333, 'up' : None, 'down' : None}  
        cave_335.tunnels = {'north' : cave_330 , 'south' : None, 'east' : None, 'west': cave_334, 'up' : None, 'down' : None}
        cave_336.tunnels = {'north' : cave_331 , 'south' : None, 'east' : cave_337, 'west': None, 'up' : None, 'down' : None} 
        cave_337.tunnels = {'north' : cave_332 , 'south' : cave_342 , 'east' : None, 'west': cave_336, 'up' : None, 'down' : None}
        cave_338.tunnels = {'north' : 'door' , 'south' : None, 'east' : None , 'west': None, 'up' : None, 'down' : cave_341}
        cave_339.tunnels = {'north' : cave_334 , 'south' : cave_344, 'east' : cave_340, 'west': None, 'up' : 'door', 'down' : None}  
        cave_340.tunnels = {'north' : None , 'south' : cave_345, 'east' : None, 'west': cave_339, 'up' : None, 'down' : None}
        cave_341.tunnels = {'north' : None , 'south' : 'door', 'east' : None, 'west': None, 'up' : cave_338, 'down' : None}
        cave_342.tunnels = {'north' : cave_347 , 'south' : cave_347, 'east' : cave_343, 'west': None, 'up' : None, 'down' : None}  
        cave_343.tunnels = {'north' : None , 'south' : cave_348, 'east' : cave_344 , 'west': cave_342, 'up' : 'door', 'down' : None}
        cave_344.tunnels = {'north' : cave_339 , 'south' : cave_349, 'east' : cave_345, 'west': cave_343, 'up' : None, 'down' : 'door'} 
        cave_345.tunnels = {'north' : cave_340 , 'south' : 'door', 'east' : None, 'west': cave_344, 'up' : None, 'down' : None}
        cave_346.tunnels = {'north' : 'door' , 'south' : None, 'east' : cave_347, 'west': None, 'up' : None, 'down' : None}
        cave_347.tunnels = {'north' : cave_342 , 'south' : None, 'east' : cave_348, 'west': cave_346, 'up' : None, 'down' : None}
        cave_348.tunnels = {'north' : cave_343 , 'south' : None, 'east' : cave_349, 'west': cave_347, 'up' : None, 'down' : None}
        cave_349.tunnels = {'north' : cave_344 , 'south' : None, 'east' : None, 'west': cave_348, 'up' : None, 'down' : None}
        cave_350.tunnels = {'north' : 'door' , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : 'door'}
        cave_351.tunnels = {'north' : cave_352 , 'south' : None, 'east' : cave_368, 'west': None, 'up' : None, 'down' : None}       
        cave_352.tunnels = {'north' : None , 'south' : None, 'east' : cave_353, 'west': None, 'up' : None, 'down' : None}
        cave_353.tunnels = {'north' : None , 'south' : None, 'east' : cave_354, 'west': cave_352, 'up' : None, 'down' : None} 
        cave_354.tunnels = {'north' : cave_355 , 'south' : None, 'east' : None, 'west': cave_353, 'up' : None, 'down' : None}
        cave_355.tunnels = {'north' : cave_360 , 'south' : cave_354, 'east' : None, 'west': cave_356, 'up' : None, 'down' : None}
        cave_356.tunnels = {'north' : cave_357 , 'south' : None, 'east' :  cave_355, 'west': None, 'up' : None, 'down' : None}
        cave_357.tunnels = {'north' : cave_359 , 'south' : cave_356, 'east' : None, 'west': 'door', 'up' : None, 'down' : None}
        cave_358.tunnels = {'north' : None , 'south' : None, 'east' : 'door' , 'west': None, 'up' : None, 'down' : None}
        cave_359.tunnels = {'north' : None , 'south' : cave_357, 'east' : None, 'west': None, 'up' : None, 'down' : None}  
        cave_360.tunnels = {'north' : None , 'south' : cave_355, 'east' : cave_361, 'west': None, 'up' : None, 'down' : None}
        cave_361.tunnels = {'north' : cave_365 , 'south' : cave_362, 'east' : cave_363, 'west': cave_360, 'up' : None, 'down' : None} 
        cave_362.tunnels = {'north' : cave_361 , 'south' : None, 'east' : None, 'west': None ,'up' : None, 'down' : None}
        cave_363.tunnels = {'north' : None, 'south' : None, 'east' : None, 'west': cave_361, 'up' : cave_364, 'down' : 'door'}
        cave_364.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': None, 'up' : 'door', 'down' : cave_363}  
        cave_365.tunnels = {'north' : None , 'south' : cave_361, 'east' : None, 'west': cave_366, 'up' : 'door' , 'down' : None}
        cave_366.tunnels = {'north' : None , 'south' : None, 'east' : cave_365, 'west': None, 'up' : cave_367, 'down' : None}
        cave_367.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : cave_366}  
        cave_368.tunnels = {'north' : None , 'south' : None, 'east' : cave_369 , 'west': cave_351, 'up' : 'door', 'down' : None}
        cave_369.tunnels = {'north' : None , 'south' : None, 'east' : cave_370, 'west': cave_368, 'up' : None, 'down' : 'door'} 
        cave_370.tunnels = {'north' : cave_374 , 'south' : cave_372, 'east' : cave_371, 'west': cave_369, 'up' : None, 'down' : None}
        cave_371.tunnels = {'north' : cave_375 , 'south' : cave_373, 'east' : None, 'west': cave_370, 'up' : None, 'down' : None}
        cave_372.tunnels = {'north' : cave_370 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_373.tunnels = {'north' : cave_371 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_374.tunnels = {'north' : None , 'south' : cave_370, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_375.tunnels = {'north' : None , 'south' : cave_371, 'east' : None, 'west': None, 'up' : None, 'down' : None}        

       

#Village
        cave_501.tunnels = {'north' : None , 'south' : None, 'east' : cave_502, 'west': None, 'up' : None, 'down' : None}
        cave_502.tunnels = {'north' : None , 'south' : cave_505, 'east' : cave_503, 'west': cave_501, 'up' : None, 'down' : cave_603} 
        cave_503.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_502, 'up' : None, 'down' : None}
        cave_504.tunnels = {'north' : None , 'south' : None, 'east' : cave_505, 'west': None, 'up' : None, 'down' : None}
        cave_505.tunnels = {'north' : cave_502 , 'south' : cave_508, 'east' :  cave_506, 'west': cave_504, 'up' : None, 'down' : None}
        cave_506.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_505, 'up' : None, 'down' : None}
        cave_507.tunnels = {'north' : None, 'south' : None, 'east' : cave_508, 'west': None, 'up' : None, 'down' : None}
        cave_508.tunnels = {'north' : cave_505 , 'south' : cave_511, 'east' : cave_509, 'west': cave_507, 'up' : None, 'down' : None}  
        cave_509.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_508, 'up' : None, 'down' : None}
        cave_510.tunnels = {'north' : None , 'south' : None, 'east' : cave_511, 'west': None, 'up' : None, 'down' : None} 
        cave_511.tunnels = {'north' : cave_508 , 'south' : cave_515, 'east' : cave_512, 'west': cave_510, 'up' : None, 'down' : None}
        cave_512.tunnels = {'north' : None, 'south' : cave_516, 'east' : cave_513, 'west': cave_511, 'up' : None, 'down' : None}
        cave_513.tunnels = {'north' : None , 'south' : cave_517 , 'east' : None, 'west': cave_512, 'up' : None, 'down' : None}  
        cave_514.tunnels = {'north' : None , 'south' : None, 'east' : cave_515, 'west': None, 'up' : None, 'down' : None}
        cave_515.tunnels = {'north' : cave_511 , 'south' : cave_518, 'east' : None, 'west': cave_514, 'up' : None, 'down' : None}
	cave_516.tunnels = {'north' : cave_512, 'south' : None, 'east' : None, 'west' : None, 'up' : None, 'down' : None}        
	cave_517.tunnels = {'north' : cave_513 , 'south' : None, 'east' : None , 'west': None, 'up' : None, 'down' : None}
	cave_518.tunnels = {'north' : cave_515 , 'south' : cave_103, 'east' : None, 'west': None, 'up' : None, 'down' : None}        
#Sewers

	cave_601.tunnels = {'north' : None , 'south' : cave_607, 'east' : cave_602, 'west': None, 'up' : None, 'down' : None}
        cave_602.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_601, 'up' : None, 'down' : None} 
        cave_603.tunnels = {'north' : None, 'south' : cave_609, 'east' : None, 'west': None, 'up' : cave_502, 'down' : None}
        cave_604.tunnels = {'north' : None , 'south' : cave_610, 'east' : cave_605, 'west': None, 'up' : None, 'down' : None}
        cave_605.tunnels = {'north' : None , 'south' : None, 'east' :  cave_606, 'west': cave_604, 'up' : None, 'down' : None}
        cave_606.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_605, 'up' : None, 'down' : None}
        cave_607.tunnels = {'north' : cave_601 , 'south' : cave_613, 'east' : cave_608, 'west': None, 'up' : None, 'down' : None}
        cave_608.tunnels = {'north' : None , 'south' : cave_614, 'east' : cave_609, 'west': cave_607, 'up' : None, 'down' : None}  
        cave_609.tunnels = {'north' : cave_603 , 'south' : cave_615, 'east' : cave_610, 'west': cave_608, 'up' : None, 'down' : None}
        cave_610.tunnels = {'north' : cave_604 , 'south' : None, 'east' : cave_611, 'west': cave_609, 'up' : None, 'down' : None} 
        cave_611.tunnels = {'north' : None , 'south' : cave_617, 'east' : None, 'west': cave_610, 'up' : None, 'down' : None}
        cave_612.tunnels = {'north' : None, 'south' : cave_618, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_613.tunnels = {'north' : cave_607 , 'south' : None, 'east' : cave_614, 'west': None, 'up' : None, 'down' : None}  
        cave_614.tunnels = {'north' : cave_608 , 'south' : cave_620, 'east' : None, 'west': None, 'up' : None, 'down' : None}
        cave_615.tunnels = {'north' : cave_609 , 'south' : cave_621, 'east' : cave_616, 'west': None, 'up' : None, 'down' : None}
	cave_616.tunnels = {'north' : None, 'south' : None, 'east' : cave_617, 'west' : cave_615, 'up' : None, 'down' : None}        
	cave_617.tunnels = {'north' : cave_611 , 'south' : cave_623, 'east' : cave_618 , 'west': cave_616, 'up' : None, 'down' : None}
	cave_618.tunnels = {'north' : cave_612 , 'south' : None, 'east' : None, 'west': cave_617, 'up' : None, 'down' : None}        
	cave_619.tunnels = {'north' : None , 'south' : None, 'east' : cave_620, 'west': None, 'up' : None, 'down' : None}     
   	cave_620.tunnels = {'north' : cave_614 , 'south' : cave_626, 'east' : cave_621, 'west': cave_619, 'up' : None, 'down' : None}
        cave_621.tunnels = {'north' : cave_615 , 'south' : cave_627, 'east' : cave_622, 'west': cave_620, 'up' : None, 'down' : None}       
	cave_622.tunnels = {'north' : None , 'south' : None, 'east' : cave_623, 'west': cave_621, 'up' : None, 'down' : None}        
	cave_623.tunnels = {'north' : cave_617 , 'south' : None, 'east' : cave_624, 'west': cave_622, 'up' : None, 'down' : None}       
	cave_624.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_623, 'up' : None, 'down' : None}               
	cave_625.tunnels = {'north' : None  , 'south' : cave_631, 'east' : cave_626, 'west': None, 'up' : None, 'down' : None}        
	cave_626.tunnels = {'north' : cave_620 , 'south' : cave_632, 'east' : None, 'west': cave_625, 'up' : None, 'down' : None}          
	cave_627.tunnels = {'north' : cave_621 , 'south' : cave_633, 'east' : None, 'west': None, 'up' : None, 'down' : cave_628}         
	cave_628.tunnels = {'north' : None , 'south' : None, 'east' : cave_629, 'west': None, 'up' : cave_627, 'down' : None}       
	cave_629.tunnels = {'north' : None , 'south' : cave_635, 'east' : cave_630, 'west': cave_628, 'up' : None, 'down' : None}       
	cave_630.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': cave_629, 'up' : cave_120, 'down' : None}          
	cave_631.tunnels = {'north' : cave_625 , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}        
	cave_632.tunnels = {'north' : cave_626 , 'south' : None, 'east' : cave_633, 'west': None, 'up' : None, 'down' : None}               
	cave_633.tunnels = {'north' : cave_627 , 'south' : None, 'east' : None, 'west': cave_632, 'up' : None, 'down' : None}          
	cave_634.tunnels = {'north' : None , 'south' : None, 'east' : 'door', 'west': None, 'up' : None, 'down' : None}        
	cave_635.tunnels = {'north' : cave_629 , 'south' : None, 'east' : cave_636, 'west': 'door', 'up' : None, 'down' : None}  
        cave_636.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west' : cave_635, 'up' : None, 'down' : None}

        cave_1000.tunnels = {'north' : None , 'south' : None, 'east' : None, 'west': None, 'up' : None, 'down' : None}  

        self.caves = [cave_0, cave_1, cave_2, cave_3, cave_4, cave_5, cave_6, cave_7, cave_8, cave_9,
                        cave_10, cave_11, cave_12, cave_13, cave_14, cave_15, cave_16, cave_17, cave_18,
                          cave_19, cave_20, cave_21, cave_22, cave_23, cave_24, cave_25, cave_26,
                      cave_27, cave_28, cave_29, cave_30, cave_31, cave_32, cave_33, cave_34, cave_35,
                        cave_101, cave_102, cave_103, cave_104, cave_105, cave_106, cave_107, cave_108, cave_109,
                              cave_110, cave_111, cave_112, cave_113, cave_114, cave_115, cave_116, cave_117, cave_118,
                              cave_119, cave_120, cave_121, cave_122, cave_123, cave_124, cave_125, cave_126, cave_127,
                              cave_128, cave_129, cave_130, cave_131, cave_132, cave_133, cave_134, cave_135, cave_136,
                      cave_800, cave_900, cave_400, cave_1000, cave_501, cave_502, cave_503, cave_504, cave_505, cave_506, cave_507, cave_508, cave_509,
                              cave_510, cave_511, cave_512, cave_513, cave_514, cave_515, cave_516, cave_517, cave_518,
                      cave_601, cave_602, cave_603, cave_604, cave_605, cave_606, cave_607, cave_608, cave_609,
                              cave_610, cave_611, cave_612, cave_613, cave_614, cave_615, cave_616, cave_617, cave_618,
                              cave_619, cave_620, cave_621, cave_622, cave_623, cave_624, cave_625, cave_626, cave_627,
                              cave_628, cave_629, cave_630, cave_631, cave_632, cave_633, cave_634, cave_635, cave_636,
                      cave_201, cave_202, cave_203, cave_204, cave_205, cave_206, cave_207, cave_208, cave_209,
                        cave_210, cave_211, cave_212, cave_213, cave_214, cave_215, cave_216, cave_217, cave_218,
                          cave_219, cave_220, cave_221, cave_222, cave_223, cave_224, cave_225, cave_226, cave_227,
                      cave_228, cave_229, cave_230, cave_231, cave_232, cave_233, cave_234,
                        cave_235, cave_236, cave_237, cave_238, cave_239, cave_240, cave_241, cave_242, cave_243, 
                          cave_244, cave_245, cave_246, cave_247, cave_248, cave_249, cave_250, cave_251, cave_252,
                      cave_253, cave_254, cave_255, cave_256, cave_257, cave_258, cave_259,
                        cave_260, cave_261, cave_262, cave_263, cave_264, cave_265, cave_266, cave_267, cave_268,
                          cave_269, cave_270, cave_271, cave_272, cave_273, cave_274, cave_275, cave_301, cave_302,
                      cave_303, cave_304, cave_305, cave_306, cave_307, cave_308, cave_309,
                        cave_310, cave_311, cave_312, cave_313, cave_314, cave_315, cave_316, cave_317, cave_318,
                          cave_319, cave_320, cave_321, cave_322, cave_323, cave_324, cave_325, cave_326,
                      cave_327, cave_328, cave_329, cave_330, cave_331, cave_332, cave_333, cave_334, cave_335,
                       cave_336, cave_337, cave_338, cave_339, cave_340, cave_341, cave_342, cave_343, cave_344,
                        cave_345, cave_346, cave_347, cave_348, cave_349, cave_350, cave_351, cave_352, cave_353,
                          cave_354, cave_355, cave_356, cave_357, cave_358, cave_359, cave_360, cave_361,
                      cave_362, cave_363, cave_364, cave_365, cave_367, cave_368, cave_369, cave_370, cave_371,
                       cave_372, cave_373, cave_374, cave_375]




        self.players = []
        self.red_start = cave_301
        self.blue_start = cave_201
        self.reborn_loc = cave_501
        self.player_store = {}

        self.load_players()

###                                                                 ##########       Items in Game      ##############

     
 
        
#Weapon
        warhammer = items.Weapon("warhammer", "A large, steel 'warhammer'", 6, cave_1000, "WEAPON", 150, attack_roll = "1d20")   
        battle_axe = items.Weapon("axe", "A wicked looking battle 'axe'", 6, cave_1000, "WEAPON", 150, attack_roll = "2d8")
        sword = items.Weapon("sword", "A simple long 'sword'", 2, cave_1000, "WEAPON", 25, attack_roll = "1d8")
        halberd = items.Weapon("halberd", "A well polished 'halberd'", 3, cave_1000, "WEAPON", 75, attack_roll = "1d12")
        mace = items.Weapon("Mace", "A wicked looking spiked 'mace' lies here", 3, cave_1000, "WEAPON", 150, attack_roll = "2d8")

#Armor
        wooden_shield = items.Armor("shield", "A worn looking wooden 'shield'", 1, cave_1000, "ARMOR", 15, "shield", armor_class = 1) 
        steel_shield = items.Armor("steel shield", "A lightly used 'steel shield'", 5, cave_18, "ARMOR", 75, "shield", armor_class = 3)
        steel_gauntlets = items.Armor("steel gauntlets", "Shiny 'steel gauntlets' lie here", 5, cave_1000, "ARMOR", 75, "gloves", armor_class = 3)
        leather_helmet = items.Armor("leather helmet", "A rough looking 'leather helmet'", 1, cave_2, "ARMOR", 20, "helmet", armor_class = 1)
        steel_helmet = items.Armor("steel helmet", "A burnished 'steel helmet'", 2, cave_12, "ARMOR", 75, "helmet", armor_class = 3)
        leather_vest = items.Armor("leather vest", "A rough looking 'leather vest'", 2, cave_11, "ARMOR", 30,"chest", armor_class = 2)
        chain_mail = items.Armor("chain mail", "A set of used 'chain mail'", 5, cave_12, "ARMOR", 150, "chest", armor_class = 5)
        plate_mail = items.Armor("plate mail", "A well made set of 'plate mail'", 7, cave_1000, 200, "ARMOR", "chest", armor_class = 7)
        
#Potions
        blue_potion = items.Drink("blue", "A dusty bottle with a clear 'blue' liquid inside", 1, cave_1000, "DRINK", 30, 0, 0, 60)   #health
        red_potion = items.Drink("red", "A clear bottle with a glowing 'red' liquid inside", 1, cave_1000, "DRINK", 30, 1, 0, 0)    #strength
        green_potion = items.Drink("green", "An old bottle with a dark 'green' liquid inside", 1, cave_1000, "DRINK", 30, 0, 1, 0)   #dexterity

                                                                    ##########      End Items in Game      ##############

                
                                                                #################    Valmoor Castle   #####################
        crown = items.Item("gold crown", "A shiny 'gold crown'", 1, cave_33, "MISC", 0)
        gilded_key = items.Item("gilded key", "A heavy 'gilded key'", 1, cave_1000, "MISC",0)
        iron_key = items.Item("iron key", "A rusty 'iron key'", 1, cave_1000, "MISC",0)
        silver_key = items.Item("silver key", "A gleaming 'silver key'", 1, cave_1000, "MISC",0)
        golden_key = items.Item("golden key", "A solid 'golden key'", 1, cave_1000, "MISC",0)
        gold = items.Gold("gold", "'gold' coins", 0, cave_28, "GOLD", 0 , 100)
        
        rat1 = monster.Monster(cave_35, "rat", "monster", "A large, dirty rat is scurrying around the room", "AWAKE", hp = 6, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        rat2 = monster.Monster(cave_35, "rat", "monster", "A large, dirty rat is scurrying around the room", "AWAKE", hp = 6, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        rat3 = monster.Monster(cave_35, "rat", "monster", "A large, dirty rat is scurrying around the room", "AWAKE", hp = 6, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        rat4 = monster.Monster(cave_35, "rat", "monster", "A large, dirty rat is scurrying around the room", "AWAKE", hp = 6, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        rat5 = monster.Monster(cave_35, "rat", "monster", "A large, dirty rat is scurrying around the room", "AWAKE", hp = 6, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        rat6 = monster.Monster(cave_35, "rat", "monster", "A large, dirty rat is scurrying around the room", "AWAKE", hp = 6, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        rat7 = monster.Monster(cave_35, "rat", "monster", "A large, dirty rat is scurrying around the room", "AWAKE", hp = 6, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        rat8 = monster.Monster(cave_35, "rat", "monster", "A large, dirty rat is scurrying around the room", "AWAKE", hp = 6, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      

        giant_bat = monster.Monster(cave_12, "Giant Bat", "monster", "A huge bat is flying aroung the room", "AWAKE", hp = 30, armor_class = 3, attack_class = "1d8", strength=2, dexterity = 10, load = 0, maxload =10, wanderer = False)                      
        bat1 = monster.Monster(cave_12, "bat", "monster", "A small bat is flying aroung the room", "AWAKE", hp = 12, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 8, load = 0, maxload =10, wanderer = False)                      
        bat2 = monster.Monster(cave_12, "bat", "monster", "A small bat is flying aroung the room", "AWAKE", hp = 12, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 8, load = 0, maxload =10, wanderer = False)                      
        bat3 = monster.Monster(cave_12, "bat", "monster", "A small bat is flying aroung the room", "AWAKE", hp = 12, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 8, load = 0, maxload =10, wanderer = False)                      

        orc1 = monster.Monster(cave_7, "Orc", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        orc2 = monster.Monster(cave_16, "Orc", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        orc3 = monster.Monster(cave_19, "Orc", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        orc4 = monster.Monster(cave_34, "Orc", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        orc5 = monster.Monster(cave_34, "Orc", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)

        undead_soldier1 = monster.Monster(cave_3, "Undead Soldier", "monster", "An undead soldier stands guard", "AWAKE", hp = 50, armor_class = 6, attack_class = "1d8", strength=6, dexterity = 6, load = 0, maxload =10, wanderer = False)
        undead_captain = monster.Monster(cave_14, "Undead Captain", "monster", "The undead Captain of the Guard is here", "AWAKE", hp = 100, armor_class = 8, attack_class = "1d12", strength=8, dexterity = 8, load = 0, maxload =10, wanderer = False)

        queen_spider = monster.Monster(cave_18, "Queen Spider", "monster", "A massive Queen spider is sitting on her web", "AWAKE", hp = 150, armor_class = 3, attack_class = "2d8", strength=10, dexterity = 6, load = 0, maxload =10, wanderer = False)                      
      
        troll1= monster.Monster(cave_4, "Troll", "monster", "A large troll is looking at you", "AWAKE", hp = 35, armor_class = 4, attack_class = "2d6", strength=8, dexterity = 3, load = 0, maxload =10, wanderer = False)
        troll2 = monster.Monster(cave_29, "Troll", "monster", "A large troll is looking at you", "AWAKE", hp = 35, armor_class = 4, attack_class = "2d6", strength=8, dexterity = 3, load = 0, maxload =10, wanderer = False)

        viper = monster.Monster(cave_28, "Viper", "monster", "A giant viper is looking at you... it ATTACKS!!", "AWAKE", hp = 50, armor_class = 6, attack_class = "1d20", strength=8, dexterity = 3, load = 0, maxload =10, wanderer = False)

        undead_knight = monster.Monster(cave_21, "Undead Knight", "monster", "The King's Knight is here on guard", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, load = 0, maxload =10, wanderer = False)
        king = monster.Monster(cave_27, "Undead King", "monster", "The Undead King of Valmoor", "AWAKE", hp = 200, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, load = 0, maxload =10, wanderer = False)
        queen = monster.Monster(cave_32, "Undead Queen", "monster", "The Undead Queen of Valmoor", "AWAKE", hp = 125, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 6, load = 0, maxload =10, wanderer = False)
       
        orc1.wallet = 10
        orc2.wallet = 10
        orc3.inventory.append(copy.copy(blue_potion))
        orc4.wallet = 10
        orc5.wallet = 10
        undead_captain.wallet = 20
             
        troll1.inventory.append(copy.copy(red_potion))
        troll2.inventory.append(wooden_shield)
                      
        giant_bat.inventory.append(gilded_key)
        queen_spider.inventory.append(iron_key)
        undead_knight.inventory.append(halberd)
        king.inventory.append(golden_key)
        queen.inventory.append(silver_key)    

#Misc
      #  gold2 = items.Gold("gold", "'gold' coins", 0, cave_1000, "GOLD", 0 , 100)
        
        crown = items.Item("gold crown", "A shiny 'gold crown'", 1, cave_33, "MISC", 100)
        gilded_key = items.Item("gilded key", "A heavy 'gilded key'", 1, cave_1000, "MISC",5)
        iron_key = items.Item("iron key", "A rusty 'iron key'", 1, cave_1000, "MISC",5)
        silver_key = items.Item("silver key", "A gleaming 'silver key'", 1, cave_1000, "MISC",5)
        golden_key = items.Item("golden key", "A solid 'golden key'", 1, cave_1000, "MISC",5)  
#Doors

# door to armory
        door1A = items.Door("oak door", "A thick 'oak door'", 100, cave_10, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_11, "east")
        door1B = items.Door("oak door", "A thick 'oak door'", 100, cave_11, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_10, "west")
        door1A.door_pair.append(door1B)
        door1B.door_pair.append(door1A)
#door to east tower
        door6A = items.Door("wooden door", "A moldy 'wooden door'", 100, cave_17, "DOOR",0,  "CLOSED", "UNLOCKED", None, cave_18, "up")
        door6B = items.Door("wooden door", "A moldy 'wooden door'", 100, cave_18, "DOOR",0, "CLOSED", "UNLOCKED", None, cave_17, "down")
        door6A.door_pair.append(door6B)
        door6B.door_pair.append(door6A)

# door to king's quarters. Requires gilded key
        door2A = items.Door("gilded door", "A 'gilded door'", 100, cave_19, "DOOR",0, "CLOSED", "LOCKED", gilded_key, cave_25, "south")
        door2B = items.Door("gilded door", "A 'gilded door'", 100, cave_25, "DOOR",0, "CLOSED", "LOCKED", gilded_key, cave_19, "north")
        door2A.door_pair.append(door2B)
        door2B.door_pair.append(door2A)
        
#door to wizard's tower
        door3A = items.Door("iron door", "An 'iron door'", 100, cave_13, "DOOR",0, "CLOSED", "LOCKED", iron_key, cave_12, "up")
        door3B = items.Door("iron door", "An 'iron door'", 100, cave_12, "DOOR",0, "CLOSED", "LOCKED", iron_key, cave_13, "down")
        door3A.door_pair.append(door3B)
        door3B.door_pair.append(door3A)
        
#door to main treasury  

        door4A = items.Door("silver door", "A large 'silver door'", 100, cave_27,0, "DOOR", "CLOSED", "LOCKED", silver_key, cave_28, "east")
        door4B = items.Door("silver door", "A large 'silver door'", 100, cave_28,0, "DOOR", "CLOSED", "LOCKED", silver_key, cave_27, "west")
        door4A.door_pair.append(door4B)
        door4B.door_pair.append(door4A)
        
#door to secret treasury
        door5A = items.Door("Golden Throne", "A magnificent 'golden throne'", 100, cave_27, "DOOR", 0,"CLOSED", "LOCKED", golden_key, cave_33, "down")
        door5B = items.Door("Secret door", "a secret passage way leading back up", 100, cave_33, "DOOR",0, "CLOSED", "LOCKED", golden_key, cave_27, "up")
        door5A.door_pair.append(door5B)
        door5B.door_pair.append(door5A)
                                                                ######################      End Valmoor Castle    #####################


                                                                 ############   Kingdom of Crydee (200 block) - Blue team  #################

        soldier201 = soldiers.Soldier("blue", cave_206, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier202 = soldiers.Soldier("blue", cave_201, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier203 = soldiers.Soldier("blue", cave_205, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier204 = soldiers.Soldier("blue", cave_225, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier205 = soldiers.Soldier("blue", cave_215, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier206 = soldiers.Soldier("blue", cave_215, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier207 = soldiers.Soldier("blue", cave_207, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier208 = soldiers.Soldier("blue", cave_230, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier209 = soldiers.Soldier("blue", cave_235, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier210 = soldiers.Soldier("blue", cave_242, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier211 = soldiers.Soldier("blue", cave_240, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier212 = soldiers.Soldier("blue", cave_240, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier213 = soldiers.Soldier("blue", cave_239, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier214 = soldiers.Soldier("blue", cave_249, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier215 = soldiers.Soldier("blue", cave_249, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier216 = soldiers.Soldier("blue", cave_262, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier217 = soldiers.Soldier("blue", cave_262, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier218 = soldiers.Soldier("blue", cave_264, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier219 = soldiers.Soldier("blue", cave_265, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier220 = soldiers.Soldier("blue", cave_274, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
  
        captain201 = soldiers.Soldier("blue", cave_218, "Captain", "The Captain of the guard", "AWAKE", hp = 100, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 6, wanderer = False)
        captain202 = soldiers.Soldier("blue", cave_258, "Captain", "The Captain of the guard", "AWAKE", hp = 100, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 6, wanderer = False)

        knight201 = soldiers.Soldier("blue", cave_227, "Knight", "The King's Knight is here guarding the Realm", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=8, dexterity = 8, wanderer = False)
        king201 = soldiers.Soldier("blue", cave_270, "King", "The King of Dorlaan stands here", "AWAKE", hp = 200, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, wanderer = False)
        queen201 = soldiers.Soldier("blue", cave_210, "Queen", "The Queen of Dorlaan stands here", "AWAKE", hp = 125, armor_class = 6, attack_class = "1d12", strength=6, dexterity = 6, wanderer = False)

   
        soldier201.wallet = 10
        soldier206.wallet = 10
        soldier211.wallet = 10
        soldier216.wallet = 10
        soldier220.wallet = 10
        king201.wallet = 100
        queen201.wallet = 50
        captain201.inventory.append(copy.copy(halberd))     
        knight201.inventory.append(copy.copy(chain_mail))

        crown201 = items.Item("Crydee Crown", "The 'Crydee Crown'", 1, cave_274, "MISC", 100)
        sword201 = items.Weapon("sword", "A simple long 'sword'", 2, cave_201, "WEAPON", 25, attack_roll = "1d8")
        sword202 = items.Weapon("sword", "A simple long 'sword'", 2, cave_201, "WEAPON", 25, attack_roll = "1d8")
        sword203 = items.Weapon("sword", "A simple long 'sword'", 2, cave_201, "WEAPON", 25, attack_roll = "1d8")
        wooden_shield201 = items.Armor("shield", "A worn looking wooden 'shield'", 1, cave_201, "ARMOR", 15, "shield", armor_class = 1)        
        wooden_shield202 = items.Armor("shield", "A worn looking wooden 'shield'", 1, cave_201, "ARMOR", 15, "shield", armor_class = 1) 

    
	door201A = items.Door("oak door", "A thick 'oak door' to the east", 100, cave_207, "DOOR", 0,"CLOSED", "UNLOCKED", None, cave_206, "east")
	door201B = items.Door("oak door", "A thick 'oak door' to the west", 100, cave_206, "DOOR", 0,"CLOSED", "UNLOCKED", None, cave_207, "west")
	door201A.door_pair.append(door201B)
	door201B.door_pair.append(door201A)


	door202A = items.Door("gilded door", "A 'gilded door'", 100, cave_205, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_203, "south")
	door202B = items.Door("gilded door", "A 'gilded door'", 100, cave_203, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_205, "north")
	door202A.door_pair.append(door202B)
	door202B.door_pair.append(door202A)
	

	door203A = items.Door("iron door", "An 'iron door'", 100, cave_201, "DOOR", 0,"CLOSED", "UNLOCKED", None, cave_216, "east")
	door203B = items.Door("iron door", "An 'iron door'", 100, cave_216, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_201, "west")
	door203A.door_pair.append(door203B)
	door203B.door_pair.append(door203A)
 
 	


	door204A = items.Door("silver door", "A large 'silver door' to the north", 100, cave_206, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_208, "north")
	door204B = items.Door("silver door", "A large 'silver door' to the south", 100, cave_208, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_206, "south")
	door204A.door_pair.append(door204B)
	door204B.door_pair.append(door204A)
		
	door205A = items.Door("dark door", "A mysterious 'dark door'", 100, cave_270, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_275, "south")
	door205B = items.Door("dark door", "A mysterious 'dark door'", 100, cave_275, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_250, "north")
	door205A.door_pair.append(door205B)
	door205B.door_pair.append(door205A)
	

	door206A = items.Door("golden door", "A large 'golden door'", 100, cave_229, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_227, "west")
	door206B = items.Door("golden door", "A large 'golden door'", 100, cave_227, "DOOR", 0, "CLOSED", "UNLOCKED", None, cave_229, "east")
	door206A.door_pair.append(door206B)
	door206B.door_pair.append(door206A)


                                                                    ############   Kingdom of Crydee (200 block) - Blue team  #################

                                                                ############   Kingdom of Dorlaan (300 block) - Red team  #################

        soldier301 = soldiers.Soldier("red", cave_304, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier302 = soldiers.Soldier("red", cave_304, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier303 = soldiers.Soldier("red", cave_303, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier304 = soldiers.Soldier("red", cave_303, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier305 = soldiers.Soldier("red", cave_307, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier306 = soldiers.Soldier("red", cave_307, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier307 = soldiers.Soldier("red", cave_310, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier308 = soldiers.Soldier("red", cave_310, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier309 = soldiers.Soldier("red", cave_309, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier310 = soldiers.Soldier("red", cave_309, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier311 = soldiers.Soldier("red", cave_322, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier312 = soldiers.Soldier("red", cave_322, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier313 = soldiers.Soldier("red", cave_332, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier314 = soldiers.Soldier("red", cave_332, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier315 = soldiers.Soldier("red", cave_345, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier316 = soldiers.Soldier("red", cave_345, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier317 = soldiers.Soldier("red", cave_336, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier318 = soldiers.Soldier("red", cave_336, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier319 = soldiers.Soldier("red", cave_337, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
        soldier320 = soldiers.Soldier("red", cave_337, "Soldier", "A stern looking soldier stands here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, wanderer = False)
  
        captain301 = soldiers.Soldier("red", cave_308, "Captain", "The Captain of the guard", "AWAKE", hp = 100, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 6, wanderer = False)
        captain302 = soldiers.Soldier("red", cave_361, "Captain", "The Captain of the guard", "AWAKE", hp = 100, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 6, wanderer = False)

        knight301 = soldiers.Soldier("red", cave_358, "Knight", "The King's Knight is here guarding the Realm", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=8, dexterity = 8, wanderer = False)
        king301 = soldiers.Soldier("red", cave_321, "King", "The King of Dorlaan stands here", "AWAKE", hp = 200, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, wanderer = False)
        queen301 = soldiers.Soldier("red", cave_346, "Queen", "The Queen of Dorlaan stands here", "AWAKE", hp = 125, armor_class = 6, attack_class = "1d12", strength=6, dexterity = 6, wanderer = False)

   
        soldier301.wallet = 10
        soldier306.wallet = 10
        soldier311.wallet = 10
        soldier316.wallet = 10
        soldier320.wallet = 10
        king301.wallet = 100
        queen301.wallet = 50
        captain301.inventory.append(copy.copy(halberd))     
        knight301.inventory.append(copy.copy(chain_mail))

        sword301 = items.Weapon("sword", "A simple long 'sword'", 2, cave_301, "WEAPON", 25, attack_roll = "1d8")
        sword302 = items.Weapon("sword", "A simple long 'sword'", 2, cave_301, "WEAPON", 25, attack_roll = "1d8")
        sword303 = items.Weapon("sword", "A simple long 'sword'", 2, cave_301, "WEAPON", 25, attack_roll = "1d8")
        wooden_shield301 = items.Armor("shield", "A worn looking wooden 'shield'", 1, cave_301, "ARMOR", 15, "shield", armor_class = 1)        
        wooden_shield302 = items.Armor("shield", "A worn looking wooden 'shield'", 1, cave_301, "ARMOR", 15, "shield", armor_class = 1) 

        crown301 = items.Item("Dorlaan Crown", "The 'Dorlaan Crown'", 1, cave_321, "MISC", 100)

        rusty_key = items.Item("Rusty Key", "A 'rusty key'", 1, cave_308, "MISC",5)
        ruby_key = items.Item("Ruby Key", "A 'ruby key'", 1, cave_358, "MISC",5)
        black_key = items.Item("Black key", "A 'black key'", 1, cave_341, "MISC",5)
        wooden_key = items.Item("Wooden Key", "A 'wooden key'", 1, cave_338, "MISC",5)
        stone_key = items.Item("Stone key", "A 'stone key'", 1, cave_346, "MISC",5)


                
#Doors


# door to Junkyard
        door314A = items.Door("Scrapy Door", "Pile of trash awaits you'", 100, cave_324, "DOOR", 0, "CLOSED", "UNLOCKED", "Rusty Key", cave_329, "south")
        door314B = items.Door("Scrapy Door", "Pile of trash awaits you'", 100, cave_329, "DOOR", 0,"CLOSED", "UNLOCKED", "Rusty Key", cave_324, "north")
        door314A.door_pair.append(door314B)
        door314B.door_pair.append(door314A)
                            
# door to Main Throne 
        door310A = items.Door("Green Door", "Glowing door blocks you path to your destiny'", 100, cave_357, "DOOR", 0,"CLOSED", "LOCKED", "Ruby Key", cave_358, "west")
        door310B = items.Door("Green Door", "Glowing door blocks you path to your destiny'", 100, cave_358, "DOOR", 0,"CLOSED", "LOCKED", "Ruby Key", cave_357, "east")
        door310A.door_pair.append(door310B)
        door310B.door_pair.append(door310A)

# door to Sacred Balcony 
        door311A = items.Door("Rusty Gate", "Old gate covered in rust'", 100, cave_350, "DOOR", 0,"CLOSED", "LOCKED", "Black Key", cave_365, "south")
        door311B = items.Door("Rusty Gate", "Old gate covered in rust'", 100, cave_365, "DOOR", 0,"CLOSED", "LOCKED", "Black Key", cave_350, "north")
        door311A.door_pair.append(door311B)
        door311B.door_pair.append(door311A)

                            
# door to Garden
        door312A = items.Door("Vine Door '", "Vines slowly grow on the door'", 100, cave_357, "DOOR", 0,"CLOSED", "LOCKED", "Wooden Key", cave_358, "west")
        door312B = items.Door("Vine Door '", "Vines slowly grow on the door'", 100, cave_358, "DOOR", 0,"CLOSED", "LOCKED", "Wooden Key", cave_357, "east")
        door312A.door_pair.append(door312B)
        door312B.door_pair.append(door312A)

# door to Peasant Room 
        door313A = items.Door("Door of the forgotten", "The creator of this door is unknown'", 100, cave_333, "DOOR", 0,"CLOSED", "LOCKED", "Stone key", cave_338, "south")
        door313B = items.Door("Door of the forgotten", "The creator of this door is unknown'", 100, cave_338, "DOOR", 0,"CLOSED", "LOCKED", "Stone key", cave_333, "north")
        door313A.door_pair.append(door313B)
        door313B.door_pair.append(door313A)



                                                            ############  End of Kingdom of Dorlaan (300 block) - Red team  #################



        
                                                              ######################    Town    #####################
        banker = town.Town("black", cave_509, "Banker", "The Banker is here counting the money in his vault", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, wanderer = False)
        bank_guard = town.Town("black", cave_509, "Bank Guard", "A tough looking Bank Guard is here guarding the Banker", "AWAKE", hp = 150, armor_class = 10, attack_class = "1d20", strength=12, dexterity = 8, wanderer = False)
        apothecary = town.Town("black", cave_503, "Apothecary", "The Apothecary is here mixing potions", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, wanderer = False)
        armorer = town.Town("black", cave_507, "Armorer", "The Armorer is here working his forge", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=14, dexterity = 8, wanderer = False)
        merchant = town.Town("black", cave_510, "Merchant", "The Merchant is here looking to buy any loot you may have found", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=14, dexterity = 8, wanderer = False)
        blacksmith = town.Town("black", cave_504, "Blacksmith", "The Blacksmith is sharpening his weapons", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, wanderer = False)
        stray_dog = town.Town("black", cave_502, "Dog", "A stray dog is here in trying to find food", "AWAKE", hp = 10, armor_class = 2, attack_class = "1d2", strength=2, dexterity = 2, wanderer = False)
        mayor = town.Town("black", cave_517, "Mayor", "The Mayor is at his desk", "AWAKE", hp = 150, armor_class = 4, attack_class = "1d20", strength=6, dexterity = 8, wanderer = False)
        town_guard1 = town.Town("black", cave_508, "Guard", "A town 'guard' is here keeping the town safe", "AWAKE", hp = 150, armor_class = 8, attack_class = "1d12", strength=8, dexterity = 6, wanderer = False)
        town_guard2 = town.Town("black", cave_518, "Guard", "A town 'guard' is here guarding the gates", "AWAKE", hp = 150, armor_class = 8, attack_class = "1d12", strength=8, dexterity = 6, wanderer = False) 
        priest = town.Town("black", cave_501, "Priest", "The Priest of Dranyst is here praying", "AWAKE", hp = 100, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 6, wanderer = False)       
        sheriff = town.Town("black", cave_514, "Sheriff", "The Sheriff is here keeping the town safe", "AWAKE", hp = 150, armor_class = 10, attack_class = "1d20", strength=12, dexterity = 8, wanderer = False)
        gildra = town.Town("black", cave_506, "Gildra", "Gildra is talking to her clients and making drinks", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d12", strength=6, dexterity = 8, wanderer = False)
        tom = town.Town("black", cave_506, "Tom", "Tom, the town drunk, is here ordering another drink ", "AWAKE", hp = 75, armor_class = 4, attack_class = "1d8", strength=6, dexterity =4, wanderer = False)
    
       
        mayor.wallet = 50
        banker.wallet = 75
        sheriff.wallet = 25
        priest.wallet = 25
        gildra.wallet = 25
        town_guard1.inventory.append(copy.deepcopy(sword))
        town_guard2.inventory.append(copy.deepcopy(sword))
        apothecary.inventory.append(copy.deepcopy(green_potion))
        apothecary.inventory.append(copy.deepcopy(red_potion))
        apothecary.inventory.append(copy.deepcopy(blue_potion))
        armorer.inventory.append(copy.deepcopy(steel_shield))

                                                                ######################      End Town    #####################



                                                                ######################      Forest    #####################


        wolf1 = monster.Monster(cave_122, "wolf", "monster", "A large, grey wolf is looking at you hungrily", "AWAKE", hp = 40, armor_class =4, attack_class = "1d8", strength=4, dexterity = 6, load = 0, maxload =10, wanderer = False)                      
        wolf2 = monster.Monster(cave_122, "wolf", "monster", "A large, grey wolf is looking at you hungrily", "AWAKE", hp = 40, armor_class =4, attack_class = "1d8", strength=4, dexterity = 6, load = 0, maxload =10, wanderer = False)
        wolf3 = monster.Monster(cave_122, "wolf", "monster", "A large, grey wolf is looking at you hungrily", "AWAKE", hp = 40, armor_class =4, attack_class = "1d8", strength=4, dexterity = 6, load = 0, maxload =10, wanderer = False)                      
        wolf_mother = monster.Monster(cave_123, "Mother Wolf", "monster", "The 'Mother Wolf' is here guarding her den", "AWAKE", hp = 75, armor_class =6, attack_class = "1d12", strength=6, dexterity = 8, load = 0, maxload =10, wanderer = False)                      
 

        mtn_lion = monster.Monster(cave_116, "Mountain Lion", "monster", "A lean mountain lion jumps off the ledge towards you!", "AWAKE", hp = 60, armor_class = 3, attack_class = "1d8", strength=2, dexterity = 10, load = 0, maxload =10, wanderer = False)                      

        goblin1 = monster.Monster(cave_120, "Goblin", "monster", "A slimy 'goblin' is here cooking dinner", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        goblin2 = monster.Monster(cave_120, "Goblin", "monster", "A slimy 'goblin' is here cooking dinner", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        goblin_scout = monster.Monster(cave_114, "Goblin Scout", "monster", "A 'goblin scout' is trying to sneak away to tell his friends you're here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)

        dark_elf = monster.Monster(cave_130, "Dark Elf", "monster", "A tall and lean 'dark elf' is here on patrol", "AWAKE", hp = 50, armor_class = 6, attack_class = "1d8", strength=6, dexterity = 6, load = 0, maxload =10, wanderer = False)
        black_bear = monster.Monster(cave_106, "Black Bear", "monster", "A 'black bear'  ", "AWAKE", hp = 100, armor_class = 8, attack_class = "1d12", strength=8, dexterity = 4, load = 0, maxload =10, wanderer = False)
        baby_bear = monster.Monster(cave_104, "Baby Bear", "monster", "A 'baby bear' is looking for its mother ", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=8, dexterity = 4, load = 0, maxload =10, wanderer = False)

        high_priestess = monster.Monster(cave_134, "High Priestess", "monster", "The High Priestess of Oquen is here praying", "AWAKE", hp = 100, armor_class = 3, attack_class = "2d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)                      
      
        oquen_priest1= monster.Monster(cave_135, "Priest", "monster", "A 'priest' of the dark god Oquen is here", "AWAKE", hp = 45, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 3, load = 0, maxload =10, wanderer = False)
        oquen_priest2 = monster.Monster(cave_135, "Priest", "monster", "A 'priest' of the dark god Oquen is here", "AWAKE", hp = 45, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 3, load = 0, maxload =10, wanderer = False)

        wild_boar = monster.Monster(cave_101, "Wild Boar", "monster", "A 'wild boar' is rooting around", "AWAKE", hp = 50, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 3, load = 0, maxload =10, wanderer = False)
        orc6 = monster.Monster(cave_133, "Orc", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        orc7 = monster.Monster(cave_133, "Orc", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        troll3 = monster.Monster(cave_128, "Troll", "monster", "A large troll is looking at you", "AWAKE", hp = 35, armor_class = 4, attack_class = "2d6", strength=8, dexterity = 3, load = 0, maxload =10, wanderer = False)


#        knight = monster.Monster(cave_21, "Undead Knight", "monster", "The King's Knight is here on guard", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, load = 0, maxload =10, wanderer = False)
        black_dragon = monster.Monster(cave_800, "Black Dragon", "monster", "You've just woken up a massive 'black dragon!!!'", "AWAKE", hp = 400, armor_class = 10, attack_class = "1d20", strength=30, dexterity = 10, load = 0, maxload =10, wanderer = False)
        witch_doctor = monster.Monster(cave_132, "Witch Doctor", "monster", "The Witch Doctor is here performing black magic", "AWAKE", hp = 125, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 6, load = 0, maxload =10, wanderer = False)
       

        wolf_cloak = items.Armor("wolf cloak", "a beautiful 'wolf cloak' lies here", 2, cave_1000, "ARMOR", 50, "cloak", armor_class = 2)
        dragon_plate = items.Armor("Dragon Plate", "A gleaming set of 'dragon plate' armor", 5, cave_1000, "ARMOR", 300, "cloak", armor_class = 7)

        black_dragon.wallet = 100
        goblin1.wallet = 10
        goblin2.wallet = 10
        goblin_scout.wallet = 10
        orc6.wallet = 10
        orc7.wallet = 10
        troll3.wallet =10
        high_priestess.wallet = 30
        oquen_priest1.wallet = 10
        oquen_priest2.wallet = 10
        witch_doctor.wallet = 20
        dark_elf.wallet = 20
        

        orc6.inventory.append(copy.copy(sword))
        orc7.inventory.append(copy.copy(wooden_shield))
        goblin1.inventory.append(copy.copy(sword))
        goblin2.inventory.append(copy.copy(wooden_shield))
        goblin_scout.inventory.append(copy.copy(blue_potion))
        wolf_mother.inventory.append(wolf_cloak)
        black_dragon.inventory.append(dragon_plate)
        witch_doctor.inventory.append(copy.copy(red_potion))
        dark_elf.inventory.append(copy.copy(steel_shield))
        high_priestess.inventory.append(copy.copy(green_potion))

                                        ######################    End of Forest    #####################
    
   
                                        ######################    Start of Sewers - 600 Block   #####################

        sewer_rat1 = monster.Monster(cave_601, "sewer rat", "monster", "A sewer rat is scurrying around the room", "AWAKE", hp = 15, armor_class = 2, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        sewer_rat2 = monster.Monster(cave_601, "sewer rat", "monster", "A sewer rat is scurrying around the room", "AWAKE", hp = 15, armor_class = 2, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      

        sewer_rat3 = monster.Monster(cave_613, "sewer rat", "monster", "A sewer rat is scurrying around the room", "AWAKE", hp = 15, armor_class = 2, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        sewer_rat4 = monster.Monster(cave_601, "sewer rat", "monster", "A sewer rat is scurrying around the room", "AWAKE", hp = 15, armor_class = 2, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
        mother_rat = monster.Monster(cave_601, "sewer rat", "monster", "A sewer rat is scurrying around the room", "AWAKE", hp = 15, armor_class = 2, attack_class = "1d2", strength=1, dexterity = 3, load = 0, maxload =10, wanderer = False)                      
  
        giant_bat600 = monster.Monster(cave_616, "Giant Bat", "monster", "A huge bat is flying aroung the room", "AWAKE", hp = 30, armor_class = 3, attack_class = "1d8", strength=2, dexterity = 10, load = 0, maxload =10, wanderer = False)                      
        bat601 = monster.Monster(cave_616, "bat", "monster", "A small bat is flying aroung the room", "AWAKE", hp = 12, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 8, load = 0, maxload =10, wanderer = False)                      
        bat602 = monster.Monster(cave_616, "bat", "monster", "A small bat is flying aroung the room", "AWAKE", hp = 12, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 8, load = 0, maxload =10, wanderer = False)                      
        bat6033 = monster.Monster(cave_616, "bat", "monster", "A small bat is flying aroung the room", "AWAKE", hp = 12, armor_class = 1, attack_class = "1d2", strength=1, dexterity = 8, load = 0, maxload =10, wanderer = False)                      

        goblin_scout = monster.Monster(cave_628, "Goblin Scout", "monster", "A 'goblin scout' is trying to sneak away to tell his friends you're here", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        goblin602 = monster.Monster(cave_629, "Goblin", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        goblin603 = monster.Monster(cave_629, "Goblin", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        goblin_captain = monster.Monster(cave_34, "Goblin Captain", "monster", "An ugly looking Orc is here sniffing around", "AWAKE", hp = 100, armor_class = 6, attack_class = "1d8", strength=10, dexterity = 6, load = 0, maxload =10, wanderer = False)
 
        goblin_warlord = monster.Monster(cave_636, "Goblin Warlord", "monster", "You've surprised the 'Goblin Warlord'!", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d12", strength=6, dexterity = 6, load = 0, maxload =10, wanderer = False)


        mud_monster = monster.Monster(cave_605, "Mud Monster", "monster", "A muddy creature begins oozing out of the ground", "AWAKE", hp = 100, armor_class = 8, attack_class = "1d12", strength=8, dexterity = 8, load = 0, maxload =10, wanderer = False)

        lizard = monster.Monster(cave_18, "Scaly Lizard", "monster", "A 'scaly lizard' ", "AWAKE", hp = 75, armor_class = 8, attack_class = "1d12", strength=8, dexterity = 2, load = 0, maxload =10, wanderer = False)                      
      
        troll3= monster.Monster(cave_633, "Troll", "monster", "A large troll is looking at you", "AWAKE", hp = 50, armor_class = 4, attack_class = "2d6", strength=8, dexterity = 3, load = 0, maxload =10, wanderer = False)
 
        anaconda = monster.Monster(cave_631, "Anaconda", "monster", "A giant anaconda is slithering towards you", "AWAKE", hp = 250, armor_class = 6, attack_class = "1d20", strength=8, dexterity = 10, load = 0, maxload =10, wanderer = False)

        mocker = monster.Monster(cave_612, "Mocker", "monster", "The Theive's leader, the 'Mocker' is here planning their next heist", "AWAKE", hp = 150, armor_class = 6, attack_class = "1d20", strength = 4, dexterity = 12, load = 0, maxload =10, wanderer = False)
        thief1 = monster.Monster(cave_618, "Thief", "monster", "You see a thief sneaking back to his hideout", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
        thief2 = monster.Monster(cave_618, "Thief", "monster", "A see a thief sneaking back to his hideout", "AWAKE", hp = 50, armor_class = 4, attack_class = "1d8", strength=6, dexterity = 4, load = 0, maxload =10, wanderer = False)
# 
#        king = monster.Monster(cave_27, "Undead King", "monster", "The Undead King of Valmoor", "AWAKE", hp = 200, armor_class = 6, attack_class = "1d20", strength=10, dexterity = 8, load = 0, maxload =10, wanderer = False)
        water_wierd = monster.Monster(cave_620, "Water Wierd", "monster", "A murky pool of water begins forming into a 'Water Wierd' right before you", "AWAKE", hp = 125, armor_class = 6, attack_class = "1d12", strength=8, dexterity = 6, load = 0, maxload =10, wanderer = False)
       

#Misc
        gold2 = items.Gold("gold", "'gold' coins", 0, cave_634, "GOLD", 0 , 50)                 #goblin treasure room
        skull_key = items.Item("skull key", "A 'skull key'", 1, cave_1000, "MISC", 5)


        sewer_rat1.wallet = 5
        sewer_rat2.wallet = 5
        mud_monster.wallet = 20
        mocker.wallet = 30
        thief1.wallet = 10
        thief2.wallet = 10
        goblin602.wallet=10
        goblin603.wallet=10

        mother_rat.inventory.append(copy.copy(blue_potion))             
        troll3.inventory.append(copy.copy(green_potion))
        mocker.inventory.append(copy.copy(green_potion))                     
        anaconda.inventory.append(copy.copy(red_potion))
        anaconda.inventory.append(copy.copy(chain_mail))
        goblin_warlord.inventory.append(skull_key)
        goblin_warlord.inventory.append(copy.copy(sword))
        goblin_captain.inventory.append(copy.copy(blue_potion))
        water_wierd.inventory.append(copy.copy(steel_helmet))
        giant_bat600.inventory.append(copy.copy(wooden_shield))
        
                                      ######################    End of Sewers - 600 Block   #####################       
 

#Doors

# door to armory
    

        door634A = items.Door("Skull door", "A 'skull door'", 100, cave_634, "DOOR",0, "CLOSED", "LOCKED", skull_key, cave_635, "east")
        door634B = items.Door("Skull door", "A 'skull door'", 100, cave_635, "DOOR",0, "CLOSED", "LOCKED", skull_key, cave_634, "west")
        door634A.door_pair.append(door634B)
        door634B.door_pair.append(door634A)
                                       


    def do_input(self):             #rewrite this to check players and monsters list for input and not search every cave
        get_input_from = [thing for cave in self.caves
                         for thing in cave.players_here
                         if 'get_input' in dir(thing)]
        for thing in get_input_from:
            thing.events = []
            thing.input = thing.get_input()
          

    def do_update(self):
        things_to_update = [thing for cave in self.caves
                            for thing in cave.players_here
                           if 'update' in dir(thing)]
        for thing in things_to_update:
            thing.update()

    def send_results(self):
        things_to_update = [thing for cave in self.caves
                            for thing in cave.players_here
                           if 'send_results' in dir(thing)]
        for thing in things_to_update:
            thing.send_results()        

    def save(self):
        """find all players in game, update their 
        status, and save everyone to the file"""
        for player in self.players:
            self.player_store[player.name] = player.save()
        print "Saving:", self.player_store
        save_file = open('players.pickle', 'wb')
        pickle.dump(self.player_store, save_file)
        
    def load_players(self):
        if not os.access('players.pickle', os.F_OK) == 1:
            return
        load_file = open('players.pickle', 'rb')
        self.player_store = pickle.load(load_file)



    def run_one_tick(self):

             self.do_input()
             self.do_update()
             self.send_results()
 
