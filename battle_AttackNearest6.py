from System.Collections.Generic import List
from System import Byte


filter = Mobiles.Filter()
filter.Enabled = True
filter.RangeMax = 24
filter.Notorieties = List[Byte](bytes([3,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow
    
    
def attack(filter):
    
    enemies = Mobiles.ApplyFilter(filter)
    enemy = Mobiles.Select(enemies, "Nearest")
    Misc.SendMessage(enemy.Name)
    Player.Attack(enemy)
    Target.ClearLast()
        
while True:
    attack(filter)
    Misc.Pause(200)