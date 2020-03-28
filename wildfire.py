def IsPlayerHealthy():
    if Player.Poisoned == True or Player.Hits <= Player.HitsMax * 0.80:
        return False
    else:
        return True



def CurePoison():
    while Player.Poisoned:
        cure_failed = False
        if cure_failed == True:
            Target.Cancel()
            Spells.CastMagery("Arch Cure")
            Target.WaitForTarget(1000, False)
            Target.Self()
        else:
            Target.Cancel()
            Spells.CastMagery("Cure")
            Target.WaitForTarget(1000, False)
            Target.Self()
            cure_failed = Player.Poisoned
        Misc.Pause(50)

def Heal():
    while Player.Hits <= Player.HitsMax * 0.80:
        if Player.Hits <= Player.HitsMax * 0.60:
            Target.Cancel()
            Spells.CastMagery("Greater Heal")
            Target.WaitForTarget(3000, False)
            Target.Self()
        else:
            Target.Cancel()
            Spells.CastMagery("Heal")
            Target.WaitForTarget(1000, False)
            Target.Self()
        Misc.Pause(50)

def Wildfire():
    Spells.CastSpellweaving("Wildfire")
    Target.WaitForTarget(3000, False)
    Target.Self()

while True:
    if IsPlayerHealthy():
        Wildfire()
    else:
        CurePoison()
        Heal()
