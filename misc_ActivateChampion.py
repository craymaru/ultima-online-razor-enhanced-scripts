
def activateChampion():
    
    skull = Items.FindByID(0x1F18, 0x0000, Player.Backpack.Serial)

    Player.InvokeVirtue("Valor")
    Misc.Pause(200)
    Target.TargetExecute(skull)
    
    
activateChampion()