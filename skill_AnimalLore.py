from System.Collections.Generic import List
from System import Byte
fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 10
fil.Notorieties = List[Byte](bytes([3,4]))

enemies = Mobiles.ApplyFilter(fil)
Mobiles.Select(enemies,'Nearest')
for enemy in enemies:
    Target.ClearLast()
    Misc.Pause(50)
    Player.UseSkill("Animal Lore")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(enemy)
    break