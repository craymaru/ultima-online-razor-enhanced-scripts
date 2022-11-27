from System.Collections.Generic import List


def get_target_item(msg):
    Player.HeadMessage(55, msg)
    target = Target.PromptTarget()

    item = Items.FindBySerial(target)
    return item

def get_items(item):
    filter = Items.Filter()
    filter.OnGround = False
    filter.Movable = True
    filter.Graphics = List[int]([item.ItemID])
    filter.Hues = List[int]([item.Hue])
    
    items = Items.ApplyFilter(filter)
    items = [x for x in items if x.Container == item.Container]
    items = sorted(items, reverse=True, key=lambda item: item.Amount)
    return items

    
item = get_target_item("item?")
container = get_target_item("container?")

while True:
    items = get_items(item)
    length = len(items)
    
    
    missing = 60000 - items[0].Amount
    
    if missing == 0:
        for i in range(length):
            if items[i].Amount == 60000: 
                Items.Move(items[i], container, -1)
                Misc.Pause(750)
            else: break
                
        Misc.Pause(1000)
        continue
    
    if not any([item.Amount < 60000 for item in items]): break
    
    if missing <= items[1].Amount:
        Items.Move(items[1], items[0], missing)
        Misc.Pause(1000)
        Items.Move(items[0], container, -1)
    else:
        Items.Move(items[1], items[0], -1)
    
    Misc.Pause(1500)
