from System.Collections.Generic import List 

looted_corpses = []

def GoToLocation(x, y):
    Coords = PathFinding.Route()
    Coords.X = x
    Coords.Y = y
    Coords.MaxRetry = -1
    PathFinding.Go(Coords)
    Misc.Pause(50)

def WhereMobile():
    mobile = Mobiles.FindBySerial(0x0001B49E)
    pos = mobile.Position
    Misc.SendMessage(mobile.Position)
    return pos

def findCorpse():
    corpse = Items.Filter()
    corpse.Enabled = True
    corpse.OnGround = True
    corpse.Movable = False
    corpse.RangeMax = 25
    corpse.IsCorpse = True
    corpses = Items.ApplyFilter(corpse)
    Misc.Pause(50)
    return corpses

  
while True:
    for corpse in findCorpse():
        if not corpse.Serial in looted_corpses:
            Misc.SendMessage(corpse.Name)
            Misc.SendMessage(corpse.Serial)
            Misc.SendMessage(corpse.Position)
            GoToLocation(corpse.Position.X, corpse.Position.Y)
            looted_corpses.append(corpse.Serial)
            Misc.Pause(5000)