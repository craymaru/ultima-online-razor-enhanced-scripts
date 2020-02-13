# Auto Mining by Cray
# ===============================

# IMPORTS
# ===============================
import time

# SETTINGS: Mining
# ===============================
pickaxes = [0x4007CAC9, 0x400AF7DE, 0x4007CAC8, 0x4007CAC7]
mini_ore_organize_bag = 0x4002B142
fire_beetle = 0x0001207D
roonbook = 0x40030BAA
bank_rune = 0
runes = range(1, 16)

# SETTINGS: PetFood
# ===============================
pet_serial = fire_beetle
trush_poach_serial = 0x4002FD51

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
    0x1BF2: "Ingot",
    0x3192: "Dark Sapphire",
    0x3193: "Turquoise",
    0x3194: "Perfect Emerald",
    0x3195: "Ecru Citrine",
    0x3197: "Fire Ruby",
    0x3198: "Blue Diamond",
    0x0F28: "A Small Piece of Blackrock",
    0x5732: "crystalline blackrock"
}

item_dic = {
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
        
def OrganizeToBank():
    
    RecallToRunebook(bank_rune)
    
    for bank_item in bank_items.keys():
        count = 0
        while Items.FindByID(bank_item, -1, Player.Backpack.Serial) and (count < 10):
            Player.ChatSay(48, "bank")
            Misc.Pause(500)
            item = Items.FindByID(bank_item, -1, Player.Backpack.Serial)
            if item:
                if item.ItemID == 0x1BF2:
                    ingot_color = ore_colors[item.Hue] + " "
                else:
                    ingot_color = ""
                    Misc.SendMessage("Item: %s%s %s" % (ingot_color, bank_items[bank_item], item.Amount), colorful())
                item_dic[item.ItemID][item.Hue]["amount"] += item.Amount
                Items.Move(item, Player.Bank.Serial, 0)
                Misc.Pause(500)
            count += 1
    
    # SORT
    # item_dic_sorted = sorted
    # scores_sorted = sorted(item_dic[0x1BF2], key=lambda x:x['amount'])

    # RESULT
    Misc.SendMessage(">>> RESULT", 1150)
    Misc.SendMessage("==============", 1150)
    for items in item_dic.values():
        for item in items.values():
            if 1 <= item["amount"]:
                Misc.SendMessage("[" + str(item["amount"]) + "] " + item["name"], colorful())
    Misc.SendMessage(" ", 1150)
    Misc.Pause(1000)


def RecallToRunebook(rune):

    Target.Cancel()
    Misc.Pause(100)
    Items.UseItem(roonbook)
    Gumps.WaitForGump(89, 3000)
    Misc.SendMessage("RUNE: %s" % rune, colorful())
    Misc.SendMessage("==============", 1150)
    rune_button = rune + 50
    Gumps.SendAction(89, rune_button)
    Misc.Pause(3000)


def Mining():

    Misc.SendMessage("MINING", colorful())
    Misc.SendMessage("==============", 1150)
    
    # TimeSet
    start_time = time.time()
    
    while time.time() - start_time < 15:
        
        # MINING
        mining_count = 0
        while Player.Weight <= Player.MaxWeight and (mining_count < 5):
            for pickaxe in pickaxes:
                Target.Cancel()
                Misc.Pause(100)
                Items.UseItem(pickaxe)
                Target.WaitForTarget(10000, False)
                x = Player.Position.X - 1
                y = Player.Position.Y - 0
                z = Player.Position.Z
                Target.TargetExecute(x, y, z)
                Misc.Pause(200)
            Misc.Pause(1000)
            mining_count += 1
        Misc.Pause(1750)
        
        # MINI ORE INTO BAG
        while Items.FindByID(mini_ore, -1, Player.Backpack.Serial):
            item = Items.FindByID(mini_ore, -1, Player.Backpack.Serial)
            if item:
                Items.Move(item, mini_ore_organize_bag, 0)
                Misc.Pause(1000)

        # MELT MINI ORE
        for ore_color in ore_colors.keys():
            item = Items.FindByID(mini_ore, ore_color, mini_ore_organize_bag)
            if item:
                if 1 < item.Amount:
                    Target.Cancel()
                    Misc.Pause(100)
                    Items.UseItem(item)
                    Target.WaitForTarget(10000, False)
                    Target.TargetExecute(fire_beetle)
                    Misc.Pause(750)

        # MELT
        for ore in ores:
            while Items.FindByID(ore, -1, Player.Backpack.Serial):
                item = Items.FindByID(ore, -1, Player.Backpack.Serial)
                if item:
                    Target.Cancel()
                    Misc.Pause(100)
                    Items.UseItem(item)
                    Target.WaitForTarget(10000, False)
                    Target.TargetExecute(fire_beetle)
                    Misc.Pause(750)

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

    Misc.SendMessage("PETFOOD", colorful())
    Misc.SendMessage("==============", 1150)
    
    while ate_meat == False or ate_fruit == False:
        Spells.CastMagery("Create Food")
        Misc.Pause(1000)

        for food_k, food_v in foods.items():
            item = Items.FindByID(food_k, -1, Player.Backpack.Serial)
            if item is not None:
                if food_v["type"] == "meat":
                    Target.Cancel()
                    Misc.Pause(50)
                    Items.Move(item, pet_serial, 0)
                    ate_meat = True
                    Misc.Pause(500)
                elif food_v["type"] == "fruit":
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
# ===============================

Misc.SendMessage("START", colorful())
Misc.SendMessage("==============", 1150)

while True:
    PetFood(pet_serial, trush_poach_serial)
    for i in range(5):
        for rune in runes:
            OrganizeToBank()
            RecallToRunebook(rune)
            Mining()
