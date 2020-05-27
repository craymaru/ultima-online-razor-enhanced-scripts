from System.Collections.Generic import List 

loot_time_ms = 5000


looted_corpses = []

def goToLocation(x, y):
    route = PathFinding.Route()
    route.X = x
    route.Y = y
    route.MaxRetry = -1
    PathFinding.Go(route)
    Misc.Pause(50)

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
            goToLocation(corpse.Position.X, corpse.Position.Y)
            looted_corpses.append(corpse.Serial)
            Misc.Pause(loot_time_ms)