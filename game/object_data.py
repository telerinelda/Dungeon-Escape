from game import Thing, Place, Pathway

def add_object_data(gs):
    # ---------------------------------------------------------------------------------------------
    #  Game Objects and Locations
    # ---------------------------------------------------------------------------------------------
    #  Starting Cell
    cell = Place("CELL")
    cell.look_texts = {"default":"You look around at your cell.  The stone is damp.  The air is foul.  The ropes that hold you are attached to the wall behind you.  You lie on an old, moldy cot."}
    cell.go_to_texts = {"default":"You reenter the cell you escaped from.  It disgusts you."}
    gs.object_dictionary[cell.name] = cell
    gs.multiword.append([["JAIL"],"CELL"])

    rope = Thing("ROPE")
    rope.location = "CELL"
    rope.can_pick_up = False
    rope.look_texts = {"default": "The rope is thick and strong.  Your wrists ache from the tight knots."}
    rope.room_look_texts = {"default": ""}
    rope.pick_up_texts = {"default": "At the moment the ropes have you."}
    rope.use_texts = {"default": "You strain against the ropes but you can't seem to achieve anything."}
    rope.drop_texts = {"default": ""}
    rope.go_to_texts = {"default": "You can't get any closer to the rope than you are now."}
    gs.object_dictionary[rope.name] = rope
    gs.multiword.append([["ROPES"],"ROPE"])
    gs.multiword.append([["BONDS"],"ROPE"])
    gs.multiword.append([["CORD"],"ROPE"])
    gs.multiword.append([["CORDS"],"ROPE"])

    bowl = Thing("BOWL")
    bowl.location = "CELL"
    bowl.can_pick_up = True
    bowl.look_texts = {"default":"An ugly wooden bowl holds a nasty looking gruel.  But you are hungry.  You feel you must eat it to keep up your strength."}
    bowl.room_look_texts = {"default":"There is a bowl of gruel."}
    bowl.pick_up_texts = {"default":"You pick up the bowl of gruel carefully, so as not to waste the precious food.  It's smell drives you mad with hunger."}
    bowl.use_texts = {"default":"You slurp down the gruel hungrily.  It is soon gone.  But as you sigh contentedly you feel some of your strength returning. You are not so hungry anymore."}
    bowl.drop_texts = {"default":"Summoning all your willpower, you place the bowl of gruel carefully on the floor. Perhaps you will eat it later. But not yet.  Surely you aren't so far gone as that yet."}
    bowl.go_to_texts = {"default":"You can't move very far, but you scoot closer to the food."}
    gs.object_dictionary[bowl.name] = bowl
    gs.multiword.append([["GRUEL"], "BOWL"])
    gs.multiword.append([["BOWL","OF","GRUEL"], "BOWL"])
    gs.multiword.append([["BOWL","OF","FOOD"], "BOWL"])


    #rat
    #cot
    #bone
    #floor
    #ceiling
    #walls

#sample doorway:
    door = Pathway("DOOR")
    door.location = "ROOM 2"
    door.location2 = "ROOM 1"
    door.look_texts = {"ROOM 1":"You inspect the door.  It is a heavy wooden door with no keyhole. The door leads to room 2.",
                      "ROOM 2":"You inspect the door.  It is a heavy wooden door with no keyhole. The door leads to room 1."}
    door.room_look_texts = {"default":"There is a door."}
    door.pick_up_texts = {"default":"Sigh.... No you can't pick up a door."}
    door.go_to_texts = {"default":"You approach the door..."}
    door.look_thru_texts = {"ROOM 1":"Beyond the door is room 2.  You can make out a wooden table.",
                           "ROOM 2":"Beyond the door is room 1.  You don't see any people or large objects."}
    #door.use_texts = {} #not needed for pathways.
    gs.object_dictionary[door.name] = door
    gs.pathways_dictionary[door.name] = door


    #  Sample Object: a rock you can pick up:
    rock = Thing("ROCK")
    rock.location = "ROOM 1"
    rock.can_pick_up = True
    rock.look_texts = {"default": "You look at the rock.  It is grey and hard, about the size of a baseball."}
    rock.room_look_texts = {"default": "There is a rock."}
    rock.pick_up_texts = {"default": "You pick up the rock."}
    rock.use_texts = {"default": "You can't think of anything to use the rock for at the moment."}
    rock.drop_texts = {"default": "You drop the rock.  It makes a sound like PLERK as it hits the ground."}
    rock.go_to_texts = {"default": "You approach the rock.  It does not respond."}
    gs.object_dictionary[rock.name] = rock


    #  Sample Object: a table that remains stationary
    table = Thing("TABLE")
    table.location = "ROOM 2"
    table.can_pick_up = False #this isn't needed because by default you can't pick up objects
    table.look_texts = {"default": "You are looking at a medium size table made of dark brown wood.  It is old and heavy."}
    table.room_look_texts = {"default": "There is a table."}
    table.pick_up_texts = {"default": "The table is too heavy to pick up."}
    table.use_texts = {"default": "You lean against the table and ponder your life choices."}
    #table.drop_texts = {} #not needed since you can't pick it up in the first place.
    table.go_to_texts = {"default": "You approach the table.  It does not react."}
    gs.object_dictionary[table.name] = table

    #  Sublocation example:  We make "on the table" a place you can put things.
    table.add_sublocation(preposition="ON",text="On the table",hidden=True)

    #  Sample Transitive Object: a hammer is a transitive object.  to use it you must use it ON something.
    hammer = Thing("HAMMER")
    hammer.is_transitive = True
    hammer.location = "ROOM 2"
    hammer.sublocation = ["TABLE","ON"]
    hammer.can_pick_up = True
    hammer.look_texts = {"default": "You look at the hammer.  It is made of metal with a wooden handle."}
    hammer.room_look_texts = {"default": "There is a hammer."}
    hammer.pick_up_texts = {"default": "You pick up the hammer."}
    hammer.use_texts = {"default": "Thunk!",
                       "ROCK": "You carefully aim the hammer and strike the rock.  KABLOOEY!  You smash the rock into a fine dust."}
    hammer.drop_texts = {"default": "You place the hammer down."}
    hammer.go_to_texts = {"default": "You approach the hammer.  It does not respond."}
    gs.object_dictionary[hammer.name] = hammer

    #add special verbs that can only be used if you have a certain object.  The dictionary returns the object name.
    # The user must provide the target.
    gs.special_verbs["HAMMER"] = "HAMMER" #Now "Hammer door" is translated as "Use hammer on door"
    gs.special_verbs["SMASH"] = "HAMMER"
    gs.special_verbs["HIT"] = "HAMMER"

    #other examples
    gs.special_verbs["LIGHT"] = "MATCHES"
    gs.special_verbs["ATTACK"] = "SWORD"

    return gs