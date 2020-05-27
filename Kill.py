from System.Collections.Generic import List
from System import Byte


fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 12
fil.Notorieties = List[Byte](bytes([3,4,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow

Player.SetWarMode(False)
enemies = Mobiles.ApplyFilter(fil)
Mobiles.Select(enemies,'Nearest')
for enemy in enemies:
    if not Player.HasSpecial:
        # Player.WeaponSecondarySA()
        Player.Attack(enemy)
        Target.ClearLast()
        Misc.Pause(500)
        Player.SetWarMode(False)