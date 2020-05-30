from System.Collections.Generic import List
from System import Byte


filter = Mobiles.Filter()
filter.Enabled = True
filter.RangeMax = 6
filter.Notorieties = List[Byte](bytes([1,3,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow

    
def attack(filter):
    
    enemies = Mobiles.ApplyFilter(filter)
    Mobiles.Select(enemies, 'Nearest')
    for enemy in enemies:
        Player.Attack(enemy)
        Target.ClearLast()
        Misc.Pause(100)
        

attack(filter)