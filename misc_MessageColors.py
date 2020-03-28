while True:
    for color in range(1910,1920):
        Misc.SendMessage("Color" + str(color), color)
        Misc.Pause(10)