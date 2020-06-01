from System.Collections.Generic import List
from System import Byte


cray_serial = 0x00020008


filter = Mobiles.Filter()
filter.Enabled = True
filter.RangeMax = 12
filter.Notorieties = List[Byte](bytes([3,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow

    
def autoInvisibility(cray_serial):
    # If you can not find specific mobile, cast Invisibility to yourself.
    # 
    # Params:
    #   specific mobile serial

    def findMobile():
        mobile = Mobiles.FindBySerial(cray_serial)
        if mobile:
            if mobile.Visible:
                Misc.Pause(4000)
                return mobile.Visible
            else:
                return False
        else:
            return False

    while not findMobile():
        if Player.BuffsExist("Inspire"):
            Spells.CastMastery("Inspire")
            Misc.Pause(2000)
        
        if Player.BuffsExist("Invigorate"):
            Spells.CastMastery("Invigorate")
            Misc.Pause(2000)
    
        if not Player.BuffsExist("Invisibility"):
            Spells.CastMagery("Invisibility")
            Target.WaitForTarget(1000, False)
            Target.TargetExecute(Player.Serial)
        
        Misc.Pause(200)


def mastery():
    
    if not Player.BuffsExist("Inspire"):
        Spells.CastMastery("Inspire")
        Misc.Pause(2000)
        
    if not Player.BuffsExist("Invigorate"):
        Spells.CastMastery("Invigorate")
        Misc.Pause(2000)


def discordance(filter):
    
    enemies = Mobiles.ApplyFilter(filter)
    enemy = Mobiles.Select(enemies, "Nearest")
    if enemy:
        Items.UseItemByID(0x0E9D) # Tambourine
        Misc.Pause(500)
        Player.UseSkill("Discordance")
        Misc.Pause(200)
        Target.TargetExecute(enemy)
        Misc.Pause(100)


def castArchCure(mobile_serial):
    mobile = Mobiles.FindBySerial(mobile_serial)
    if mobile.Poisoned:
        Spells.CastMagery("Arch Cure")
        Misc.Pause(1000)
        Target.TargetExecute(mobile.Serial)
        

while True:
    autoInvisibility(cray_serial)
    mastery()
    discordance(filter)
    castArchCure(cray_serial)
    castArchCure(Player.Serial)
    Misc.Pause(1000)