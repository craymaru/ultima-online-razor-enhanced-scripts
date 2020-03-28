runic_atlas = 0x405FCFCC

runes = range(0, 44)


def RecallToAtlas(rune):
    # USE ATLAS
    Items.UseItem(runic_atlas)
    
    # PAGENATE
    page = rune / 16
    Misc.SendMessage("Page: %s" % page)
    for i in range(page):
        Gumps.WaitForGump(498, 10000)
        Gumps.SendAction(498, 1150)
    
    # SELECT RUNE
    Misc.SendMessage("Rune: %s" % rune)
    rune_button = rune + 100
    Gumps.WaitForGump(498, 10000)
    Gumps.SendAction(498, rune_button)
    
    # RECALL
    Gumps.WaitForGump(498, 10000)
    Gumps.SendAction(498, 4)
    
    Misc.Pause(5000)



for rune in runes:
    RecallToAtlas(rune)