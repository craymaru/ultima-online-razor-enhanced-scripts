from System.Collections.Generic import List
from System import Byte
fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 10
fil.Notorieties = List[Byte](bytes([3,4]))

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