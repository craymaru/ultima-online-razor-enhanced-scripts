from System.Collections.Generic import List
from System import Byte


filter = Mobiles.Filter()
filter.Enabled = True
filter.RangeMax = 20
filter.Notorieties = List[Byte](bytes([3,4]))

while True:
    last_enemy = None
    if Player.WarMode:
        Player.SetWarMode(False)
        
    enemies = Mobiles.ApplyFilter(filter)
    Mobiles.Select(enemies,'Nearest')
    for enemy in enemies:
        if not Player.HasSpecial:
            if enemy.Name == "Swoop" and enemy.Hits == enemy.HitsMax:
                if not Player.BuffsExist("Invisibility"):
                    Target.Cancel()
                    Spells.CastMagery("Invisibility")
                    Target.WaitForTarget(3000, False)
                    Target.Self()
                    Misc.Pause(50)
            
                if Player.BuffsExist("Invisibility"):
                    Player.Attack(enemy)
                    Target.ClearLast()
                    Misc.Pause(10000)
                    
                if Player.WarMode:
                    Player.SetWarMode(False)
                    
    Misc.Pause(1000)