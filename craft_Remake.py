amount = 200

for i in range(amount):
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 21)
    Player.HeadMessage(6, str(i+1) + "/" + str(amount))