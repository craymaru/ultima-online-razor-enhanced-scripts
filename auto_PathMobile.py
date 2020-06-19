from System.Collections.Generic import List 

targets = [
    0x0024, # Lizardman
    0x00F2, # Deathwatch beetle hatchling
    0x00F0, # Kappa
]

def goPos(x, y):
    route = PathFinding.Route()
    route.X = x
    route.Y = y
    route.MaxRetry = 10
    PathFinding.Go(route)
    Misc.Pause(50)

    
def findCorpses():
    corpseFilter = Items.Filter()
    corpseFilter.Enabled = True
    corpseFilter.OnGround = True
    corpseFilter.Movable = False
    corpseFilter.RangeMax = 3
    corpseFilter.IsCorpse = True
    corpses = Items.ApplyFilter(corpseFilter)
    return corpses

    
def findEnemy():
    enemyFilter = Mobiles.Filter()
    enemyFilter.Enabled = True
    enemyFilter.Bodies = List[int]([0x00F2,0x0024])
    enemyFilter.RangeMax = 30
    enemies = Mobiles.ApplyFilter(enemyFilter)
    enemy = Mobiles.Select(enemies, "Nearest")
    return enemy
  

def loot():
    global looted
    looted = []
    corpses = findCorpses()
    
    for corpse in corpses:
        if corpse and not corpse.Serial in looted:
            looted.append(corpse.Serial)
            Player.HeadMessage(33, "LootTime!")
            Player.HeadMessage(33, str(looted))
            Misc.Pause(3000)

            
def resetPosition(x, y, duration):
    enemyFilter = Mobiles.Filter()
    enemyFilter.Enabled = True
    enemyFilter.Bodies = List[int]([0x00F2,0x0024])
    enemyFilter.RangeMax = 10
    enemies = Mobiles.ApplyFilter(enemyFilter)
    
    Player.HeadMessage(54, len(enemies))
    
    if not Timer.Check("ResetPos") and len(enemies) is 0:
        Player.HeadMessage(80, "ResetPos!")
        goPos(x, y)
        Timer.Create("ResetPos", duration)
    
        
        
while True:
    
    resetPosition(948, 434, 1000 * 60)
    
    enemy = findEnemy()
    if enemy:
        goPos(enemy.Position.X, enemy.Position.Y)
    
    # loot()
        
    Misc.Pause(1000)
    
