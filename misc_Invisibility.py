def Invisibility():
    while True:
        if not Player.BuffsExist("Invisibility"):
            Target.Cancel()
            Spells.CastMagery("Invisibility")
            Target.WaitForTarget(3000, False)
            Target.Self()
        if Player.WarMode:
            Player.SetWarMode(False)
        Misc.Pause(100)
        
Invisibility()
