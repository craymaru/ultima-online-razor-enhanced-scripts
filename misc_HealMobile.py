Misc.SendMessage("PET?", 53)
target = Target.PromptTarget()

def HealMobile():
    mobile = Mobiles.FindBySerial(target)
    if mobile.Hits < mobile.HitsMax * 0.9:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(5000, False)
        Target.TargetExecute(target)
        
while True:
    HealMobile()
    Misc.Pause(1000)