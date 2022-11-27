from System.Collections.Generic import List


def getAFBag(container=Player.Backpack.Serial):
    return Items.FindByID(0x0E76, 0x0a3f, container)
    
    
def getWallet(container=Player.Backpack.Serial):
    return Items.FindByID(0x46A6, 0x0021, container)
    
    
def getYellowBag():
    filter = Items.Filter()
    filter.Graphics = List[int]([0x0E76])
    filter.Hues = List[int]([0x0035])
    filter.OnGround = False
    filter.Movable = True
    items = Items.ApplyFilter(filter)
    return Items.Select(items, "Nearest")
    


def moveItem(id, color, dest, *, threshold=0, frm=Player.Backpack.Serial):
    item = Items.FindByID(id, color, frm)
    if not item or not dest:
        return
    
    if item.Amount <= threshold:
        return
    
    Items.Move(item, dest, 0)
    Misc.Pause(500)
        

gold = [0x0EED, 0x0000]
arrow = [0x0F3F, 0x0000]
bone = [0x0F80, 0x0000]
map = [0x14EC, 0x0000]

# Run
while not Player.IsGhost:
    Misc.SendMessage("Looting...", 10)
    Player.ChatSay(55, "[gr")
    Misc.Pause(500)
    moveItem(*gold, getWallet(), threshold=30000)
    moveItem(*arrow, getAFBag(), threshold=10)
    moveItem(*bone, getAFBag(), threshold=10)
    moveItem(*map, getYellowBag())
    Misc.Pause(5000)