while Items.FindByID(0x1012, -1, Player.Backpack.Serial):
    item = Items.FindByID(0x1012, -1, Player.Backpack.Serial)
    Misc.SendMessage(item)
    x = Player.Position.X + 0
    y = Player.Position.Y + 1
    z = Player.Position.Z
    Items.MoveOnGround(item,0, x, y, z)
    Misc.Pause(800)