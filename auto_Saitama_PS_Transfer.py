from System.Collections.Generic import List


gump_list = [
    {"id": 111922706, "tag": "Ultimate Power Scroll Book Top"},
    {"id": 3002212122, "tag": "Ultimate Power Scroll Book Botom"},
    {"id": 2556333534, "tag": "Power Scroll Transfar Barrel"}
]


def getTransferBarrel():
    filter = Items.Filter()
    filter.Graphics = List[int]([0x0E77])
    filter.Hues = List[int]([0x047e])
    filter.RangeMax = 5
    filter.OnGround = True
    filter.Movable = False
    return Items.Select(Items.ApplyFilter(filter), "Nearest")
    

def closeGumps(gump_list):
    Misc.Pause(200)
    for g in gump_list:
        Gumps.CloseGump(g["id"])
    Misc.Pause(200)


def transfer(barrel_serial):
    Misc.WaitForContext(0x400000EA, 10000)
    Misc.ContextReply(0x400000EA, 0)
    Gumps.WaitForGump(2556333534, 10000)
    Gumps.SendAction(2556333534, 1)


# Run
barrel = getTransferBarrel() 

closeGumps(gump_list)
Items.UseItem(0x50EB8476)

Misc.SendMessage("---1")

while True:
    Misc.Pause(500)
    Gumps.SendAction(111922706, 1) # Open scroll list
    Gumps.WaitForGump(111922706, 10000)
    Gumps.WaitForGump(3002212122, 10000)
    current = Gumps.CurrentGump()
    Misc.SendMessage(current, 55)
    
    if current == 3002212122:
        break
    
    
for i in range(100):
    Gumps.WaitForGump(3002212122, 1000)
    Gumps.SendAction(3002212122, 100) # Extract top scroll

closeGumps(gump_list)
transfer(barrel.Serial)