from System.Collections.Generic import List
from System import Byte


filter = Mobiles.Filter()
filter.Enabled = True
filter.RangeMax = 12
filter.Notorieties = List[Byte](bytes([3,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow


def mastery():
    
    if not Player.BuffsExist("Inspire"):
        Spells.CastMastery("Inspire")
        Misc.Pause(2000)
        
    if not Player.BuffsExist("Invigorate"):
        Spells.CastMastery("Invigorate")
        Misc.Pause(2000)
    


def discordance(filter):
    

    
    enemies = Mobiles.ApplyFilter(filter)
    Mobiles.Select(enemies,'Nearest')
    if enemies:
        Items.UseItemByID(0x0E9D) # Tambourine
        Misc.Pause(500)
    for enemy in enemies:
        Player.UseSkill("Discordance")
        # Target.WaitForTarget(10000, False)
        Misc.Pause(200)
        Target.TargetExecute(enemy)
        Misc.Pause(100)


while True:
    mastery()
    discordance(filter)
    Misc.Pause(1000)