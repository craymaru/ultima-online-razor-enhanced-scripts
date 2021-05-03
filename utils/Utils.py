def getCRDelayOfMagery(fastCastRecovery: int):
    cr = fastCastRecovery - 1
    return 1500 - (cr * 250)


class RE():
    def __init__(self, Items, Misc):
        self.Items = Items
        self.Misc = Misc

    def moveItems(self, items, container, amount=0):
        if items:
            for item in items:
                self.Items.Move(item, container, 0)
                self.Misc.Pause(550)
