# ===============================
# Auto Lumberjacking V2
# Author: Cray
# ===============================

from Scripts.config import config

# LOAD CONFIG
container_serial = config.Lumberjacking[Misc.ShardName()][Player.Serial]["container_serial"]
atlas_serial = config.Lumberjacking[Misc.ShardName()][Player.Serial]["atlas_serial"]
bank_rune = config.Lumberjacking[Misc.ShardName()][Player.Serial]["bank_rune"]
runes = config.Lumberjacking[Misc.ShardName()][Player.Serial]["runes"]
position_offset_x = config.Lumberjacking[Misc.ShardName()][Player.Serial]["position_offset_x"]
position_offset_y = config.Lumberjacking[Misc.ShardName()][Player.Serial]["position_offset_y"]


# ITEM_ID
axes = {
    0x0F43: "hatchet",
    0x1443: "two handed axe"
}
log = 0x1BDD
board = 0x1BD7
store_items = {
    0x1BDD: "Log",
    0x1BD7: "Board",
    0x2F5F: "Switch",
    0x318F: "Bark Fragment",
    0x3190: "Parasitic Plant",
    0x3191: "Luminescent Fungi",
    0x3199: "Brilliant Amber",
    0x5738: "crystal shards"
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

def getAxe():
    # FIND LEFT HAND
    hand_item = Player.GetItemOnLayer("LeftHand")
    if hand_item:
        if hand_item.ItemID in axes:
            return hand_item
    # FIND BACKPACK
    for axe_id in axes:
        item = Items.FindByID(axe_id, -1, Player.Backpack.Serial)
        if item:
            return item

def equipAxe(axe):
    # UNEQUIP NOT AXES
    for layer in ["RightHand", "LeftHand"]:
        if Player.CheckLayer(layer):
            if Player.GetItemOnLayer(layer).ItemID in axes:
                return
            Player.UnEquipItemByLayer(layer)
            Misc.Pause(550)
    # EQUIP AXE
    Player.EquipItem(axe)
    Misc.Pause(550)

    
def lumberjacking():
    
    axe = getAxe()
    
    Journal.Clear()
    
    Timer.Create("Lumberjacking", 8000)
    while Player.Weight <= Player.MaxWeight :
        
        if not Timer.Check("Lumberjacking"):
            break
        
        if Journal.Search("not enough"):
            break
        
        equipAxe(axe)
        
        # TREE POSITION
        x = Player.Position.X + position_offset_x
        y = Player.Position.Y + position_offset_y
        map_id = Player.Map
        
        # TILE CHECK
        tiles = Statics.GetStaticsTileInfo(x, y, map_id)
        for i, tile in enumerate(tiles):
            if i == 1:
                Misc.SendMessage("TileID: %s" % tile.StaticID)
                
                # JACKING
                Target.Cancel()
                Misc.Pause(50)
                Items.UseItem(axe)
                Target.WaitForTarget(1000, False)
                Target.TargetExecute(x, y, tile.StaticZ, tile.StaticID)
                Misc.Pause(1000)

                
def turnLogToBoard():
    # LOG TO BOARD
    for log_color in log_colors.keys():
        item = Items.FindByID(log, log_color, Player.Backpack.Serial)
        if item:
            Target.Cancel()
            Misc.Pause(50)
            Misc.SendMessage(log)
            Items.UseItem(getAxe())
            Target.WaitForTarget(1000, False)
            Target.TargetExecute(item)
            Misc.Pause(500)

                
def recallAtlas(atlas_serial, rune):
    
    if not Items.FindBySerial(atlas_serial):
        Player.HeadMessage(33, "There is no Atlas Rune Book.")
        Misc.ScriptStop("auto_Lumberjacking.py")
    
    Items.UseItem(atlas_serial)
    
    # PAGENATION
    page = rune / 16
    for i in range(page):
        Gumps.WaitForGump(498, 10000)
        Gumps.SendAction(498, 1150)
    
    # SELECT RUNE
    Misc.SendMessage("Rune: {page}-{rune}".format(page=page, rune=rune))
    rune_button = rune + 100
    Gumps.WaitForGump(498, 10000)
    Gumps.SendAction(498, rune_button)
    
    # RECALL
    Gumps.WaitForGump(498, 10000)
    Gumps.SendAction(498, 4)
    
    Misc.Pause(3500)
    
            
def storeItems(container_serial):
    
    if Player.Weight <= Player.MaxWeight - 200:
        return
    
    recallAtlas(atlas_serial, bank_rune)
    
    Timer.Create("Store", 5000)
    for store_item in store_items.keys():
        while Items.FindByID(store_item, -1, Player.Backpack.Serial):
            
            if not Timer.Check("Store"):
                break
                
            item = Items.FindByID(store_item, -1, Player.Backpack.Serial)
            if item:
                if not container_serial:
                    Player.ChatSay(12, "bank")
                    Misc.Pause(300)
                    container_serial = Player.Bank
                Items.Move(item, container_serial, 0)
                Misc.Pause(550)
    
    Misc.Pause(750)

    

while True:
    for rune in runes:
        turnLogToBoard()
        storeItems(container_serial)
        recallAtlas(atlas_serial, rune)
        lumberjacking()
        