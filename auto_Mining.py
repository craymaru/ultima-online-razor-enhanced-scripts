"""
Auto Mining Version4
Author: Cray
"""

from System.Collections.Generic import List

from Scripts import misc_PetFood as pt
from Scripts.config import config


# SETTINGS: Mining
# ===============================
footing = config.Mining[Misc.ShardName()][Player.Serial]["footing"]
container_serial = config.Mining[Misc.ShardName()][Player.Serial]["container_serial"]
mini_ore_organize_bag = config.Mining[Misc.ShardName()][Player.Serial]["mini_ore_organize_bag"]
runic_atlas_serial = config.Mining[Misc.ShardName()][Player.Serial]["runic_atlas_serial"]
bank_rune = config.Mining[Misc.ShardName()][Player.Serial]["bank_rune"]
runes = config.Mining[Misc.ShardName()][Player.Serial]["runes"]
position_offset_x = config.Mining[Misc.ShardName()][Player.Serial]["position_offset_x"]
position_offset_y = config.Mining[Misc.ShardName()][Player.Serial]["position_offset_y"]

pet_serial = config.Mining[Misc.ShardName()][Player.Serial]["pet_serial"]
pet_food_habit = config.Mining[Misc.ShardName()][Player.Serial]["pet_food_habit"]
petfood = pt.PetFood(pet_serial, pet_food_habit)


# ITEM_ID
# ===============================
mini_ore = 0x19b7
ores = {
    0x19b8: "small ore",
    0x19b9: "midium ore",
    0x19ba: "large ore"
}
ore_colors = {
    0x0000: "Iron",
    0x0973: "Dull Copper",
    0x0966: "Shadow",
    0x096d: "Copper",
    0x0972: "Bronze",
    0x08a5: "Golden",
    0x0979: "Agapite",
    0x089f: "Verite",
    0x08ab: "Valorite"
}
bank_items = {
    0x1779: "High Quality Granite",
    0x1BF2: "Ingot",
    0x0F0F: "Star Sapphire",
    0x0F10: "Emerald",
    0x0F11: "Sapphire",
    0x0F13: "Ruby",
    0x0F15: "Citrine",
    0x0F16: "Amethyst",
    0x0F18: "Tourmaline",
    0x0F25: "Amber",
    0x0F26: "Diamond",
    0x3192: "Dark Sapphire",
    0x3193: "Turquoise",
    0x3194: "Perfect Emerald",
    0x3195: "Ecru Citrine",
    0x3197: "Fire Ruby",
    0x3198: "Blue Diamond",
    0x0F28: "A Small Piece of Blackrock",
    0x5732: "crystalline blackrock",
}

item_dic = {
    0x1779: {
        0x0000: {"name": "Iron Granite", "amount": 0},
        0x0973: {"name": "Dull Copper Granite", "amount": 0},
        0x0966: {"name": "Shadow Granite", "amount": 0},
        0x096d: {"name": "Copper Granite", "amount": 0},
        0x0972: {"name": "Bronze Granite", "amount": 0},
        0x08a5: {"name": "Golden Granite", "amount": 0},
        0x0979: {"name": "Agapite Granite", "amount": 0},
        0x089f: {"name": "Verite Granite", "amount": 0},
        0x08ab: {"name": "Valorite Granite", "amount": 0}
    },
    0x1BF2: {
        0x0000: {"name": "Iron Ingot", "amount": 0},
        0x0973: {"name": "Dull Copper Ingot", "amount": 0},
        0x0966: {"name": "Shadow Ingot", "amount": 0},
        0x096d: {"name": "Copper Ingot", "amount": 0},
        0x0972: {"name": "Bronze Ingot", "amount": 0},
        0x08a5: {"name": "Golden Ingot", "amount": 0},
        0x0979: {"name": "Agapite Ingot", "amount": 0},
        0x089f: {"name": "Verite Ingot", "amount": 0},
        0x08ab: {"name": "Valorite Ingot", "amount": 0}
    },
    0x0F0F: {0x0000: {"name": "Star Sapphire", "amount": 0}},
    0x0F10: {0x0000: {"name": "Emerald", "amount": 0}},
    0x0F11: {0x0000: {"name": "Sapphire", "amount": 0}},
    0x0F13: {0x0000: {"name": "Ruby", "amount": 0}},
    0x0F15: {0x0000: {"name": "Citrine", "amount": 0}},
    0x0F16: {0x0000: {"name": "Amethyst", "amount": 0}},
    0x0F18: {0x0000: {"name": "Tourmaline", "amount": 0}},
    0x0F25: {0x0000: {"name": "Amber", "amount": 0}},
    0x0F26: {0x0000: {"name": "Diamond", "amount": 0}},
    0x3192: {0x0000: {"name": "Dark Sapphire", "amount": 0}},
    0x3193: {0x0000: {"name": "Turquoise", "amount": 0}},
    0x3194: {0x0000: {"name": "Perfect Emerald", "amount": 0}},
    0x3195: {0x0000: {"name": "Ecru Citrine", "amount": 0}},
    0x3197: {0x0000: {"name": "Fire Ruby", "amount": 0}},
    0x3198: {0x0000: {"name": "Blue Diamond", "amount": 0}},
    0x0F28: {0x0497: {"name": "A Small Piece of Blackrock", "amount": 0}},
    0x5732: {0x0000: {"name": "Crystalline Blackrock", "amount": 0}}
}





# DEFINES
# ===============================

class ColorfulMassage:
    def __init__(self):
        self.cc = 0
        
    def __call__(self):
        if self.cc < 1910 or 1920 < self.cc:
            self.cc = 1910
        self.cc += 1
        return self.cc
        
colorful = ColorfulMassage()


def OrganizeToBank(container_serial):
    
    if Player.Weight < Player.MaxWeight * 0.45:
       return 
    
    RecallWithAtlas(runic_atlas_serial, bank_rune)
    
    for bank_item in bank_items.keys():
        count = 0
        while Items.FindByID(bank_item, -1, Player.Backpack.Serial) and (count < 10):
            
            item = Items.FindByID(bank_item, -1, Player.Backpack.Serial)
            if item:
                if item.ItemID == 0x1BF2:
                    ingot_color = ore_colors[item.Hue] + " "
                else:
                    ingot_color = ""
                    Misc.SendMessage("Item: %s%s %s" % (ingot_color, bank_items[bank_item], item.Amount), colorful())
                item_dic[item.ItemID][item.Hue]["amount"] += item.Amount
                
                if not container_serial:
                    container_serial = Player.Bank.Serial
                    Player.ChatSay(48, "bank")
                    Misc.Pause(200)
                Items.Move(item, container_serial, 0)
                Misc.Pause(550)
            count += 1
    

    # RESULT
    Misc.SendMessage(">>> RESULT", 1150)
    Misc.SendMessage("==============", 1150)
    for items in item_dic.values():
        for item in items.values():
            if 1 <= item["amount"]:
                Misc.SendMessage("[" + str(item["amount"]) + "] " + item["name"], colorful())
    Misc.SendMessage(" ", 1150)
    Misc.Pause(1000)


def RecallWithAtlas(runic_atlas_serial, rune):
    
    runic_atlas = Items.FindBySerial(runic_atlas_serial)
    
    if runic_atlas:
        Items.UseItem(runic_atlas)
    else:
        Player.HeadMessage(33, "There is no Atlas Rune Book.")
        Misc.ScriptStop("auto_Mining.py")

    # PAGENATE
    page = rune / 16
    for i in range(page):
        Gumps.WaitForGump(498, 5000)
        if Gumps.CurrentGump() ==498:
            Gumps.SendAction(498, 1150)
    
    # SELECT RUNE
    Misc.SendMessage("Rune: {page}-{rune}".format(page=page, rune=rune), colorful())
    rune_button = rune + 100
    
    Gumps.WaitForGump(498, 5000)
    if Gumps.CurrentGump() ==498:
        Gumps.SendAction(498, rune_button)
    
    # RECALL
    Gumps.WaitForGump(498, 5000)
    if Gumps.CurrentGump() ==498:
        Gumps.SendAction(498, 4)
    
    Misc.Pause(2000)


def melting(pet_serial):
    # MINI ORE INTO BAG
    while Items.FindByID(mini_ore, -1, Player.Backpack.Serial):
        item = Items.FindByID(mini_ore, -1, Player.Backpack.Serial)
        if item:
            Items.Move(item, mini_ore_organize_bag, 0)
            Misc.Pause(1000)
    
    def melt(item, pet_serial):
        Items.UseItem(item)
        Misc.Pause(200)
        Target.TargetExecute(pet_serial)
        Misc.Pause(100)

        
    # MELT MINI ORE
    for ore_color in ore_colors.keys():
        item = Items.FindByID(mini_ore, ore_color, mini_ore_organize_bag)
        if item:
            if 1 < item.Amount:
                melt(item, pet_serial)
    # MELT ORE 
    for ore in ores:
        while Items.FindByID(ore, -1, Player.Backpack.Serial):
            item = Items.FindByID(ore, -1, Player.Backpack.Serial)
            if item:
                melt(item, pet_serial)


def getPickaxes():
    pickaxe_filter = Items.Filter()
    pickaxe_filter.Enabled
    pickaxe_filter.Graphics = List[int]([0x0E86])
    pickaxe_filter.Movable = True
    pickaxe_filter.OnGround = False
    pickaxes = Items.ApplyFilter(pickaxe_filter)
    return pickaxes


                
def mining():

    Misc.SendMessage("MINING", colorful())
    Misc.SendMessage("==============", 1150)
    
    pickaxes = getPickaxes()
    
    def getTile(x, y, map):
        for tile in Statics.GetStaticsTileInfo(x, y, map):
            return tile
    
    # MINING
    Journal.Clear()
    Timer.Create("Mining", 10000)
    while Player.Weight < Player.MaxWeight - 100 and Timer.Check("Mining"):
        
        if Journal.Search("There is no metal here to mine."):
            Misc.Pause(1000)
            break
        
        for pickaxe in pickaxes:
            Items.UseItem(pickaxe)
            Misc.Pause(50)
            x = Player.Position.X
            y = Player.Position.Y
            z = Player.Position.Z
            map = Player.Map
            tile = getTile(x, y, map)
            
            if footing and tile:
                Target.TargetExecute(x, y, z, tile.StaticID)
            else:
                Target.TargetExecute(x + position_offset_x, y + position_offset_y, z)
            
        Misc.Pause(1000)
        
    
def callPetFood():
    if not Timer.Check("PetFood"):
        petfood(Misc, Player, Mobiles, Items, Spells, Timer)
        Misc.Pause(1000)
        Timer.Create("PetFood", 5 * 60 * 1000)
        

# RUN
# ===============================

Misc.SendMessage("START", colorful())
Misc.SendMessage("==============", 1150)

while True:
    
    for rune in runes:
        
        callPetFood()
        OrganizeToBank(container_serial)
        RecallWithAtlas(runic_atlas_serial, rune)
        mining()
        melting(pet_serial)
