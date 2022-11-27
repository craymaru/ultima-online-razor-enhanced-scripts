from System.Collections.Generic import List
from System import Byte

filter = Mobiles.Filter()
filter.Enabled = True
filter.RangeMax = 12
filter.Notorieties = List[Byte](bytes([3])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow


def getNearestMob():
    enemies = Mobiles.ApplyFilter(filter)
    mob = Mobiles.Select(enemies, 'Nearest')
    return mob
    
while True:
    
    mob = getNearestMob()
    if mob:
        Spells.CastMagery("Fireball")
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(mob)
    
    Misc.Pause(10)