Misc.SendMessage("MOBILE?")
target = Target.PromptTarget()

mobile = Mobiles.FindBySerial(target)


def goToLocation(x, y):
    route = PathFinding.Route()
    route.X = x
    route.Y = y
    route.MaxRetry = -1
    PathFinding.Go(route)


while True:
    goToLocation(mobile.Position.X, mobile.Position.Y)
    Misc.Pause(100)