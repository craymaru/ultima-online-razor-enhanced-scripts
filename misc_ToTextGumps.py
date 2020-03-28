gump_id = Gumps.CurrentGump()
Misc.SendMessage(gump_id)

gump_len = len(Gumps.LastGumpGetLineList())
Misc.SendMessage(gump_len)

for line in range(gump_len):
    if Gumps.LastGumpTextExistByLine(line, "%"):
        msg = Gumps.LastGumpGetLine(line)
        Misc.SendMessage(msg)