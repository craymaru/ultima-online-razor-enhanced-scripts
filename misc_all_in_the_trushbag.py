
corpse = Target.PromptTarget()
Misc.SendMessage(corpse)
trash_bag = Items.FindByID(0x09B0, 0x09c4, Player.Backpack.Serial)
Misc.SendMessage(trash_bag)
items = Items.FindByID(-1, -1, corpse)
Misc.SendMessage(items)

for item in items:
    Items.Move(item, trash_bag, 0)
    Misc.Pause(300)
