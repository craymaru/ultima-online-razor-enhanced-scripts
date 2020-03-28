bulk_order_book_serial = 0x400D8CC6

item_id_list = {
    0x2258: "bulk_order_deed" 
}


def MoveItems(item_id_list, moved_serial, amount):
    for item_id in item_id_list:
        while Items.FindByID(item_id, -1, Player.Backpack.Serial):
            item = Items.FindByID(item_id, -1, Player.Backpack.Serial)
            if item:
                Items.Move(item, moved_serial, amount)
                Misc.Pause(650)


MoveItems(item_id_list, bulk_order_book_serial, 0)