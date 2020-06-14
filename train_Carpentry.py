from Scripts.glossary.colors import colors
from Scripts.glossary.crafting.carpentry import FindCarpentryTool, carpentryCraftables
from Scripts.glossary.items.containers import FindTrashPouch


board_id = 0x1BD7
gump_id = 949095101


def useToolFirst(tool_gump):
    Gumps.WaitForGump(tool_gump, 2000)
    if Gumps.LastGumpTextExist("You have worn out your tool!") \
    or not Gumps.CurrentGump() == tool_gump:
        item = FindCarpentryTool(Player.Backpack)
        if item:
            Items.UseItem(item)
        else:
            end()


def createItem(itemToCraft):
    
    useToolFirst(gump_id)
    
    for path in itemToCraft.gumpPath:
        Gumps.WaitForGump( path.gumpID, 2000 )
        if Gumps.CurrentGump() == path.gumpID and not Gumps.LastGumpTextExist(itemToCraft.name):
            Gumps.SendAction( path.gumpID, path.buttonID )
        if Gumps.CurrentGump() == path.gumpID and Gumps.LastGumpTextExist(itemToCraft.name):
            Gumps.SendAction( path.gumpID, path.buttonID )
        

def clean(item_id):
    
    def getCleanupPouch():
        cleanup_pouch = Items.FindByID(0x09B0, 0x09c4, Player.Backpack.Serial)
        return cleanup_pouch
    
    while Items.FindByID(item_id, 0x0000, Player.Backpack.Serial):
        item = Items.FindByID(item_id, 0x0000, Player.Backpack.Serial)
        if item:
            if not Timer.Check("MoveItem"):
                Items.Move(item, getCleanupPouch(), 1)
                Timer.Create("MoveItem", 550)
        Misc.Pause(100)
        
        
def getBankItem(item, less_amount, get_amount):
    if Items.BackpackCount(item, 0x0000) < less_amount:
        if not Player.Bank:
            Player.ChatSay(80, "bank")
        Misc.Pause(100)
        item = Items.FindByID(item, 0x0000, Player.Bank.Serial)
        Items.Move(item, Player.Backpack.Serial, get_amount)
        Misc.Pause(550)


while True:
    getBankItem(board_id, 100, 200)
    
    if carpentryCraftables["bokuto"].minSkill <= Player.GetRealSkillValue("Carpentry"):
        itemToCraft = carpentryCraftables["bokuto"]
    elif carpentryCraftables["wooden shield"].minSkill <= Player.GetRealSkillValue("Carpentry"):
        itemToCraft = carpentryCraftables["wooden shield"]
    elif carpentryCraftables["medium crate"].minSkill <= Player.GetRealSkillValue("Carpentry"):
        itemToCraft = carpentryCraftables["medium crate"]
        
    createItem(itemToCraft)
    clean(itemToCraft.itemID)
