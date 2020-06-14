
# IDS
skillet_id = 0x097F
bark_fragment_id = 0x318F
raw_fish_steak_id = 0x097A
wood_pulp_id = 0x103D

# SERIALS
container_serial = 0x400795DD


def get_item(item_id, container_serial, low_amount, get_amount):
    current_amount = Items.BackpackCount(item_id)
    if current_amount <= low_amount:
        item = Items.FindByID(item_id, -1, container_serial)
        if item:
            Items.Move(item, Player.Backpack.Serial, get_amount - current_amount)
            Misc.Pause(700)


def put_item(item_id, container_serial, high_amount, put_amount):
    current_amount = Items.BackpackCount(item_id)
    if high_amount <= current_amount:
        item = Items.FindByID(item_id, -1, Player.Backpack.Serial)
        if item:
            Items.Move(item, container_serial, put_amount)
            Misc.Pause(700)


def remake():
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 21)
    Misc.Pause(1500)


def use(item_id, item_color=-1):
    item = Items.FindByID(item_id, item_color, Player.Backpack.Serial)
    if item:
        Items.UseItem(item)
        Misc.Pause(200)
        remake()
    else:
        end()
        
while True:
    # get_item(raw_fish_steak["id"], container_serial, 1)
    
    put_item(wood_pulp_id, Player.Bank.Serial, 100, -1)
    get_item(bark_fragment_id, Player.Bank.Serial, 10, 100)
    use(skillet_id)
