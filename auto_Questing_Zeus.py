# QUESTING

# REQUIRED:
# * DO NOT HAVE BACKPACKS
# * PACK PET
# * TRUSH POUCH
# * MAKE TOOL ONCE




# IMPORTS
# ========================
import sys
import re


# SETTINGS
# ========================
quest_mobile_serial = 0x00000717 # QUEST NPC
pack_pet_serial = 0x000117BD # PACK PET SERIAL

pet_serials ={
    0x0000A8D5: {"name": "Nigoki", "food": "meat"},
    0x0000A8D5: {"name": "Nirama", "food": "fruit"}
}

# TARGET ITEM_ID
target_item_ids = {
    0x2831: "Recipe Scroll",
    0x2F58: "Talisman",
    0x2F59: "Talisman",
    0x2F5A: "Talisman",
    0x2F5B: "Talisman"
}
# TARGET PROPERTIES
target_properties_regex = {
    "Recipe Scroll",
    "Slayer",
    "^(?=.*Bonus)(?=.*(2[5-9]|[3-9][0-9])).*$", # Bonus and 25-99
}

# ITEM_ID
# ========================
tool_kit_id = 0x1EB8
ingot_id = 0x1BF2
quest_item_color_id = 0x04ea


#for i in range(100):
#    Misc.SendMessage("MESSAGE:" + str(i), i)
#    Misc.Pause(100)



# INITS
# ========================
quested = False


# DEFINES
# ========================

def Warning():
    Misc.SendMessage("WARNING:", 33)
    for i in range(10):
        Misc.SendMessage("Sub-backpacks and all items inside are DESTROYED!!!", 33)
    Misc.SendMessage("IF YOU CONFIRMED, SELECT YOUR TRUSH POUCH.", 53)
    Misc.SendMessage("( ESC to be CANCEL ) ", 53)
    global trush_pouch
    trush_pouch = Target.PromptTarget()
    if trush_pouch == -1:
        Misc.SendMessage("Cancelled!", 5)
        sys.exit()

def MoveItemToBackpack(item):
    Items.Move(item, Player.Backpack.Serial, 0)
    Misc.Pause(1000)
    
def MoveItemToTrush(item):
    Items.Move(item, trush_pouch, 0)
    Misc.Pause(1000)

def GetItemFromPet(item, low_amount, get_amount):
    if Items.BackpackCount(item, -1) < low_amount:
        pet = Mobiles.FindBySerial(pack_pet_serial)
        get_item = Items.FindByID(item, -1, pet.Backpack.Serial)
        Items.Move(get_item, Player.Backpack.Serial, get_amount)
        Misc.Pause(1000)
    
def DevideSubBackpackItems():
    
    Misc.SendMessage("DEVIDE ITEMS", 1150)
    Misc.SendMessage("==============", 1150)
    
    backpack_id = 0x0E75
    while Items.FindByID(backpack_id, -1, Player.Backpack.Serial):
        sub_backpack = Items.FindByID(backpack_id, -1, Player.Backpack.Serial)
        if sub_backpack: 
            
            for item_id in target_item_ids:
                
                while Items.FindByID(item_id, -1, sub_backpack.Serial):
                    target_item = Items.FindByID(item_id, -1, sub_backpack.Serial)
                    
                    if target_item:
                        item_props = Items.GetPropStringList(target_item)
                        is_target = False
                        
                        # PROPERTIES CHECK
                        for item_prop in item_props:
                            Misc.SendMessage(item_prop)
                            # EVAL TARGET PROPERTIES
                            for target_prop in target_properties_regex:
                                # REGEX
                                if re.search(target_prop, item_prop, flags=re.IGNORECASE):
                                    Misc.Beep()
                                    Misc.SendMessage("MATCH!", 50)
                                    Misc.SendMessage("REGEX:", 60)
                                    Misc.SendMessage(" => " + target_prop, 60)
                                    Misc.SendMessage("PROPS:", 80)
                                    Misc.SendMessage(" => " + item_prop, 80)
                                    is_target = True
                                    
                        # TARGET TO KEEP OR TRUSH
                        if is_target:
                            Misc.SendMessage(" => KEEP", 90)
                            MoveItemToBackpack(target_item)
                            is_target = False
                        else:
                            Misc.SendMessage(" => TRUSH")
                            MoveItemToTrush(target_item)
                        
                        Misc.Pause(1000)
                        
                    Misc.Pause(100)
                    
        MoveItemToTrush(sub_backpack)
        Misc.Pause(1000)

def SubBackpackCleanup():
    bag = 0x0E75
    colors = {
        0x0003: "Blue",
        0x000d: "Purple",
        0x0021: "Red",
        0x001c: "Dark Pink",
        0x0037: "Frog Green",
        0x003a: "Uguisu Green",
        0x0044: "Green",
        0x0059: "Light Blue",
        0x0062: "Dark Blue",
        0x0071: "Dark Purple"
    }
    for color in colors:
        while Items.FindByID(bag, color, Player.Backpack.Serial):
            item = Items.FindByID(bag, color, Player.Backpack.Serial)
            MoveItemToTrush(item)
            
def Questing():
    
    global quested
    
    if quested:
        return

    if 10 <= Items.BackpackCount(tool_kit_id, quest_item_color_id):
        return
    
    Misc.SendMessage("QUESTING", 1150)
    Misc.SendMessage("==============", 1150)
    
    while not quested:
        
        # TALK
        Mobiles.UseMobile(quest_mobile_serial)
        Misc.Pause(100)
        
        # ALREDY GET QUEST?
        if Gumps.LastGumpTextExist("I will be in your debt if you bring me"):
            Misc.SendMessage("Already have a quest.")
            # CLOSE
            Gumps.WaitForGump(1280077232, 10000)
            Gumps.SendAction(1280077232, 0)
            quested = True
            Misc.Pause(500)
            return
        
        # CHECK QUEST
        quest_check = Gumps.LastGumpTextExist("Necessity's Mother")
        Misc.SendMessage("QUEST: %s" % quest_check)
        
        if quest_check:
            # ACCEPT
            Gumps.WaitForGump(1280077232, 10000)
            Gumps.SendAction(1280077232, 4)
            quested = True
        else:
            # REFUSE
            Gumps.WaitForGump(1280077232, 10000)
            Gumps.SendAction(1280077232, 2)
            # CLOSE
            Gumps.WaitForGump(1280077232, 10000)
            Gumps.SendAction(1280077232, 0)
            quested = False
            
        Misc.Pause(500)


def HowManyMake():
    # CREATE TOOLS FOR QUEST
    if Items.BackpackCount(tool_kit_id, 0) <= 1:
        return 11
    else:
        return 10

def Craft():

    global quested
    
    if not quested:
        return
    
    if 10 <= Items.BackpackCount(tool_kit_id, quest_item_color_id):
        return
    
    Misc.SendMessage("CRAFTING", 1150)
    Misc.SendMessage("==============", 1150)
        
    # CREATE TOOLS FOR QUEST
    count = 0
    while Items.BackpackCount(tool_kit_id, quest_item_color_id) < HowManyMake() and (count < 15):

        # USE
        item = Items.FindByID(tool_kit_id, 0, Player.Backpack.Serial)
        Items.UseItem(item)
        Misc.Pause(500)
        
        # REMAKE
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 21)
        Misc.Pause(1500)
        
        count += 1
    
    # CLOSE
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 0)
    Misc.Pause(500)

def ReportQuest():
    
    global quested
    
    Misc.SendMessage("REPORT QUEST", 1150)
    Misc.SendMessage("==============", 1150)
    
    if 10 <= Items.BackpackCount(tool_kit_id, quest_item_color_id):
        # TALK
        Mobiles.UseMobile(quest_mobile_serial)
        Misc.Pause(250)
        # CONTINUE
        Gumps.WaitForGump(1280077232, 10000)
        Gumps.SendAction(1280077232, 8)
        # ACCEPT
        Gumps.WaitForGump(1280077232, 10000)
        Gumps.SendAction(1280077232, 5)
        quested = False
        Misc.Pause(250)

        
        
        
# ITEM_ID: Foods
# ===============================
foods = {
    0x097B: {"name": "fish", "type": "etc"},
    0x097D: {"name": "cheese", "type": "etc"},
    0x09B7: {"name": "chicken", "type": "meat"},
    0x09C0: {"name": "sausage", "type": "meat"},
    0x09C9: {"name": "ham", "type": "meat"},
    0x09D1: {"name": "grape", "type": "fruit"},
    0x09D2: {"name": "peach", "type": "fruit"},
    0x09D0: {"name": "apple", "type": "fruit"},
    0x09EB: {"name": "muffins", "type": "etc"},
    0x09F2: {"name": "ribs", "type": "meat"}
}

# DEFINES: PetFood
# ===============================
def PetFood(pet_serial, trush_poach_serial):
    
    global ate_meat
    global ate_fruit

    ate_meat = False
    ate_fruit = False

    Misc.SendMessage("PETFOOD", 1150)
    Misc.SendMessage("==============", 1150)
    
    while ate_fruit == False:
        Spells.CastMagery("Create Food")
        Misc.Pause(1000)

        for food_k, food_v in foods.items():
            item = Items.FindByID(food_k, -1, Player.Backpack.Serial)
            if item is not None:
                if food_v["type"] == "fruit":
                    Target.Cancel()
                    Misc.Pause(50)
                    Items.Move(item, pet_serial, 0)
                    ate_fruit = True
                    Misc.Pause(500)
                
        for food in foods.keys():
            item = Items.FindByID(food, -1, Player.Backpack.Serial)
            if item is not None:
                Target.Cancel()
                Misc.Pause(50)
                Items.Move(item, trush_poach_serial, 0)
                Misc.Pause(500)
    Misc.Pause(1000)
        
        
        
# RUN
# ========================

Warning()

while True:
    
    PetFood(pack_pet_serial, trush_pouch)
    
    for i in range(10):
        
        DevideSubBackpackItems()
        SubBackpackCleanup()
        Questing()
        GetItemFromPet(ingot_id, 100, 400)
        Craft()
        ReportQuest()
        
        Misc.Pause(50)
