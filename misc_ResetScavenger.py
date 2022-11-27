
pos = Player.Position
while not Player.IsGhost:
    if pos != Player.Position:
        Scavenger.Stop()
        Scavenger.Start()
        pos = Player.Position
    Misc.Pause(1000)