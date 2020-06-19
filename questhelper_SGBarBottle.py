from System.Collections.Generic import List
#put bottles on scavenger
piratefil = Mobiles.Filter()
piratefil.Enabled = True
piratefil.Bodies = List[int]((0x0190,0x0190))
piratefil.RangeMax = 50

pirates = Mobiles.ApplyFilter(piratefil)
Misc.Pause(100)
pirate = Mobiles.Select(pirates,'Nearest')
if Items.BackpackCount(0x099B) > 0 and Player.Hits == Player.HitsMax and pirate:
    Items.UseItemByID(0x099B,-1)
    Target.WaitForTarget(500,False)
    Target.TargetExecute(pirate)
    Misc.Pause(800)
if Items.BackpackCount(0x099B) == 0:
    Misc.SendMessage(str(Items.BackpackCount(0x099B))+' Bottles Left',43)
if pirate == None:
     Misc.SendMessage('No Pirates in Range',43)
