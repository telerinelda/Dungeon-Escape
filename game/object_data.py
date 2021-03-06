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

    rat = Thing("RAT")
    rat.location = "NOWHERE"
    rat.can_pick_up = False
    rat.look_texts = {"default":"The rat is large and looks well-fed. You shudder to think what his diet consists of, down here. He looks at you with keen interest. He seems disappointed that you are awake. He will not approach the bowl of gruel while he senses you are conscious."}
    rat.room_look_texts = {"default":"There is a rat."}
    rat.pick_up_texts = {"default":"The rat stays well out of your reach."}
    rat.use_texts = {"default":"You can't think of a use for this rat, and you doubt he'd agree to be picked up."}
    #rat.drop_texts
    rat.go_to_texts = {"default":"The ropes prevent your getting any closer to the rat."}
    gs.object_dictionary[rat.name] = rat
    gs.multiword.append([["RODENT"], "RAT"])

    cot = Thing("COT")
    cot.location = "CELL"
    cot.can_pick_up = False
    cot.look_texts = {"default":"You are lying on a disgusting old bed.  Black spots of mold dot the ancient fabric.  Who knows how long it has been in this dungeon."}
    cot.room_look_texts = {"default":"There is a bed."}
    cot.pick_up_texts = {"default":"The cot is too large to bring with you."}
    cot.use_texts = {"default":"You are already using the cot."}
    #cot.drop_texts
    cot.go_to_texts = {"default":"You already lie upon the cot."}
    gs.object_dictionary[cot.name] = cot
    gs.multiword.append([["BED"], "COT"])
    cot.add_sublocation(preposition="UNDER",text="Under the cot",hidden=True)
    cot.add_sublocation(preposition="ON",text="On the cot",hidden=False)

    bone = Thing("BONE")
    bone.location = "CELL"
    bone.can_pick_up = True
    bone.sublocation = ["COT","UNDER"]
    bone.look_texts = {"default":"You look at the creepy grey-white bone sliver.  It is thin and broken to a point at one end. Could it be... a human finger?  You shudder."}
    bone.room_look_texts = {"default":"There is a piece of bone."}
    bone.pick_up_texts = {"default":"You pick up the bone."}
    bone.is_transitive = True
    bone.use_texts = {"default":"You try but the bone doesn't accomplish what you wanted."}
    bone.drop_texts = {"default":"You put the creepy bone down.  You feel better already.  That thing is weird."}
    bone.go_to_texts = {"default":"You move closer to the bone sliver.  You wonder what beast ... or person ... it once belonged to."}
    gs.object_dictionary[bone.name] = bone
    gs.multiword.append([["BONE","SLIVER"], "BONE"])
    gs.multiword.append([["PIECE","OF","BONE"], "BONE"])

    cellfloor = Thing("CELL FLOOR")
    cellfloor.location = "CELL"
    cellfloor.can_pick_up = False
    cellfloor.look_texts = {"default":"The floors are jumbled stone and ancient mortar.  The cracks are caked with unimaginable filth."}
    cellfloor.room_look_texts = {"default":""}
    cellfloor.pick_up_texts = {"default":"Your fingers search the floor carefully but it is unyielding."}
    cellfloor.use_texts = {"default":"You can't think of anything to do with the floor of your cell."}
    cellfloor.drop_texts = dict()
    cellfloor.go_to_texts = {"default":"You lean in close to the floor.  It smells of sweat and despair."}
    gs.object_dictionary[cellfloor.name] = cellfloor

    cellwall = Thing("CELL WALL")
    cellwall.location = "CELL"
    cellwall.can_pick_up = False
    cellwall.look_texts = {"default":"The walls of the ancient cell are ugly and hard. In one place a former prisoner has made 22 tally marks.  You wonder how long ago they were made, and what that prisoner's fate turned out to be."}
    cellwall.room_look_texts = {"default":""}
    cellwall.pick_up_texts = {"default":"You can't pick up the walls."}
    cellwall.use_texts = {"default":"You press on the walls here and there, but no secrets are revealed."}
    cellwall.drop_texts = dict()
    cellwall.go_to_texts = {"default":"You draw close to the cell wall, with no result."}
    gs.object_dictionary[cellwall.name] = cellwall

    cellceiling = Thing("CELL CEILING")
    cellceiling.location = "CELL"
    cellceiling.can_pick_up = False
    cellceiling.look_texts = {"default":"The ceiling is low and made of brick, stones, ancient lumber, and mortar."}
    cellceiling.room_look_texts = {"default":""}
    cellceiling.pick_up_texts = {"default":"You can't pick up the ceiling."}
    cellceiling.use_texts = {"default":"The ceiling is of no use to you in your present state."}
    cellceiling.drop_texts = dict()
    cellceiling.go_to_texts = {"default":"You can't get any closer to the ceiling."}
    gs.object_dictionary[cellceiling.name] = cellceiling

    celldoor = Pathway("CELL DOOR")
    celldoor.location = "CELL"
    celldoor.location2 = "HALLWAY"
    celldoor.look_texts = {"CELL":"A very strong-looking iron door is the only way out of the cell.",
                           "HALLWAY":"The iron door that once kept you locked within is just as imposing from the outside."}
    celldoor.room_look_texts = {"default":"There is a door."}
    celldoor.pick_up_texts = {"default":"The ropes that bind you prevent you from approaching the door"}
    celldoor.go_to_texts = {"default":"The ropes that bind you prevent you from approaching the door."}
    celldoor.look_thru_texts = {"CELL":"Whether from the smallness of the cracks, or the darkness on the other side, you can see nothing through the door."}
    gs.object_dictionary[celldoor.name] = celldoor
    gs.pathways_dictionary[celldoor.name] = celldoor
    gs.multiword.append([["CELL","DOOR"], "CELL DOOR"])

    #hallway location,then:
    #rat progress point & all text updates.




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