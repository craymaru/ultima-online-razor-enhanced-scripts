from System.Collections.Generic import List
# sg armor assistant written by mourn 8182 discord contact
armorId = 0x151A   #Cursed Suit of Armor
cphylactId = 0x4686   #Corrupt Phylactery
cphylactColor = 0x081B
pphylactId = 0x4686 #Purified Phylactery
pphylactColor = 0x0000

FFilter = Items.Filter()
FFilter.RangeMax = 2
FFilter.OnGround = True
FFilter.Enabled = True
FFilter.Movable = False
flameId = List[int]((0x19AB, 0x19AB))
FFilter.Graphics = flameId 

Armorfilter = Items.Filter()
Armorfilter.RangeMax = 4
Armorfilter.OnGround = True
Armorfilter.Enabled = True
Armorfilter.Movable = False
armorIds = List[int]((0x151A,0x1512))
Armorfilter.Graphics = armorIds

def purify():    
    if Items.BackpackCount(cphylactId, cphylactColor) >= 1:
        Flames = Items.ApplyFilter(FFilter)
        if len(Flames)> 0:
            flame = Items.Select(Flames,'Nearest')
            if Items.BackpackCount(cphylactId, cphylactColor) > 0:
                Items.UseItemByID(cphylactId,cphylactColor)
                Target.WaitForTarget(1000,False)
                Target.TargetExecute(flame)
                Misc.Pause(1500)
                
def throw():
       
    if Items.BackpackCount(pphylactId, pphylactColor) >= 1:
        armors = Items.ApplyFilter(Armorfilter)
        if len(armors) > 0:
            armor = Items.Select(armors,'Nearest')
            if Player.InRangeItem(armor,4):
                if Items.BackpackCount(pphylactId, pphylactColor) > 0:                    
                    Items.UseItemByID(pphylactId,pphylactColor)
                    Target.WaitForTarget(1000,False)
                    Target.TargetExecute(armor)
                    Misc.Pause(1500)
                
while True:
    purify()
    throw()
    Misc.Pause(200)
        