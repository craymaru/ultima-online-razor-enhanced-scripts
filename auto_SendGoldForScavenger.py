from System.Collections.Generic import List
import re



# SEND GOLD

def getSendingBag():
    

    def chargePowder(bag):
        
        powder = Items.FindByID(0x26B8, 0x0000, Player.Backpack.Serial)
        if powder:
            Items.UseItem(powder)
            Misc.Pause(200)
            Target.TargetExecute(bag)
            Player.HeadMessage(54, "Charged powder!")
            return bag
        else:
            Player.HeadMessage(34, "You have not a powder!")
    

    bag = Items.FindByID(0x0E76, 0x08ad, Player.Backpack.Serial) # BlueBag
    if not bag:
        bag = Items.FindByID(0x0E76, 0x089b, Player.Backpack.Serial) # RedBag

    if bag:
        
        # CHECK CHARGES
        for prop in bag.Properties:
            match = re.match("^charges: (\d+)$", str(prop))
            if match:
                if int(match.groups()[0]) == 0:
                    Player.HeadMessage(33, str(prop))
                    chargePowder(bag)
                    
        return bag
    else:
        Player.HeadMessage(54, "You have not sending bag!")


def getGold(amount=45000):
    
    filter = Items.Filter()
    filter.Enabled = True
    filter.OnGround = False
    filter.IsCorpse = False
    filter.Graphics = List[int]([0x0EED])
    golds = Items.ApplyFilter(filter)
    
    for gold in golds:
        if gold.Container == Player.Backpack.Serial and amount <= gold.Amount :
            return gold


def sendGold():
    
    gold = getGold()
    sendingBag = getSendingBag()
    
    if gold:
        if sendingBag:
            Items.UseItem(sendingBag)
            Misc.Pause(200)
            Target.TargetExecute(gold)
            Misc.Pause(650)
    else:
        Misc.Pause(1000)

  
# PATHFINDING


def goToLocation(x, y):
    route = PathFinding.Route()
    route.X = x
    route.Y = y
    route.MaxRetry = 5
    PathFinding.Go(route)
    Misc.Pause(50)


def findGold():
    filter = Items.Filter()
    filter.Enabled = True
    filter.IsCorpse = False
    filter.Graphics = List[int]([0x0EED])
    filter.RangeMax = 25
    filter.OnGround = True
    filter.Movable = True
    golds = Items.ApplyFilter(filter)
    gold = Items.Select(golds, "Random")
    return gold


def goToGold():
    
    gold = findGold()
    if gold:
        Player.HeadMessage(1150, str(gold.Position))
        goToLocation(gold.Position.X, gold.Position.Y)

    

def hiding():
    # HIDING
    if not Player.BuffsExist("Hiding") and Player.GetSkillValue("Hiding") <= 100:
        Player.UseSkill("Hiding")


def countGold():
    
    global beforeGold
    
    if not beforeGold:
        beforeGold = None

while True:
    
    hiding()
    sendGold()
    
    if not Timer.Check("ScavengeTime"):
        goToGold()
        Timer.Create("ScavengeTime", 6000)

   
    if not beforeGold == Player.Gold:
        Player.HeadMessage(54, Player.Gold)
        beforeGold = Player.Gold

        