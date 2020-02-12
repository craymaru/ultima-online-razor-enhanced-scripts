import time

#===================================================================

# SETTINGS
pickaxes = [0x4007CAC9, 0x400AF7DE, 0x4007CAC8, 0x4007CAC7]
mini_ore_organize_bag = 0x4002B142
fire_beetle = 0x0001207D
roonbook = 0x40030BAA
bank_rune = 0
runes = range(1, 16)

#===================================================================

# CREATE PETFOOD
pet_serial = fire_beetle
trush_poach_serial = 0x4002FD51

#===================================================================

# ITEM ID
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
    0x1BF2: "ingot",
    0x3192: "Dark Sapphire",
    0x3193: "Turquoise",
    0x3194: "Perfect Emerald",
    0x3195: "Ecru Citrine",
    0x3197: "Fire Ruby",
    0x3198: "Blue Diamond",
    0x0F28: "a small piece of blackrock",
    0x5732: "crystalline blackrock"
}

#===================================================================

def OrganizeToBank():
    
    RecallToRunebook(bank_rune)
    
    for bank_item in bank_items.keys():
        count = 0
        while Items.FindByID(bank_item, -1, Player.Backpack.Serial) and (count < 10):
            Player.ChatSay(48, "bank")
            Misc.Pause(500)
            item = Items.FindByID(bank_item, -1, Player.Backpack.Serial)
            Misc.SendMessage("Item: %s, %s" % (item.Name, item.Amount))
            Items.Move(item, Player.Bank.Serial, 0)
            Misc.Pause(500)
            count += 1
    Misc.Pause(1000)


def RecallToRunebook(rune):
    Items.UseItem(roonbook)
    Gumps.WaitForGump(89, 3000)
    Misc.SendMessage("Rune: %s" % rune)
    rune_button = rune + 50
    Gumps.SendAction(89, rune_button)
    Misc.Pause(3000)


def Mining():
    
    # TimeSet
    start_time = time.time()
    
    while time.time() - start_time < 15:
        
        # MINING
        mining_count = 0
        while Player.Weight <= Player.MaxWeight and (mining_count < 5):
            for pickaxe in pickaxes:
                Target.Cancel()
                Misc.Pause(50)
                Items.UseItem(pickaxe)
                Target.WaitForTarget(1000, False)
                x = Player.Position.X - 1
                y = Player.Position.Y - 0
                z = Player.Position.Z
                Target.TargetExecute(x, y, z)
                Misc.Pause(200)
            Misc.Pause(1000)
            mining_count += 1
        Misc.Pause(1000)
        
        
        
        # MINI ORE INTO BAG
        while Items.FindByID(mini_ore, -1, Player.Backpack.Serial):
            item = Items.FindByID(mini_ore, -1, Player.Backpack.Serial)
            Items.Move(item, mini_ore_organize_bag, 0)
            Misc.Pause(1000)

        # MELT MINI ORE
        for ore_color in ore_colors.keys():
            item = Items.FindByID(mini_ore, ore_color, mini_ore_organize_bag)
            if item is not None:
                if 1 < item.Amount:
                    Target.Cancel()
                    Misc.Pause(50)
                    Items.UseItem(item)
                    Target.WaitForTarget(1000, False)
                    Target.TargetExecute(fire_beetle)
                    Misc.Pause(500)

        # MELT
        for ore in ores:
            while Items.FindByID(ore, -1, Player.Backpack.Serial):
                item = Items.FindByID(ore, -1, Player.Backpack.Serial)
                Target.Cancel()
                Misc.Pause(50)
                Items.UseItem(item)
                Target.WaitForTarget(1000, False)
                Target.TargetExecute(fire_beetle)
                Misc.Pause(500)

# ===================================================================
# PETFOOD
# ===================================================================

# Foods
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

        
def PetFood(pet_serial, trush_poach_serial):
    
    global ate_meat
    global ate_fruit

    ate_meat = False
    ate_fruit = False

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

#===================================================================

while True:
    PetFood(pet_serial, trush_poach_serial)
    for i in range(5):
        for rune in runes:
            OrganizeToBank()
            RecallToRunebook(rune)
            Mining()
