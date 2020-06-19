
#By Mourn#8182 discord contact


############### GUI INTERFACE FOR DEXXER OR SAMP
# please DM me with ideas 


minDurability = 20  ##### durability check amount for repair


from time import sleep
from datetime import datetime
import clr, time, thread, sys, System

clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Data')
clr.AddReference('IronPython')
from System.Threading import ThreadStart, Thread
from System.Collections.Generic import List
from System import Byte
from System.Drawing import Point, Color, Size
from System.Windows.Forms import (Application, Button, Form, BorderStyle, Label, FlatStyle, DataGridView,
 DataGridViewAutoSizeColumnsMode, DataGridViewSelectionMode, DataGridViewEditMode, RadioButton, GroupBox,
 TextBox, CheckBox, ProgressBar)
from System.Data import DataTable
from IronPython.Compiler import CallTarget0
import sys
#sys.path.append(r'C:\Program Files (x86)\IronPython.StdLib.2.7.9')  # D/L and adjust path for your library sorry 
sys.path.append(r'C:\Program Files\IronPython 2.7\Lib')  # D/L and adjust path for your library sorry 
import os

contents = []
Misc.SetSharedValue('run','False')
list= []
railcoords = []
moblist = [0x9999]
layers = ["RightHand","LeftHand","Shoes","Pants","Shirt","Head","Gloves","Ring","Neck","Waist",
"InnerTorso","Bracelet","MiddleTorso","Arms","Cloak","OuterTorso","OuterLegs","InnerLegs","Talisman"]
Misc.SetSharedValue('homeX','False')
Misc.SetSharedValue('homeY','False')
Misc.SetSharedValue('mobID','False')
BFilter = Items.Filter()
BFilter.RangeMax = 3
BFilter.OnGround = True
BFilter.Enabled = True
BFilter.Movable = True
BFilter.Graphics = List[int]((0xA278, 0xA27F))
global wep

############################## rail recorder form  ##############################

class SimpleTextBoxForm(Form):    
    list = []
    def __init__(self):
        self.Text = "Fast Rails"
        self.Width = 250
        self.Height = 225
        self.TopMost = True
       
        self.button = Button()
        self.button.Text = 'Add Coord'
        self.button.Width = 100
        self.button.Height = 40
        self.button.Location = Point(10, 10)
        self.button.Click += self.add
        
        self.button1 = Button()
        self.button1.Text = 'Del last Coord'
        self.button1.Width = 100
        self.button1.Height = 40
        self.button1.Location = Point(125, 10)
        self.button1.Click += self.delLast

        self.button2 = Button()
        self.button2.Text = 'Clear All'
        self.button2.Width = 100
        self.button2.Height = 40
        self.button2.Location = Point(125, 50)
        self.button2.Click += self.clear
        
        self.button3 = Button()
        self.button3.Text = 'Test Rail'
        self.button3.Width = 100
        self.button3.Height = 40
        self.button3.Location = Point(10, 50)
        self.button3.Click += self.test
        
        self.button4 = Button()
        self.button4.Text = 'INFO'
        self.button4.Width = 100
        self.button4.Height = 40
        self.button4.Location = Point(10, 90)
        self.button4.Click += self.info
        
        self.button5 = Button()
        self.button5.Text = 'SAVE'
        self.button5.Width = 75
        self.button5.Height = 30
        self.button5.Location = Point(135, 135)
        self.button5.BackColor = Color.FromArgb(10,225,10)
        self.button5.Click += self.makefile
        
        self.textbox = TextBox()
        self.textbox.Text = "Rail_Name"
        self.textbox.Location = Point(10, 140)
        self.textbox.Width = 115

        
        self.Controls.Add(self.button)
        self.Controls.Add(self.button1)
        self.Controls.Add(self.button2)
        self.Controls.Add(self.button3)
        self.Controls.Add(self.button4)
        self.Controls.Add(self.button5)
        self.Controls.Add(self.textbox)
        
    def add(self, sender, event):
        list.append([(Player.Position.X),(Player.Position.Y)])
        
        Misc.SendMessage('{} Total Coords'.format(len(list)))
        
           
    def test(self, sender, event):
        if len(list) > 0:
            for l in list:
                go(l[0],l[1])
        else:
            Misc.SendMessage('You didnt set any Coords!',33)
            
    def delLast(self, sender, event):
        if len(list) > 0:
            del list[-1]
            Misc.SendMessage('{} Total Coords'.format(len(list)))
        else:
            Misc.SendMessage('The Coord list is Empty!',33)
            
    def clear(self, sender, event):
        list.Clear()
        Misc.SendMessage('Coord list Cleared',180)
        
    def info(self, sender, event):
        if len(list) > 0:
            Misc.SendMessage('{} Total Coords'.format(len(list)),75)
            Misc.SendMessage('Last Coords were {}'.format(list[-1]),180)
            Misc.SendMessage('Current Coords are {}'.format(str(Player.Position.X)) + ',' + (str(Player.Position.Y)),285)
        else:
            Misc.SendMessage('You didnt set any Coords!',33)
            Misc.SendMessage('Current Coords are {}'.format(str(Player.Position.X)) + ',' + (str(Player.Position.Y)),285)
            
    def makefile(self, sender, event):
        rail_file = os.path.join(os.environ.get('userprofile', 'c:'), 'Documents', '{}.txt'.format(self.textbox.Text))

        if not os.path.exists(rail_file):
            file = open(rail_file, 'w+')
            file.write(str(list))
            file.close()
        else:
            Misc.SendMessage('Saved {}.txt in Documents'.format(self.textbox.Text),30)
            file = open(rail_file, 'w+')
            file.write(str(list))
            file.close()
            
            ################################# repair checker ########################################

class DurabilityChecker(object):    
    def hasDurability(self, item):
        Items.WaitForProps(item, 1000)
        
        for prop in Items.GetPropStringList(item):
            if prop.find("durability") >= 0:
                return True
                
        return False

    def getDurability(self, item):
        Items.WaitForProps(item, 1000)
        return Items.GetPropValue(item, "durability")
        
    def repairshit(self,item):
        benchlist = Items.ApplyFilter(BFilter)
        Misc.Pause(200)
        bench = Items.Select(benchlist,'Nearest')                                  
        Items.UseItem(bench)            
        Gumps.WaitForGump(9237, 10000)
        Gumps.SendAction(9237, 2002)
        Target.WaitForTarget(10000, False)
        Misc.Pause(1000)
        Target.TargetExecute(item)
        Gumps.WaitForGump(9237, 10000)
        Gumps.SendAction(9237, 2001)
        Target.WaitForTarget(10000, False)  # maybe something missing like stone i dunno
        Target.TargetExecute(item)          # mult deeds is easier than figuring out what deed to use
        Gumps.WaitForGump(9237, 10000)
        Gumps.SendAction(9237, 2003)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(item)
        Gumps.WaitForGump(9237, 10000)
        Gumps.SendAction(9237, 2006)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(item)
        Misc.Pause(2000) 
            
    def Main(self):
        
        Misc.Pause(3000)                
        for layer in layers:
            item = Player.GetItemOnLayer(layer)
            
            if not item:
                continue
                
            if not self.hasDurability(item):
                continue
                
            durability = self.getDurability(item)    
                
            if durability < minDurability:
                Misc.SendMessage(layer, 38)
                Misc.SendMessage(item,38)
                broken = item.Serial
                Misc.SendMessage(broken,38)
                Misc.Pause(1000)
                benches = Items.ApplyFilter(BFilter)
                if len(benches) > 0:
                    bench = Items.Select(benches,'Nearest')
                    if bench:
                        self.repairshit(broken)
                
        Misc.SendMessage('Check Complete',87)    
                    
######################################  main form ###############################################  
                                    
class dexxer(Form):
    CurVer = '1.6'
    ScriptName = 'Mourns Dexxer Assistant'
    
    
    def __init__(self, contents):
        self.Contents = contents       
        self.BackColor = Color.FromArgb(25,25,25)
        self.ForeColor = Color.FromArgb(231,231,231)
        self.Size = Size(200, 605)
        self.Text = '{0} - v{1}'.format(self.ScriptName, self.CurVer)
        self.TopMost = True
        
        self.box = GroupBox()
        self.box.BackColor = Color.FromArgb(25,25,25)
        self.box.ForeColor = Color.FromArgb(23,221,23)
        self.box.Size = Size(180, 140)
        self.box.Location = Point(2, 57)
        self.box.Text = 'Options'
        
        self.box2 = GroupBox()
        self.box2.BackColor = Color.FromArgb(25,25,25)
        self.box2.ForeColor = Color.FromArgb(23,221,23)
        self.box2.Size = Size(180, 50)
        self.box2.Location = Point(02, 400)
        self.box2.Text = 'Chase Mobile Options'
        
        self.box3 = GroupBox()
        self.box3.BackColor = Color.FromArgb(25,25,25)
        self.box3.ForeColor = Color.FromArgb(23,221,23)
        self.box3.Size = Size(180, 155)
        self.box3.Location = Point(02, 244)
        self.box3.Text = 'Dress/Arm'
        
        self.box4 = GroupBox()
        self.box4.BackColor = Color.FromArgb(25,25,25)
        self.box4.ForeColor = Color.FromArgb(23,221,23)
        self.box4.Size = Size(180, 60)
        self.box4.Location = Point(02, 505)
        
        self.box5 = GroupBox()
        self.box5.BackColor = Color.FromArgb(25,25,25)
        self.box5.ForeColor = Color.FromArgb(23,221,23)
        self.box5.Size = Size(180, 40)
        self.box5.Location = Point(02, 200)
        self.box5.Text = 'Weapon Type'
        
        self.box6 = GroupBox()
        self.box6.BackColor = Color.FromArgb(25,25,25)
        self.box6.ForeColor = Color.FromArgb(23,221,23)
        self.box6.Size = Size(180, 55)
        self.box6.Location = Point(2, 2)
        self.box6.Text = Player.Name
        
        self.box7 = GroupBox()
        self.box7.BackColor = Color.FromArgb(25,25,25)
        self.box7.ForeColor = Color.FromArgb(23,221,23)
        self.box7.Size = Size(180, 55)
        self.box7.Location = Point(02, 450)
        self.box7.Text = 'Rail Options'
        
        self.cbA = CheckBox()
        self.cbA.Text = 'Conf/Evade'
        self.cbA.Checked = False
        self.cbA.BackColor = Color.FromArgb(25,25,25)
        self.cbA.Location = Point(10, 70)
        self.cbA.Size = Size(85, 20)
        
        hb = ProgressBar()
        hb.Minimum = 1
        hb.Maximum = 100
        hb.Step = 1
        hb.Value = 1
        hb.Location = Point(10, 20)
        hb.Width = 165
        hb.Height = 25
        hb.BackColor = Color.FromArgb(5,255,25)
        hb.ForeColor = Color.FromArgb(233,221,23)        
        self.prog = hb 
                
        self.cbB = CheckBox()
        self.cbB.Text = 'EoO'
        self.cbB.Checked = False
        self.cbB.BackColor = Color.FromArgb(25,25,25)
        self.cbB.Location = Point(95, 70)
        self.cbB.Size = Size(85, 20)
        
        self.cbC = CheckBox()
        self.cbC.Text = 'Band Heal'
        self.cbC.Checked = False
        self.cbC.BackColor = Color.FromArgb(25,25,25)
        self.cbC.Location = Point(10, 90)
        self.cbC.Size = Size(85, 20)
        
        self.cbD = CheckBox()
        self.cbD.Text = 'Cons Wep'
        self.cbD.Checked = False
        self.cbD.BackColor = Color.FromArgb(25,25,25)
        self.cbD.Location = Point(95, 90)
        self.cbD.Size = Size(85, 20)
        
        self.cbE = CheckBox()
        self.cbE.Text = 'Honor'
        self.cbE.Checked = False
        self.cbE.BackColor = Color.FromArgb(25,25,25)
        self.cbE.Location = Point(10, 110)
        self.cbE.Size = Size(85, 20)
        
        self.cbF = CheckBox()
        self.cbF.Text = 'Div Fury'
        self.cbF.Checked = False
        self.cbF.BackColor = Color.FromArgb(25,25,25)
        self.cbF.Location = Point(95, 110)
        self.cbF.Size = Size(85, 20)
        
        self.cbG = CheckBox()
        self.cbG.Text = 'Onslaught'
        self.cbG.Checked = False
        self.cbG.BackColor = Color.FromArgb(25,25,25)
        self.cbG.Location = Point(10, 130)
        self.cbG.Size = Size(85, 20)
        
        self.cbH = CheckBox()
        self.cbH.Text = 'Cntr Atk'
        self.cbH.Checked = False
        self.cbH.BackColor = Color.FromArgb(25,25,25)
        self.cbH.Location = Point(95, 130)
        self.cbH.Size = Size(85, 20)
        
        self.cbI = CheckBox()
        self.cbI.Text = 'OJ Petal'
        self.cbI.Checked = False
        self.cbI.BackColor = Color.FromArgb(25,25,25)
        self.cbI.Location = Point(10, 150)
        self.cbI.Size = Size(85, 20)
        
        self.cbJ = CheckBox()
        self.cbJ.Text = 'Insure'
        self.cbJ.Checked = False
        self.cbJ.BackColor = Color.FromArgb(25,25,25)
        self.cbJ.Location = Point(95, 150)
        self.cbJ.Size = Size(85, 20)
        
        self.cbK = CheckBox()
        self.cbK.Text = 'Apple'
        self.cbK.Checked = False
        self.cbK.BackColor = Color.FromArgb(25,25,25)
        self.cbK.Location = Point(10, 170)
        self.cbK.Size = Size(85, 20)
        
        self.cbL = CheckBox()
        self.cbL.Text = 'On/Off'
        self.cbL.Checked = False
        self.cbL.BackColor = Color.FromArgb(25,25,25)
        self.cbL.Location = Point(10, 415)
        self.cbL.Size = Size(60, 20)
        
        self.cbM = CheckBox()
        self.cbM.Text = 'On/Off'
        self.cbM.Checked = False
        self.cbM.BackColor = Color.FromArgb(25,25,25)
        self.cbM.Location = Point(10, 463)
        self.cbM.Size = Size(60, 20)
        
        self.cbN = CheckBox()
        self.cbN.Text = 'Bone Cutter'
        self.cbN.Checked = False
        self.cbN.BackColor = Color.FromArgb(25,25,25)
        self.cbN.Location = Point(95, 170)
        self.cbN.Size = Size(85, 20)
        
        self.rbD = RadioButton()
        self.rbD.Text = 'D Axe'
        self.rbD.Location = Point(25, 213)
        self.rbD.BackColor = Color.FromArgb(25,25,25)
        self.rbD.ForeColor = Color.FromArgb(231,231,231)
        self.rbD.Size = Size(65, 20)
        
        self.rbE = RadioButton()
        self.rbE.Text = 'B Staff'
        self.rbE.Location = Point(105,213)
        self.rbE.BackColor = Color.FromArgb(25,25,25)
        self.rbE.ForeColor = Color.FromArgb(231,231,231)
        self.rbE.Size = Size(65, 20)
        
        self.btnA = Button()
        self.btnA.Text = 'Demon'
        self.btnA.BackColor = Color.FromArgb(50,24,25)
        self.btnA.Location = Point(10, 342)
        self.btnA.Size = Size(55, 25)
        self.btnA.FlatStyle = FlatStyle.Flat
        self.btnA.FlatAppearance.BorderSize = 1
        self.btnA.Click += self.btnDemonPressed
        
        self.btnB = Button()
        self.btnB.Text = 'Reptile'
        self.btnB.BackColor = Color.FromArgb(25,50,25)
        self.btnB.Location = Point(65, 342)
        self.btnB.Size = Size(55, 25)
        self.btnB.FlatStyle = FlatStyle.Flat
        self.btnB.FlatAppearance.BorderSize = 1 
        self.btnB.Click += self.btnReptilePressed
        
        self.btnC = Button()
        self.btnC.Text = 'Undead'
        self.btnC.BackColor = Color.FromArgb(50,25,25)
        self.btnC.Location = Point(120, 342)
        self.btnC.Size = Size(55, 25)
        self.btnC.FlatStyle = FlatStyle.Flat
        self.btnC.FlatAppearance.BorderSize = 1 
        self.btnC.Click += self.btnUndeadPressed
        
        self.btnD = Button()
        self.btnD.Text = 'Elemen'
        self.btnD.BackColor = Color.FromArgb(25,50,25)
        self.btnD.Location = Point(10, 317)
        self.btnD.Size = Size(55, 25)
        self.btnD.FlatStyle = FlatStyle.Flat
        self.btnD.FlatAppearance.BorderSize = 1 
        self.btnD.Click += self.btnElemenPressed
        
        self.btnE = Button()
        self.btnE.Text = 'Arach'
        self.btnE.BackColor = Color.FromArgb(50,25,25)
        self.btnE.Location = Point(65, 317)
        self.btnE.Size = Size(55, 25)
        self.btnE.FlatStyle = FlatStyle.Flat
        self.btnE.FlatAppearance.BorderSize = 1 
        self.btnE.Click += self.btnArachPressed
        
        self.btnF = Button()
        self.btnF.Text = 'Repond'
        self.btnF.BackColor = Color.FromArgb(25,50,25)
        self.btnF.Location = Point(120, 317)
        self.btnF.Size = Size(55, 25)
        self.btnF.FlatStyle = FlatStyle.Flat
        self.btnF.FlatAppearance.BorderSize = 1 
        self.btnF.Click += self.btnRepondPressed
        
        self.btnG = Button()
        self.btnG.Text = 'Main Dress'
        self.btnG.BackColor = Color.FromArgb(25,50,25)
        self.btnG.Location = Point(10, 260)
        self.btnG.Size = Size(165, 25)
        self.btnG.FlatStyle = FlatStyle.Flat
        self.btnG.FlatAppearance.BorderSize = 1 
        self.btnG.Click += self.btnDressPressed
        
        self.btnH = Button()
        self.btnH.Text = 'Luck Suit'
        self.btnH.BackColor = Color.FromArgb(50,50,10)
        self.btnH.Location = Point(10, 285)
        self.btnH.Size = Size(165, 25)
        self.btnH.FlatStyle = FlatStyle.Flat
        self.btnH.FlatAppearance.BorderSize = 1 
        self.btnH.Click += self.btnLuckPressed
        
        self.btnI = Button()
        self.btnI.Text = 'Repair Check'
        self.btnI.BackColor = Color.FromArgb(10,10,60)
        self.btnI.Location = Point(10, 367)
        self.btnI.Size = Size(165, 25)
        self.btnI.FlatStyle = FlatStyle.Flat
        self.btnI.FlatAppearance.BorderSize = 1 
        self.btnI.Click += self.btnRepairPressed
        
        self.btnJ = Button()
        self.btnJ.Text = 'Chase by MobID'
        self.btnJ.BackColor = Color.FromArgb(0,0,0)
        self.btnJ.Location = Point(75, 415)
        self.btnJ.Size = Size(100, 30)
        self.btnJ.FlatStyle = FlatStyle.Flat
        self.btnJ.FlatAppearance.BorderSize = 1 
        self.btnJ.Click += self.btnMobIDPressed
        
        self.btnGet = Button()
        self.btnGet.Text = 'Stop'
        self.btnGet.BackColor = Color.FromArgb(100,10,10)
        self.btnGet.Location = Point(95, 520)
        self.btnGet.Size = Size(80, 35)
        self.btnGet.FlatStyle = FlatStyle.Flat
        self.btnGet.FlatAppearance.BorderSize = 1
        self.btnGet.Click += self.btnStopPressed
        
        self.startGet = Button()
        self.startGet.Text = 'Start'
        self.startGet.BackColor = Color.FromArgb(10,100,10)
        self.startGet.Location = Point(10, 520)
        self.startGet.Size = Size(80, 35)
        self.startGet.FlatStyle = FlatStyle.Flat
        self.startGet.FlatAppearance.BorderSize = 1
        self.startGet.Click += self.btnStartPressed
                
        self.button4 = Button()
        self.button4.Text = 'Open Recorder'
        self.button4.Width = 100
        self.button4.Height = 30
        self.button4.Location = Point(75,465)
        self.button4.FlatStyle = FlatStyle.Flat
        self.button4.Click += self.info

        self.textbox2 = TextBox()
        self.textbox2.Text = "Rail_Name"
        self.textbox2.Location = Point(10,480 )
        self.textbox2.Width = 60
        
        self.Controls.Add(self.textbox2)
        self.Controls.Add(self.button4)
        self.Controls.Add(self.cbA)
        self.Controls.Add(self.cbB)
        self.Controls.Add(self.cbC)
        self.Controls.Add(self.cbD)
        self.Controls.Add(self.cbE)
        self.Controls.Add(self.cbF)
        self.Controls.Add(self.cbG)
        self.Controls.Add(self.cbH)
        self.Controls.Add(self.cbI)
        self.Controls.Add(self.cbJ)
        self.Controls.Add(self.cbK)
        self.Controls.Add(self.cbL)
        self.Controls.Add(self.cbM)
        self.Controls.Add(self.cbN)
        
        self.Controls.Add(self.btnA)
        self.Controls.Add(self.btnB)
        self.Controls.Add(self.btnC)
        self.Controls.Add(self.btnD)
        self.Controls.Add(self.btnE)
        self.Controls.Add(self.btnF)
        self.Controls.Add(self.btnG)
        self.Controls.Add(self.btnH)
        self.Controls.Add(self.btnI)
        self.Controls.Add(self.btnJ)
        self.Controls.Add(self.btnGet)
        self.Controls.Add(self.startGet)
        
        self.Controls.Add(self.rbD)   
        self.Controls.Add(self.rbE)
        
        self.Controls.Add(hb)
        
        self.Controls.Add(self.box)
        self.Controls.Add(self.box2)
        self.Controls.Add(self.box3)
        self.Controls.Add(self.box4)
        self.Controls.Add(self.box5)
        self.Controls.Add(self.box6)
        self.Controls.Add(self.box7)

        Misc.Pause(500)
        self.Shown += self.refresh
        
    def btnStartPressed(self, sender, args):
        Misc.SetSharedValue('run','True')       
        Misc.SetSharedValue('bush','False')
        Misc.SetSharedValue('eoo','False')
        Misc.SetSharedValue('consec','False')
        Misc.SetSharedValue('honor','False')
        Misc.SetSharedValue('devFury','False')
        Misc.SetSharedValue('onslaught','False')
        Misc.SetSharedValue('cAttack','False')
        Misc.SetSharedValue('ojPetal','False')
        Misc.SetSharedValue('apple','False')
        Misc.SetSharedValue('chase','False')
        Misc.SetSharedValue('insure','False')
        Misc.SetSharedValue('dAxe','False')
        Misc.SetSharedValue('bStaff','False')
        Misc.SetSharedValue('rail','False')
        Misc.SetSharedValue('bonecutter','False')
        Misc.SendMessage('Starting',80)
        
        def attack():
            while Misc.ReadSharedValue('run') == 'True':
                eNumber = 0
                fil = Mobiles.Filter()
                fil.Enabled = True
                fil.RangeMax = 1
                fil.Notorieties = List[Byte](bytes([3,4,5,6]))
                if Misc.ReadSharedValue('dAxe') == 'True':
                    enemies = Mobiles.ApplyFilter(fil)
                    Mobiles.Select(enemies,'Nearest')
                    for enemy in enemies:
                        eNumber += 1
                    if eNumber == 1:
                        eNumber = 0
                        if not Player.HasSpecial:
                            Player.WeaponPrimarySA()
                        Player.Attack(enemy)
                    if eNumber == 2:
                        eNumber = 0
                        if not Player.SpellIsEnabled('Momentum Strike'):
                            Spells.CastBushido('Momentum Strike')
                        Player.Attack(enemy) 
                    if eNumber > 2 :
                        eNumber = 0
                        if not Player.HasSpecial:
                            Player.WeaponSecondarySA()
                        Player.Attack(enemy)
                    Misc.Pause(250) 
                if Misc.ReadSharedValue('bStaff') == 'True':
                    enemies = Mobiles.ApplyFilter(fil)
                    Mobiles.Select(enemies,'Nearest')
                    for enemy in enemies:
                        eNumber += 1
                    if eNumber == 1:
                        eNumber = 0
                        if not Player.HasSpecial:
                            Player.WeaponPrimarySA()
                        Player.Attack(enemy)
                    if eNumber >= 2:
                        eNumber = 0
                        if not Player.SpellIsEnabled('Momentum Strike'):
                            Spells.CastBushido('Momentum Strike')
                        Player.Attack(enemy)
                Misc.Pause(500)
                
        def cast():
            while Misc.ReadSharedValue('run') == 'True':
                if Misc.ReadSharedValue('bush') == 'True':
                    bush()
                if Misc.ReadSharedValue('eoo') == 'True':
                    enemyOfOne()
                if Misc.ReadSharedValue('consec') == 'True':  
                    consecrateWep()
                if Misc.ReadSharedValue('honor') == 'True':
                    honorNearest()
                if Misc.ReadSharedValue('devFury') == 'True':
                    divineFury()
                if Misc.ReadSharedValue('onslaught') == 'True':
                    onslaughtMastery()
                if Misc.ReadSharedValue('cAttack') == 'True':
                    counterAttack()
                if Misc.ReadSharedValue('ojPetal') == 'True':
                    orangePetal()
                if Misc.ReadSharedValue('insure') == 'True':
                    list = []
                    for item in Player.Backpack.Contains:
                        list.append(item.Serial)
                        Misc.Pause(50)
                    insure()
                                
                Misc.Pause(500)
                
        def rail():
            self.ReadRail()
            while Misc.ReadSharedValue('chase') == 'True' and Misc.ReadSharedValue('rail') == 'False':
                chase()
                Misc.Pause(500)
                if Misc.ReadSharedValue('run') == 'False': 
                    break
            while Misc.ReadSharedValue('rail') == 'True': 
                
                for coords in railcoords:
                    go(coords[0],coords[1])
                    if Misc.ReadSharedValue('run') == 'False': 
                        break
                    if Misc.ReadSharedValue('chase') == 'True':
                        chase()                        
                Misc.Pause(500)
        
        def actions():
            while Misc.ReadSharedValue('run') == 'True':            
                if Misc.ReadSharedValue('apple') == 'True':
                    apple()
                if Misc.ReadSharedValue('bonecutter') == 'True': 
                    bonecutter(wep)
                Misc.Pause(1000)
                
        if self.cbC.Checked:
            Misc.Pause(300)  
            if BandageHeal.Status() == False:
                BandageHeal.Start()
        if self.cbA.Checked:
            Misc.Pause(300)
            Misc.SetSharedValue('bush','True')
        if self.cbB.Checked:
            Misc.Pause(300)
            Misc.SetSharedValue('eoo','True')       
        if self.cbD.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('consec','True')
        if self.cbE.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('honor','True')
        if self.cbF.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('devFury','True') 
        if self.cbG.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('onslaught','True')
        if self.cbH.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('cAttack','True')
        if self.cbI.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('ojPetal','True')            
        if self.cbJ.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('insure','True')
        if self.cbK.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('apple','True')
        if self.cbL.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('chase','True')
        if self.cbM.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('rail','True') 
        if self.cbN.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('bonecutter','True')
            Misc.SendMessage('Select Bone Cutter Wep',30)
            wep = Target.PromptTarget('')
            while Target.HasTarget():
                Misc.Pause(1000)
        if self.rbD.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('dAxe','True')
        if self.rbE.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('bStaff','True')
            
        c = Thread(ThreadStart(cast))
        c.Start()
        a = Thread(ThreadStart(attack))
        a.Start()
        r = Thread(ThreadStart(rail)) 
        r.Start()
        act = Thread(ThreadStart(actions))
        act.Start()
        
    def refresh (self,sender,event):
        def update():
            while True:
                Misc.Pause(1000)
                if Misc.ReadSharedValue('run') == 'True':
                    self.box2.Text = (str(Player.Position.X) + ", " + str(Player.Position.Y))
                    hits = ((Player.Hits + .0)/Player.HitsMax)* 100        
                    hit = int(hits)
                    if hit == 0:
                        hit = 1
                    def step():
                        count = 0
                        self.prog.Value = hit
                    self.Invoke(CallTarget0(step))                                        
                else:
                    self.prog.Value = 1
                    
        h = Thread(ThreadStart(update))
        h.Start()    
        
    def btnStopPressed(self, sender, args): 
        Misc.Pause(300)
        Misc.SendMessage('Stopping',45)
        Misc.SetSharedValue('run', 'False')
        self.box2.Text = "Chase Options:"
        Misc.SetSharedValue('rail', 'False')
        Misc.SetSharedValue('chase', 'False')
        
    def btnRepairPressed(self, sender, args):
        checker = DurabilityChecker()
        checker.Main()
    def btnMobIDPressed(self, sender, args):
        mobser = Target.PromptTarget('Select Mobile Type To Chase')
        mob = Mobiles.FindBySerial(mobser)
        moblist.append(mob.Body)
        Misc.SendMessage('Added {} type to Chase List'.format(mob.Name),48)
        
    def btnDemonPressed(self, sender, args):
        Dress.ChangeList('demon')
        Dress.DressFStart()
    def btnUndeadPressed(self, sender, args):
        Dress.ChangeList('undead')
        Dress.DressFStart()
    def btnReptilePressed(self, sender, args):
        Dress.ChangeList('reptile')
        Dress.DressFStart()
    def btnRepondPressed(self, sender, args):
        Dress.ChangeList('repond')
        Dress.DressFStart()
    def btnElemenPressed(self, sender, args):
        Dress.ChangeList('elemen')
        Dress.DressFStart()
    def btnArachPressed(self, sender, args):
        Dress.ChangeList('arach')
        Dress.DressFStart()
    def btnDressPressed(self, sender, args):
        Dress.ChangeList('dress')
        Dress.DressFStart()
    def btnLuckPressed(self, sender, args):
        Dress.ChangeList('luck')
        Dress.DressFStart()
                
    def info(self, sender, event):
        newform = SimpleTextBoxForm()  #run rail form
        Form.ShowDialog(newform)
        
    def ReadRail(self):
        railfile = os.path.join(os.environ.get('userprofile', 'c:'), 'Documents', '{}.txt'.format(self.textbox2.Text))
        with open(railfile) as file:
            rail = file.read()
            Misc.Pause(100)
            remove = ["[","]",","]
            for i in remove: 
                rail = rail.replace(i, '') 
            coords = rail.split(" ")
            x = 0
            y = 1
            while y <= len(coords):
                railcoords.append([int(coords[x]),int(coords[y])])
                x += 2
                y += 2      
def bush():
    healhits = 90
    evadehits = 100
    if Player.Hits < (healhits) and not Player.BuffsExist('Confidence'):
        Misc.Pause (400)
        Spells.CastBushido("Confidence")
        Misc.Pause (500)
        
    if Player.Hits < (evadehits) and not Player.BuffsExist('Evasion'):
        Misc.Pause (400)
        Spells.CastBushido("Evasion")
        Misc.Pause (500)
        
def enemyOfOne():
    if not Player.BuffsExist('Enemy Of One'):
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(500)
        
def consecrateWep():
    if not Player.BuffsExist('Consecrate Weapon'):
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(500)
        
def honorNearest():
    if not Player.BuffsExist('Honored'):
        honfil = Mobiles.Filter()
        honfil.Enabled = True
        honfil.RangeMax = 8
        honfil.Notorieties = List[Byte](bytes([3,4,5,6]))
        enemies = Mobiles.ApplyFilter(honfil)
        Misc.Pause(200)
        enemy = Mobiles.Select(enemies,'Nearest')
        if enemy:
            Player.InvokeVirtue("Honor")
            Target.WaitForTarget(1000, False)
            Target.TargetExecute(enemy.Serial)
        
def divineFury():
    if Player.Stam < Player.Stam - 20:   
        Spells.CastChivalry("Divine Fury")
        Misc.Pause(500)
        
def onslaughtMastery():
    if Timer.Check('mastery') == False:
        Spells.CastMastery('Onslaught')
        Timer.Create('mastery',10000)
    
def counterAttack():
    if not Player.BuffsExist('Counter Attack'):
        Spells.CastBushido('Counter Attack')
        Misc.Pause(500)
        
def orangePetal():
    ojpetals = Items.FindByID(0x1021,0x002B,Player.Backpack.Serial)
    if not ojpetals:
        if Timer.Check('oj') == False:
            Misc.SendMessage('No Orange Petals',33)
        Timer.Create('oj',10000)
        pass
    if Player.BuffsExist('Poison'):
        if not Player.BuffsExist('Orange Petals'):
            Items.UseItem(ojpetals.Serial)
            Misc.Pause(200)
def insure():
    for item in Player.Backpack.Contains:
        if item.Serial in list:
            pass
        else:
            Items.WaitForProps(item, 1000)
            list.append(item.Serial)
            if not (Items.GetPropValue(item, '<b>Insured</b>')):
                if not (Items.GetPropValue(item, 'Blessed')):
                    if not (Items.GetPropValue(item, 'Cursed')):
                        Target.Cancel()    
                        Misc.WaitForContext(Player.Serial, 3000)
                        Misc.ContextReply(Player.Serial, "Toggle Item Insurance")
                        Target.WaitForTarget(2000, True)
                        Target.TargetExecute(item)
                        Misc.Pause(600)    
                        Target.Cancel()
                       
def apple():
    apples = Items.FindByID(0x2FD8,-1,Player.Backpack.Serial)
    if not apples:
        if Timer.Check('apple') == False:
            Misc.SendMessage('No Apples',33)
        Timer.Create('apple',10000)
        pass
    if Player.BuffsExist('Blood Oath(curse)') or Player.BuffsExist('Mortal Strike') and Timer.Check('apple') == False:
        Items.UseItem(apples.Serial)
        Misc.Pause(400)
        Timer.Create("apple", 30500)
        
def bonecutter(wep):    
    namelist = ["bones (0ECE)","bones (0ECC)","bones (0ECB)","bones (0ECA)","bones (0ED0)","bones (0ECD)","bones (0ECF)"]
    grounditemfilter = Items.Filter()
    grounditemfilter.Enabled
    grounditemfilter.OnGround = True
    grounditemfilter.Movable = True
    grounditemfilter.Graphics = List[int]((0x0ECE,0x0ED0,0x0ECA,0x0ECD,0x0ECC,0x0ED0,0x0ECF,0x0ECB))
    grounditemfilter.RangeMax = 5   
    bones = Items.ApplyFilter(grounditemfilter)
    for bonepile in bones:
        Items.Message(bonepile,33,bonepile.Name)
        if bonepile.Name in namelist:
            Items.UseItem(wep)
            Target.WaitForTarget(500,False)
            Target.TargetExecute(bonepile)
            Misc.Pause(650) 
            break
            
def go(x1, y1):
    Coords = PathFinding.Route() 
    Coords.X = x1
    Coords.Y = y1
    Coords.MaxRetry = 5
    PathFinding.Go(Coords)
            
def chase():
    chaseables = []
    ignore = []
    cfil = Mobiles.Filter()
    cfil.Enabled = True
    cfil.RangeMax = 10
    cfil.Notorieties = List[Byte](bytes([3,4,5,6]))
    if len(moblist) > 1:
        cfil.Bodies = List[int](moblist)
    mobs = Mobiles.ApplyFilter(cfil)
    for m in mobs:
        if not m.Serial in ignore:
            chaseables.append(m.Serial)        
    while len(chaseables)>0:
        if Misc.ReadSharedValue('run') == 'False':
            break
        if Timer.Check('chasetimer') == False:          
            mob = Mobiles.Select(mobs,'Nearest')
            if mob:                                    
                go(mob.Position.X,mob.Position.Y)
                if not Player.InRangeMobile(mob,1):
                   ignore.append(mob.Serial) 
                Timer.Create('chasetimer',3000)
            del chaseables
            chaseables = []
            mobs = Mobiles.ApplyFilter(cfil)
            Misc.Pause(100)
            for m in mobs:
                if not m.Serial in ignore:
                    chaseables.append(m)            
        Misc.Pause(100)
   
     
                
form = dexxer(contents)
Application.Run(form)




