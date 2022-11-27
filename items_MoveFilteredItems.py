from System.Collections.Generic import List



def filterMoveItems(id, hue, source, dest, *, match):
    fil = Items.Filter()
    fil.Graphics = List[int]([id])
    fil.Hues = List[int]([hue])
    fil.OnGround = False
    
    items = Items.ApplyFilter(fil)
    items = list(filter(lambda item: item.Container == Player.Backpack.Serial, items))
    
    amount = len(items)
    if not items:
        return

        
    for i, item in enumerate(items):
        if match:
            for prop in item.Properties:
                if not match in str(prop):
                    continue
        
        Player.HeadMessage(5, str(i+1) + "/" + str(amount))
        Items.Move(item, dest, 0)
        Misc.Pause(600)
    
    Player.HeadMessage(63, "Done!")

    
# Run
Player.HeadMessage(55, "Item?")
item = Items.FindBySerial(Target.PromptTarget(""))
Player.HeadMessage(55, "Dest?")
dest = Target.PromptTarget("")
filterMoveItems(item.ItemID, item.Hue, item.Container, dest, match="exceptional")