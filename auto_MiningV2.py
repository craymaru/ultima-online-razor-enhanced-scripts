"""
Auto Mining Version2
Author: Cray
"""

# Settings

# Pickaxe
pickaxe_serials = [0x4007CAC9, 0x400AF7DE, 0x4007CAC8, 0x4007CAC7]

# Roonbook
roonbook_serial = 0x40030BAA
# Number of bankrunes placed in the runbook 
bank_rune = 0
# Number of runes placed in the runbook
runes = range(1, 16)

# Items
bank_items = {
    0x1779: "High Quality Granite",
    0x19b7: "Mini Ore",
    0x19b8: "Small Ore",
    0x19b9: "Midium Ore",
    0x19ba: "Large Ore",
    0x1BF2: "Ingot",
    0x3192: "Dark Sapphire",
    0x3193: "Turquoise",
    0x3194: "Perfect Emerald",
    0x3195: "Ecru Citrine",
    0x3197: "Fire Ruby",
    0x3198: "Blue Diamond",
    0x0F28: "A Small Piece of Blackrock",
    0x5732: "Crystalline Blackrock",
}


def recall_to_runebook(rune):
    
    Items.UseItem(roonbook_serial)
    Gumps.WaitForGump(89, 15000)
    Misc.Pause(100)
    Misc.SendMessage("RUNE: %s" % rune, 54)
    rune_button = rune + 50
    Gumps.SendAction(89, rune_button)
    Misc.Pause(3000)
    
    
def store_to_bank():
    
    recall_to_runebook(bank_rune)
    
    Misc.SendMessage("STORE", 65)
    
    for bank_item in bank_items.keys():
        loop_limit = 10
        count = 0
        while Items.FindByID(bank_item, -1, Player.Backpack.Serial) and (count < loop_limit):
            Player.ChatSay(48, "bank")
            Misc.Pause(200)
            item = Items.FindByID(bank_item, -1, Player.Backpack.Serial)
            if item:
                Items.Move(item, Player.Bank.Serial, 0)
                Misc.Pause(500)
            count += 1
            
    Misc.Pause(1000)
    

def mining():
    
    Misc.SendMessage("MINING", 75)
    
    # TimeSet
#    Timer.Create("mining", 10000)
#    
#    while Timer.Check("mining"):
        
    # MINING
    mining_count = 0
    while Player.Weight <= Player.MaxWeight - 100 and (mining_count < 10):
        for pickaxe_serial in pickaxe_serials:
            Items.UseItem(pickaxe_serial)
            Misc.Pause(100)
            # Target.WaitForTarget(1000, False)
            x = Player.Position.X - 1
            y = Player.Position.Y - 0
            z = Player.Position.Z
            Target.TargetExecute(x, y, z)
        Misc.Pause(1000)
        mining_count += 1
    
    Target.Cancel()
    Misc.Pause(1000)
    
    
    
while True:
    for rune in runes:
        store_to_bank()
        recall_to_runebook(rune)
        mining()