from System.Collections.Generic import List

def getGroundObjectFilter(id, color, range=15):
    filter = Items.Filter()
    filter.Graphics = List[int]([id])
    filter.Hues = List[int]([color])
    filter.OnGround = True
    filter.Movable = False
    filter.RangeMax = range
    return filter
    
    
def getPentagramFilter():
    filter = Items.Filter()
    filter.Graphics = List[int]([0x0FEA])
    filter.Hues = List[int]([0x0000])
    filter.OnGround = True
    filter.Movable = False
    filter.RangeMax = 5
    return filter


def isPentagramExist(filter):
    # FIND PENTAGRAM
    items = Items.ApplyFilter(filter)
    item = Items.Select(items, "Nearest")
    if item:
        return True
    else:
        return False


def activateChampion(filter):
    # ACTIVATE IDOL OF CHAMPION
    skulls = Items.ApplyFilter(filter)
    skull = Items.Select(skulls, "Nearest")
    # Use Valor to Skull
    if skull:
        Player.InvokeVirtue("Valor")
        Misc.Pause(200)
        Target.TargetExecute(skull)


# FILTERS
skullFilter = getGroundObjectFilter(0x1F18, 0x0000, 20)
pentagramFilter = getGroundObjectFilter(0x0FEA, 0x0000, 20)
deactiveStairsFilter = getGroundObjectFilter(0x0759, 0x0497, 20)


# RUN
while not Player.IsGhost:
    
    if isPentagramExist(getGroundObjectFilter(0x1F18, 0x0000, 20)):
        activateChampion(getSkull)
    Misc.Pause(5000)