from System.Collections.Generic import List


ham_filter = Items.Filter()
ham_filter.Enabled
ham_filter.Graphics = List[int]([0x09C9])
ham_filter.RangeMax = 2
ham_filter.OnGround = True
ham_filter.Movable = True

while True:
    hams = Items.ApplyFilter(ham_filter)
    ham = Items.Select(hams, "Nearest")
    if ham:
        Items.Move(ham, 0x4012280D, 0)
        Misc.Pause(550)