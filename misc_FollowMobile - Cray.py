Misc.SendMessage("FOLLOW TO CRAY")
target = 0x00020008

mobile = Mobiles.FindBySerial(target)


def goToLocation(x, y):
    Misc.SendMessage(mobile.Position.X)
    Misc.SendMessage(Player.Position.X)
    Misc.SendMessage(mobile.Position.Y)
    Misc.SendMessage(Player.Position.Y)
    if mobile.Position.X != Player.Position.X or mobile.Position.Y != Player.Position.Y:
        route = PathFinding.Route()
        route.X = x
        route.Y = y
        route.MaxRetry = -1
        PathFinding.Go(route)


while True:
    goToLocation(mobile.Position.X, mobile.Position.Y)
    Misc.Pause(100)