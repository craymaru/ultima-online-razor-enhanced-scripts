from System.Collections.Generic import List
import re



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


def getGold(amount=53000):
    
    filter = Items.Filter()
    filter.Enabled = True
    filter.OnGround = False
    filter.IsCorpse = False
    filter.Graphics = List[int]([0x0EED])
    items = Items.ApplyFilter(filter)
    
    for item in items:
        Misc.SendMessage(item.Amount)
        if item.Container == Player.Backpack.Serial and amount <= item.Amount :
            return item


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

    
while True:
    sendGold()