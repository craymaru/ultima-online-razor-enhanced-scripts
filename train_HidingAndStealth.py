

# directions = ["East", "Down", "South", "Left", "West", "Up", "North", "Right"]
directions = ["South", "North"]

def hiding():
    if not Timer.Check("Hiding"):
        Player.UseSkill("Hiding")
        Timer.Create("Hiding", 10000)
        
        
while True:
    for direction in directions:
        hiding()
        for i in range(6):
            Player.Walk(direction)
