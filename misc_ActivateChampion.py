from System.Collections.Generic import List 

def filterSkull():
    # FILTER SKULL
    filter = Items.Filter()
    filter.Graphics = List[int]([0x1F18])
    filter.OnGround = True
    filter.Movable = False
    filter.RangeMax = 5
    return filter


def activateChampion(filter):
    # ACTIVATE IDOL OF CHAMPION
    skulls = Items.ApplyFilter(filter)
    skull = Items.Select(skulls, "Nearest")
    # Use Valor to Skull
    if skull:
        Player.InvokeVirtue("Valor")
        Misc.Pause(200)
        Target.TargetExecute(skull)
    
skullFilter = filterSkull()
activateChampion(skullFilter)