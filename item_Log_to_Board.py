Misc.SendMessage("AXE?", 53)
axe_serial = Target.PromptTarget()
log_id = 0x1BDD
board_id = 0x1BD7

log_colors = {
    0x0000: "Log",
    0x07da: "Ork",
    0x04a7: "Ash",
    0x04a8: "Yew",
    0x04a9: "Heartwood",
    0x04aa: "Bloodwood",
    0x047f: "Frostwood"
}

# DEFINES
def PutItemToBank(item_id, amount):
    item = Items.FindByID(item_id, -1, Player.Backpack.Serial)
    if item:
        Items.Move(item, Player.Bank.Serial, amount)
        Misc.Pause(700)

def GetItemFromBank(item_id, amount):
    item = Items.FindByID(item_id, -1, Player.Bank.Serial)
    if item:
        Items.Move(item, Player.Backpack.Serial, amount)
        Misc.Pause(500)
        
def LogToBoard(axe_serial):
    
    for log_color in log_colors.keys():
        item = Items.FindByID(log_id, log_color, Player.Backpack.Serial)
        if item:
            Target.Cancel()
            Misc.Pause(50)
            Misc.SendMessage(log_id)
            Items.UseItem(axe_serial)
            Target.WaitForTarget(1000, False)
            Target.TargetExecute(item)
            Misc.Pause(500)
        
Player.ChatSay(12, "bank")
while True:
    LogToBoard(axe_serial)
    PutItemToBank(board_id, 0)
    GetItemFromBank(log_id, 200)