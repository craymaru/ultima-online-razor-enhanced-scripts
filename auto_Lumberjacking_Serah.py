# Auto Lumberjacking by Cray
# ===============================


# SETTINGS: Lumberjacking
# ===============================
axe = 0x40081CB8 # Your equippable Axe Static ID
position_offset_x = -1 # Tree pos from the your character pos
position_offset_y = 0
times = 6

# SETTINGS: Runes
# ===============================
runebook = 0x4002E477 # your Roonbook
runic_atlas = 0x405FADE0 # your Runic-Atlas
bank_rune = 0 # Bank rune should be first of the Runic-Atlas
runes = range(1, 33) # How many runes are in the Runic-Atlas

# ITEM_ID
# ===============================
log = 0x1BDD
board = 0x1BD7
bank_items = {
    0x1BDD: "Log",
    0x1BD7: "Board",
    0x2F5F: "Switch",
    0x318F: "Bark Fragment",
    0x3190: "Parasitic Plant",
    0x3191: "Luminescent Fungi",
    0x3199: "Brilliant Amber"
}
log_colors = {
    0x0000: "Log",
    0x07da: "Ork",
    0x04a7: "Ash",
    0x04a8: "Yew",
    0x04a9: "Heartwood",
    0x04aa: "Bloodwood",
    0x047f: "Frostwood"
}
# ===============================

def Lumberjacking():
    #LUMBERJACKING
    Journal.Clear()
    count = 0
    while Player.Weight <= Player.MaxWeight and (count < times):
        
        if Journal.Search('not enough'):
            break
        
        # EQUIP AXE
        if not Player.CheckLayer("LeftHand"):
            Player.EquipItem(axe)
            Misc.Pause(1000)
        
        # TREE POSITION
        x = Player.Position.X + position_offset_x
        y = Player.Position.Y + position_offset_y
        map_id = Player.Map
        
        # TILE CHECK
        tiles = Statics.GetStaticsTileInfo(x, y, map_id)
        for i, tile in enumerate(tiles):
            if i == 1:
                global tile_static_id
                tile_static_id = tile.StaticID
                Misc.SendMessage("TileID: %s" % tile_static_id)
                
                # JACKING
                Target.Cancel()
                Misc.Pause(50)
                Items.UseItem(axe)
                Target.WaitForTarget(1000, False)
                Target.TargetExecute(x, y, tile.StaticZ, tile_static_id)
                Misc.Pause(1000)
        count += 1

            
            
# LOG TO BOARD
def LogToBoard():
    
    for log_color in log_colors.keys():
        item = Items.FindByID(log, log_color, Player.Backpack.Serial)
        if item:
            Target.Cancel()
            Misc.Pause(50)
            Misc.SendMessage(log)
            Items.UseItem(axe)
            Target.WaitForTarget(1000, False)
            Target.TargetExecute(item)
            Misc.Pause(500)
    
def Bank():
    # BANK
    RecallToAtlas(bank_rune)
    
    for bank_item in bank_items.keys():
        count = 0
        while Items.FindByID(bank_item, -1, Player.Backpack.Serial) and (count < 10):
            item = Items.FindByID(bank_item, -1, Player.Backpack.Serial)
            if item:
                Player.ChatSay(12, "bank")
                Misc.Pause(500)
                Items.Move(item, Player.Bank, 0)
                Misc.Pause(500)
            count += 1


def RecallToRunebook(rune):
    Items.UseItem(runebook)
    Gumps.WaitForGump(89, 10000)
    rune_button = rune + 50
    Gumps.SendAction(89, rune_button)
    Misc.SendMessage("Rune: %s" % rune_button)
    Misc.Pause(500)


def RecallToAtlas(rune):
    # USE ATLAS
    Target.Cancel()
    Misc.Pause(50)
    Items.UseItem(runic_atlas)
    
    # PAGENATE
    page = rune / 16
    Misc.SendMessage("Page: %s" % page)
    for i in range(page):
        Gumps.WaitForGump(498, 10000)
        Gumps.SendAction(498, 1150)
    
    # SELECT RUNE
    Misc.SendMessage("Rune: %s" % rune)
    rune_button = rune + 100
    Gumps.WaitForGump(498, 10000)
    Gumps.SendAction(498, rune_button)
    
    # RECALL
    Gumps.WaitForGump(498, 10000)
    Gumps.SendAction(498, 4)
    
    Misc.Pause(3500)

LogToBoard()

while True:
    for rune in runes:
        Bank()
        #RecallToRunebook(rune)
        RecallToAtlas(rune)
        Lumberjacking()
        LogToBoard()
        