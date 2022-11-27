def moveAllItems(id, color, dest, source=None, *, Items, Player, Misc):
    """
    Move all items

    Example:
        RE = { "Misc": Misc, "Player": Player, "Items": Items }
        moveAllItems(id, color, dest, **RE)
    """

    if source is None:
        source = Player.Backpack.Serial

    while True:
        item = Items.FindByID(id, color, source)
        if not item:
            break
        Items.Move(item, dest, 0)
        Misc.Pause(600)
