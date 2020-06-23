# ITEM_ID
gold_id = 0x0EED
board_id = 0x1BD7
board_hue = 0x0000

# DEFINES
def ItemToBank(item_id, amount):
    item = Items.FindByID(item_id, 0, Player.Backpack.Serial)
    if item:
        Items.Move(item, Player.Bank.Serial, amount)
        Misc.Pause(700)

def GetItemFromBank(item_id, amount):
    item = Items.FindByID(item_id, 0, Player.Bank.Serial)
    if item:
        Items.Move(item, Player.Backpack.Serial, amount)
        Misc.Pause(500)

def IsPlayerHasItem(item_id):
    item = Items.FindByID(item_id, 0, Player.Backpack.Serial)
    if item:
        return True
    else:
        return False
        
def VenderSell(item_id):
    
    if IsPlayerHasItem(item_id):
    
        # SELL WITH AGENT SETTINGS
        Misc.WaitForContext(0x0000597A, 500)
        Misc.ContextReply(0x0000597A, 2)
        Misc.Pause(50)
      
def GetItemAmount(item_id, item_hue, container_serial):
    contains_amount = Items.ContainerCount(container_serial, item_id, item_hue)
    Misc.SendMessage(" >> " + str(contains_amount), 60)
    if contains_amount == 0:
        error

        
def hiding():
    if not Player.BuffsExist("Hiding"):
        if not Timer.Check("Skill"):
            Player.UseSkill("Hiding")
            Timer.Create("Skill", 10000)        
        
Player.ChatSay(12, "bank")


while True:
    hiding()
    ItemToBank(gold_id, 0)
    GetItemFromBank(board_id, 475)
    VenderSell(board_id)
    GetItemAmount(board_id, board_hue, Player.Bank.Serial)
    Misc.Pause(50)