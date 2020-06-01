from System.Collections.Generic import List
from System import Byte

tambourine = 0x0E9D

def Instrumental():
    item = Items.FindByID(tambourine, -1, Player.Backpack.Serial)
    Items.UseItem(item)
    Misc.Pause(50)

def TrainDiscordance():
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 7
    fil.Notorieties = List[Byte](bytes([3,4]))

    Player.SetWarMode(False)
    enemies = Mobiles.ApplyFilter(fil)
    Mobiles.Select(enemies,'Nearest')
    for enemy in enemies:
        if enemy:
            Player.UseSkill("Discordance")
            Target.WaitForTarget(3000, False)
            Target.TargetExecute(enemy)
            Misc.Pause(10000)
        
    Spells.CastMagery("Invisibility")
    Target.WaitForTarget(5000, False)
    Target.Self()
    Misc.Pause(18000)
    Spells.CastMagery("Heal")
    Target.WaitForTarget(5000, False)
    Target.Self()
    Misc.Pause(100)
    
while True:
    Instrumental()
    TrainDiscordance()
