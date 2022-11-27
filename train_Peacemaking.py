Instrument = 0x0E9D


def peacemaking():
    Player.UseSkill("Peacemaking")
    Target.WaitForTarget(1000, True)
    Target.TargetExecute(Player.Serial)
    

def main():
    while True:
        Journal.Clear()
        
        Items.UseItemByID(Instrument)
        Misc.Pause(100)
        
        peacemaking()
        
        Misc.Pause(500)
        
        if Journal.SearchByType("You attempt to calm everyone, but fail.", "System"):
            Misc.Pause(10000)
        else:
            Misc.Pause(5000)


main()