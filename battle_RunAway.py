from System.Collections.Generic import List
from System import Byte

def go(x, y):
    route = PathFinding.Route()
    route.X = x
    route.Y = y
    route.MaxRetry = 10
    route.IgnoreMobile = True
    PathFinding.Go(route)


def getAroundEnemies(range):
    filter = Mobiles.Filter()
    filter.RangeMax = range
    filter.Notorieties = List[Byte](bytes([3,4,5,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow
    enemies = Mobiles.ApplyFilter(filter)
    return len(enemies)
    

def stand(pos):
    Misc.Pause(2000)
    while True:
        if 7 < getAroundEnemies(2):
            break
        if getAroundEnemies(10) < 20 and Player.Position != pos:
            go(pos.X, pos.Y)
        Misc.Pause(1000)


pos = Player.Position
while not Player.IsGhost:
    stand(pos)
    go(pos.X - 7, pos.Y)
    stand(pos)
    go(pos.X, pos.Y - 7)
    stand(pos)
    go(pos.X + 7, pos.Y)
    stand(pos)
    go(pos.X, pos.Y + 7)