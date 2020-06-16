from System.Collections.Generic import List
import re



# GOLD SENDINGS

def getSendingBag():
    # FIND SENDINGBAG AND CHARGE POWDER
    
    # CHARGE POWDER
    def chargePowder(bag):
        
        powder = Items.FindByID(0x26B8, 0x0000, Player.Backpack.Serial)
        if powder:
            if Scavenger.Status():
                Scavenger.Stop()
            Items.UseItem(powder)
            Misc.Pause(200)
            if not Scavenger.Status():
                Scavenger.Start()
            Target.TargetExecute(bag)
            Player.HeadMessage(54, "Charged powder!")
            return bag
        else:
            Player.HeadMessage(15, "You have not a powder!")
    
    # BAG CHECK
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


def getGold(amount=55000):
    # FILTER BACKPACK GOLD
    filter = Items.Filter()
    filter.Enabled = True
    filter.OnGround = False
    filter.IsCorpse = False
    filter.Graphics = List[int]([0x0EED])
    golds = Items.ApplyFilter(filter)
    
    for gold in golds:
        if gold.Container == Player.Backpack.Serial and amount <= gold.Amount :
            return gold


def sendGold(amount):
    # SEND GOLD TO BANK
    gold = getGold(amount)
    sendingBag = getSendingBag()
    
    if gold:
        if sendingBag:
            if Scavenger.Status():
                Scavenger.Stop()
            Misc.Pause(550)
            Items.UseItem(sendingBag)
            Misc.Pause(550)
            Target.TargetExecute(gold)
            Player.HeadMessage(90, "Send!")
            Misc.Pause(650)
            if not Scavenger.Status():
                Scavenger.Start()
    else:
        Misc.Pause(1000)

  
# PATHFINDINGS


def goToLocation(x, y):
    # GO TO LOCATION
    route = PathFinding.Route()
    route.X = x
    route.Y = y
    route.MaxRetry = 5
    PathFinding.Go(route)
    Misc.Pause(50)


def findGold():
    # FILTER GROUND GOLD
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
    # GO TO GOLD POS
    gold = findGold()
    if gold:
        Player.HeadMessage(66, str(gold.Position))
        goToLocation(gold.Position.X, gold.Position.Y)

    

def hiding():
    # HIDING WHEN NOT HIDING
    if not Player.BuffsExist("Hiding") and 100 <= Player.GetSkillValue("Hiding"):
        Player.UseSkill("Hiding")
        
    if not Player.BuffsExist("Hiding") and not Player.BuffsExist("Invisibility"):
        Spells.CastMagery("Invisibility")
        Target.WaitForTarget(2000, False)
        Target.Self()

def castWraithForm():
    if not Player.BuffsExist("Wraith Form") and 30 <= Player.GetSkillValue("Necromancy"):
        Spells.CastNecro("Wraith Form")
        Misc.Pause(2000)


def countGold():
    # GOLD COUNTER
    
    global beforeGold
    
    try:
        beforeGold
        pass
    except NameError:
        beforeGold = None
    
    if not beforeGold == Player.Gold:
        Player.HeadMessage(54, "Gold: " + str(Player.Gold))
        beforeGold = Player.Gold


def scavengeGold(time):
    if not Timer.Check("ScavengeTime"):
            Player.HeadMessage(66, "Finding...")
            goToGold()
            Timer.Create("ScavengeTime", time)


            
while not Player.IsGhost:
    
    castWraithForm()
    hiding()
    sendGold(55000)
    scavengeGold(6000)
    countGold()
    

        

