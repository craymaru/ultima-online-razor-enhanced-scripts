from System.Collections.Generic import List
from System import Byte

def detect_mobile():
    
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 20
    fil.Notorieties = List[Byte](bytes([3,4,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow

    enemies = Mobiles.ApplyFilter(fil)
    Mobiles.Select(enemies,'Nearest')

    for enemy in enemies:
        if enemy.Hits >= enemy.HitsMax:
            Misc.Beep()
            Misc.Pause(500)

while True:
    detect_mobile()
    Misc.Pause(10000)