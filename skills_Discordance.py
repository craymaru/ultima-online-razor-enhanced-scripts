from System.Collections.Generic import List
from System import Byte


fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 12
fil.Notorieties = List[Byte](bytes([3,4,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow

while True:
    enemies = Mobiles.ApplyFilter(fil)
    Mobiles.Select(enemies,'Nearest')
    for enemy in enemies:

        Player.UseSkill("Discordance")
        # Target.WaitForTarget(10000, False)
        Misc.Pause(200)
        Target.TargetExecute(enemy)
        Misc.Pause(500)
