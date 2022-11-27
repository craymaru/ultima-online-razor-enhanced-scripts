from System.Collections.Generic import List

def getShovels():
    filter = Items.Filter()
    filter.OnGround = False
    filter.Graphics = List[int]([0x0F39])
    filter.Hues = List[int]([0x0000])
    return Items.ApplyFilter(filter)


pos = Target.PromptGroundTarget("rock?")
while not Player.IsGhost:
    shovels = getShovels()
    
    if not len(shovels):
        Player.HeadMessage(33, "There is no shovels!")
        break
        
    for shovel in shovels:
        Items.UseItem(shovel)
        Misc.Pause(100)
        Target.TargetExecute(pos.X, pos.Y, pos.Z)
        Target.Cancel()
    Target.Cancel()
    Misc.Pause(1000 - len(shovels) * 40)