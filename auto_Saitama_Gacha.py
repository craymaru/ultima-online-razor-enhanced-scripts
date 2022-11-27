from System.Collections.Generic import List
import re


GACHA_CHUNK = 100
TRADE_GACHA_ITEM_LIST = [
    {"id": 0x14F0, "color": 0x0000, "name": "Small Soul Forge"},
    {"id": 0x1541, "color": 0x0485, "name": '"Crimson Sash"'},
    {"id": 0x20E1, "color": 0x0000, "name": "Rideable Polar Bear Statuette"},
    {"id": 0x367A, "color": 0x0000, "name": "Name: an Idol Master"},
    {"id": 0x367A, "color": 0x0000, "name": "A Heritage Token"}
]
RE_PATTERN = re.compile(r": ([\d]+)\/156")


def useAllItems(id, color, container=Player.Backpack.Serial):
    while True:
        item = Items.FindByID(id, color, container)
        if not item:
            break
        Items.UseItem(item)
        Misc.Pause(10)


def moveAllItems(id, color, dest, container=Player.Backpack.Serial):
    while True:
        item = Items.FindByID(id, color, container)
        if not item:
            break
        Items.Move(item, dest, 0)
        Misc.Pause(600)
        
        
def moveItems(items, dest):
    for item in items:
        Items.Move(item, dest, 0)
        Misc.Pause(600)
        
        
def getItemsByName(id, color, name, container=Player.Backpack):
    fil = Items.Filter()
    fil.Graphics = List[int]([id])
    fil.Hues = List[int]([color])
    fil.OnGround = False
    items = Items.ApplyFilter(fil)
    if items:
        items = list(filter(lambda item: item.Container == container.Serial and str(item.Properties[0]).title() == str(name).title(), items))
        
        return items


def getNearestGroundItem(id, color, range):
    filter = Items.Filter()
    filter.OnGround = True
    filter.Movable = False
    filter.RangeMax = range
    filter.Graphics = List[int]([id])
    filter.Hues = List[int]([color])
    items = Items.ApplyFilter(filter)
    return Items.Select(items, "Nearest")

        
def getGacha():
    gacha = getNearestGroundItem(0x1947, 0x0505, 2)
    if not gacha:
        Player.HeadMessage(33, "There is no Gacha!")
    return gacha


def getWyrmBox():
    box = getNearestGroundItem(0x2DF2, 0x0813, 2)
    if not box:
        Player.HeadMessage(33, "There is no Wyrm Box!")
    return box
    

def getContainer(message):
    Player.HeadMessage(55, message)
    target = Target.PromptTarget("")
    item = Items.FindBySerial(target)
    
    if not item:
        Player.HeadMessage(33, "There is no item!")
        end()
        
    if not item.IsContainer:
        Player.HeadMessage(33, "Not Container!")
        end()
    
    Items.UseItem(item)
    Misc.Pause(100)
    
    return item


def getIdolBooks(container, completed=False):
    Items.UseItem(container)
    Misc.Pause(600)
    
    fil = Items.Filter()
    fil.Graphics = List[int]([0x2259])
    fil.Hues = List[int]([0x0492])
    fil.OnGround = False
    books = Items.ApplyFilter(fil)
    if completed:
        return list(filter(lambda item: item.Container == container.Serial and not "/156" in str(item.Properties[3]), books))
    books = list(filter(lambda item: item.Container == container.Serial and "/156" in str(item.Properties[3]), books))
    books = sorted(books, key=getIdolAmount, reverse=True)
    
    Player.HeadMessage(5, "Find " + str(len(books)) + " Idol Books.")
    
    return books

    
def getIdolAmount(idol_book):
    match_obj = RE_PATTERN.search(str(idol_book.Properties[3]))
    if match_obj:
        num_str = match_obj.groups()[0]
        #Misc.SendMessage(int(num_str))
        return int(num_str)
    

# Prosess Methods

def playGacha(times):
    gacha = getGacha()
    if not gacha:
        return
    for i in range(times):
        Items.UseItem(gacha)
        Misc.Pause(20)
    Misc.Pause(100)


def useGachaBall():
    useAllItems(0x3666, -1)
    
    
def addIdolsToBooks(books):
    for book in books:
        Misc.WaitForContext(book.Serial, 3000)
        Misc.ContextReply(book.Serial, 0)

        
def tradeCompletedBooks(container):
    for book in getIdolBooks(container, True):
        Items.Move(book, getGacha(), 0)
        Misc.Pause(600)
        
    
def tradeGachaItems():
    for item in TRADE_GACHA_ITEM_LIST:
        Misc.SendMessage(item["name"], 5)
        items = getItemsByName(item["id"], item["color"], item["name"])
        if not items:
            continue
        moveItems(items, getGacha())
        

def tradeFollowersScrolls():
    if not Items.FindByID(0x14F0, 0x005b, Player.Backpack.Serial):
        return
    Items.UseItem(getWyrmBox())
    while Items.FindByID(0x14F0, 0x005b, Player.Backpack.Serial):
        Gumps.WaitForGump(2510313894, 10000)
        Gumps.SendAction(2510313894, 300)
        Misc.Pause(300)
        Misc.ResponsePrompt("1")
        Misc.Pause(200)
    Gumps.CloseGump(2510313894)
        
        
def putChecksToMyWallet():
    wallet = Items.FindByID(0x46A6, 0x0021, Player.Backpack.Serial)
    if not wallet:
        return
    moveAllItems(0x14F0, 0x0034, wallet)
        

def moveRaiseMaxLevelScroll(container):
    moveAllItems(0x14F0, 0x0481, container)


def cooltime(seconds):
    for i in range(seconds):
        Player.HeadMessage(65, "Cooldown... " + str(seconds - i))
        Misc.Pause(1000)


# Run
Player.HeadMessage(33, "CAUTION: Clear away the other Power Scrolls before you start this.")
idol_bag = getContainer("Idol Books Container?")
ps_bag = getContainer("Raise Max Level Container?")

while True:
    # Gacha
    playGacha(100)
    useGachaBall()

    # Idol Books
    addIdolsToBooks(getIdolBooks(idol_bag))
    tradeCompletedBooks(idol_bag)

    # Item Organize
    tradeGachaItems()
    putChecksToMyWallet()
    tradeFollowersScrolls()
    moveRaiseMaxLevelScroll(ps_bag)

    cooltime(1)

