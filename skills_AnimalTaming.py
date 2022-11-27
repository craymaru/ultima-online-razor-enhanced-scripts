target = Target.PromptTarget("Taming?")
mobile = Mobiles.FindBySerial(target)

while True:
    Journal.Clear()
    
    while True:
        Player.UseSkill("Animal Taming")
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(target)
        
        if Journal.SearchByName("You start to tame the creature", Player.Name):
            break
        
    while True:
        if Journal.SearchByName("You fail to tame the creature.", mobile.Name):
            break
        Misc.Pause(100)
    
    if Journal.SearchByName("It seems to accept you as master.", Player.Name):
        break
    if Journal.SearchByName("That animal looks tame already.",mobile.Name):
        break
    
    Misc.Pause(100)