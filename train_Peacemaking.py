
def peacemaking():
    Player.UseSkill("Peacemaking")
    Target.WaitForTarget(1000, True)
    Target.TargetExecute(Player.Serial)
    



while True:
    
    Items.UseItemByID(0x0E9D)
    Misc.Pause(500)
    peacemaking()
    Misc.Pause(10500)
    