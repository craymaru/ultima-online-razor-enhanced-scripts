x = 45
y = 65
container = Items.FindBySerial(Target.PromptTarget('Choose Source'))
itemID = Items.FindBySerial(Target.PromptTarget('Choose type')).ItemID
dest = Target.PromptTarget('Chose Destination') 
for items in container.Contains:
    if items.ItemID == itemID:
        Items.Move(items,dest,1,x,y)
        x +=3
        if x > 140:
            x = 45
            y += 20
            Misc.Pause(650)