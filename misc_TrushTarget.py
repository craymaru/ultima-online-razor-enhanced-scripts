
def findTrushPouch():
    
    itemID = 0x09B0
    color = 0x09c4
    
    item = Items.FindByID(itemID, color, Player.Backpack.Serial)
    return item
    

def moveItem(target):
    item = Items.FindBySerial(target)
    if item and item.Movable:
        Items.Move(item.Serial, findTrushPouch(), item.Amount)
    
while True:
    target = Target.PromptTarget()
    Misc.Pause(100)
    moveItem(target)