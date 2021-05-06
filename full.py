from replit import audio
import random,time,os
Red = "\033[0;31m"
Green = "\033[0;32m"
White = "\033[0;37m" 
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
red_back="\033[0;41m"
grey_back="\033[0;40m"


def victory():
  print(yellow+ " **    **                    **       ** **         ")
  print(blue+   "//**  **                    /**      /**//          ")
  print(yellow+ " //****    ******  **   **  /**   *  /** ** ******* ")
  print(blue+   "  //**    **////**/**  /**  /**  *** /**/**//**///**")
  print(yellow+ "   /**   /**   /**/**  /**  /** **/**/**/** /**  /**")
  print(blue+   "   /**   /**   /**/**  /**  /**** //****/** /**  /**")
  print(yellow+ "   /**   //****** //******  /**/   ///**/** ***  /**")
  print(blue+   "   //     //////   //////   //       // // ///   // ")

def defeat():
  print(red+"'||' '|'                     '||''|.    ||               '||  ")
  print(red+"  || |     ...   ... ...      ||   ||  ...    ....     .. ||  ")
  print(red+"   ||    .|  '|.  ||  ||      ||    ||  ||  .|...||  .'  '||  ")
  print(red+"   ||    ||   ||  ||  ||      ||    ||  ||  ||       |.   ||  ")
  print(red+"  .||.    '|..|'  '|..'|.    .||...|'  .||.  '|...'  '|..'||. ")

def clear():
  os.system("clear")

a0=magenta+"Infinite"
a1=magenta+"=========="
a2=magenta+"========="
a3=magenta+"========"
a4=magenta+"======="
a5=magenta+"======"
a6=magenta+"====="
a7=magenta+"===="
a8=magenta+"==="
a9=magenta+"=="
a10=magenta+"="
a11=magenta+""

s1=cyan+"=========="
s2=cyan+"========="
s3=cyan+"========"
s4=cyan+"======="
s5=cyan+"======"
s6=cyan+"====="
s7=cyan+"===="
s8=cyan+"==="
s9=cyan+"=="
s10=cyan+"="
s11=cyan+""

h1=green+"=========="
h2=green+"========="
h3=green+"========"
h4=green+"======="
h5=yellow+"======"
h6=yellow+"====="
h7=yellow+"===="
h8=red+"==="
h9=red+"=="
h10=red+"="
h11=red+""

class human:
  def __init__ (self, health, shield, weapon):
    self.health=health
    self.shield=shield
    self.weapon=weapon
  def show_hp(self):
    if self.health > 90:
      hlth=h1
    elif self.health > 80 and self.health < 91:
      hlth=h2
    elif self.health > 70 and self.health < 81:
      hlth=h3
    elif self.health > 60 and self.health < 71:
      hlth=h4
    elif self.health > 50 and self.health < 61:
      hlth=h5
    elif self.health > 40 and self.health < 51:
      hlth=h6
    elif self.health > 30 and self.health < 41:
      hlth=h7
    elif self.health > 20 and self.health < 31:
      hlth=h8
    elif self.health > 10 and self.health < 21:
      hlth=h9
    elif self.health > 0 and self.health < 11:
      hlth=h10
    else:
      hlth=h11
    print(Green+"| Total Health:  "+hlth+"|  "+str(self.health)+white)
    if self.shield > 90:
      sld=s1
    elif self.shield > 80 and self.shield < 91:
      sld=s2
    elif self.shield > 70 and self.shield < 81:
      sld=s3
    elif self.shield > 60 and self.shield < 71:
      sld=s4
    elif self.shield > 50 and self.shield < 61:
      sld=s5
    elif self.shield > 40 and self.shield < 51:
      sld=s6
    elif self.shield > 30 and self.shield < 41:
      sld=s7
    elif self.shield > 20 and self.shield < 31:
      sld=s8
    elif self.shield > 10 and self.shield < 21:
      sld=s9
    elif self.shield > 0 and self.shield < 11:
      sld=s10
    else:
      sld=s11
    print(cyan+"| Total Shield:  "+sld+"|  "+str(self.shield)+white)

class match:
  def __init__ (self, kills, left):
    self.kills=kills
    self.left=left
  def show(self):
    left=str(game.left-1)
    print(yellow+"Your kills--  "+blue+str(game.kills)+yellow+"    People left--  "+blue+left)
class weapon:
  def __init__ (self, name, dam, ammo, gain, accuracy, colo):
    self.name=name
    self.dam=dam
    self.ammo=ammo
    self.gain=gain
    self.accuracy=accuracy
    self.colo=colo
  def show_weapon(self):
    print(self.colo+"["+self.name+"]")
  def show_ammo(self):
    if self.ammo > 100000:
      bar=a0
    elif self.ammo > 90:
      bar=a1
    elif self.ammo > 80 and self.ammo < 91:
      bar=a2
    elif self.ammo > 70 and self.ammo < 81:
      bar=a3
    elif self.ammo > 60 and self.ammo < 71:
      bar=a4
    elif self.ammo > 50 and self.ammo < 61:
      bar=a5
    elif self.ammo > 40 and self.ammo < 51:
      bar=a6
    elif self.ammo > 30 and self.ammo < 41:
      bar=a7
    elif self.ammo > 20 and self.ammo < 31:
      bar=a8
    elif self.ammo > 10 and self.ammo < 21:
      bar=a9
    elif self.ammo > 0 and self.ammo < 11:
      bar=a10
    else:
      bar=a11
    if self.ammo > 100000:
      print(magenta+"| Total Ammo:  "+bar+" |  "+white)
    else: 
      print(magenta+"| Total Ammo:  "+bar+"|  "+str(self.ammo)+white)


fist=weapon("Fist",5,110e11,2,2,grey_back)
knife=weapon("Knife",8,110e11,2,2,grey_back)
shovel=weapon("Shovel",7,110e11,2,2,grey_back)
rocks=weapon("Some rocks",14,110e11,2,2,grey_back)
stick=weapon("Wood Stick",6,110e11,2,2,grey_back)
spear=weapon("Ewok Spear",20,110e11,2,2,grey_back)
rocket_launcher=weapon("Rocket Luncher",150,1,2,2,orange_back)
baton=weapon("Baton",10,110e11,2,2,grey_back)
staff=weapon("Staff",20,110e11,2,2,grey_back)
katana=weapon("Katana",20,110e11,2,2,grey_back)
slingshot=weapon("Slingshot",10,5,10,2,grey_back)
lightsaber=weapon("Lightsaber",60,110e11,2,2,blue_back)
STW48=weapon("ST-W48 Blaster",50,100,10,7,blue_back)
A180=weapon("A180 (Pistol mode)",20,50,5,7,grey_back)
A180X=weapon("A180X (Sniper Rifle mode)",75,15,2,20,blue_back)
KiSteer=weapon("KiSteer 1284 Projectile Rifle",100,15,2,10,blue_back)
A180D=weapon("A180D (Repeating Blaster mode)",25,100,10,3,grey_back)
ELG=weapon("ELG-3A Pistol",10,50,4,5,grey_back)
SE44=weapon("SE-44C Pistol",10,50,4,5,grey_back)
RT97=weapon("RT-97C Heavy Blaster Rifle",35,100,10,3,grey_back)
FWMB=weapon("FWMB-10 Repeating Blaster",25,100,10,3,grey_back)
EWEB=weapon("E-WEB Mounted Machine Gun",50,110e11,5,4,blue_back)
EL16=weapon("EL-16 Blaster Rifle",20,100,4,2,grey_back)
EC17=weapon("EC-17 Hold Out Blaster",10,110e11,2,1,grey_back)
DL44=weapon("DL-44 (Han blaster)",30,25,5,2,grey_back)
DC17=weapon("Dual DC-17 blaster pistols",30,100,10,2,blue_back)
OPDC=weapon("Overpowered Dual DC-17's", 100, 110e11, 20, 10, orange_back)
OP280=weapon("Overpowered A280", 100, 110e11, 20, 10, orange_back)
DarthVader=weapon("Darth Vador summoner", 125, 1, 2, 100, orange_back)
DC15S=weapon("DC-15S Blaster",20,100,5,2,grey_back)
DC15X=weapon("DC-15X Sniper Rifle",75,15,2,20,blue_back)
DC15=weapon("DC-15 Blaster Rifle",20,100,5,2,grey_back)
OrbitalStrike=weapon("Orbital Strike",150,3,2,1,orange_back)
E22=weapon("E-22 Blaster Rifle",65,30,10,2,blue_back)
Z6=weapon("Z-6 Heavy Repeating Blaster", 50, 100, 10, 2, blue_back )
E11=weapon("E-11 Blaster",20,100,10,2,grey_back)
E11D=weapon("E-11D CQC Gun",10,50,5,2,grey_back)
dagger=weapon("Dagger",10,110e11,2,2,grey_back)
DH17=weapon("DH-17 Pistol",10,50,5,2,grey_back)
M45=weapon("M-45 Heavy Repeating Blaster",25,100,10,3,blue_back)
DLT19=weapon("DLT-19 Heavy Repeating blaster",50,100,10,1,grey_back)
DLT19X=weapon("DLT-19X Sniper Rifle",75,15,10,20,blue_back)
RK3=weapon("RK-3 Blaster Pistol",10,25,10,2,grey_back)
A280=weapon("A280 Blaster Rifle",20,100,10,2,grey_back)
E5=weapon("E-5 Blaster",20,50,5,2,grey_back)
#______________________________
#New weapons
WR=weapon("Wrist Rocket",150,1,2,2,orange_back)
WB=weapon("Wrist Blaster",10,50,5,2,grey_back)
T21=weapon("T-21 Light Repeating Blaster",35,100,10,3,blue_back)
BCast=weapon("Bowcaster",50,20,3,5,blue_back)
Striker=weapon("Striker Projectile Pistol",70,5,1,2,orange_back)
CR24=weapon("CR-24 Flame Rifle",30,110e11,10,3,blue_back)
BD1=weapon("BD-1 Vibro-Ax",40,110e11,2,2,blue_back)
DT57=weapon("DT-57",30,30,10,7,blue_back)
KS=weapon("KiSteer 1284 Projectile Rifle",75,15,2,20,blue_back)
ELG=weapon("ELG-3A",15,25,10,2,grey_back)
TL50=weapon("TL-50 Repeating Blaster",40,100,5,2,grey_back)
NT242=weapon("NT-242 Sniper Rifle",100,10,2,10,blue_back)
Blurrg=weapon("Blurrg-1120 Blaster Pistol",50,50,5,5,blue_back)
RG4D=weapon("RG-4D Blaster Pistol",10,25,10,2,grey_back)
Valken=weapon("Valken-38X 'Sniper Rifle'",40,50,10,7,grey_back)
#self, name, dam, ammo, gain, accuracy, colo

starwarsweapons=[fist,knife,shovel,rocks,stick,spear,lightsaber,rocket_launcher,baton,staff,STW48,A180,A180X,A180D,katana,slingshot,KiSteer,ELG,SE44,RT97,FWMB,EWEB,EL16,EC17,DL44,DC17,DC15S,DC15X,DC15,OrbitalStrike,E22,E11,E11D,dagger,DH17,M45,DLT19,DLT19X,RK3,A280,E5,Z6,OPDC,OP280,DarthVader,WR,WB,T21,BCast,Striker,CR24,BD1,DT57,KS,ELG,TL50,NT242,Blurrg,RG4D,Valken]

def fight():
  print("Someone found you!! They are looking to fight!")
  input()
  enemy=human(random.randrange(1,100),random.randrange(0,100),random.choice(starwarsweapons))
  while True:
    if you.weapon.ammo < 0:
      you.weapon.ammo=0
    clear()
    print(blue_back+"Your Stats:")
    you.show_hp()
    print("")
    you.weapon.show_weapon()
    you.weapon.show_ammo()
    print(red_back+"\n\nEnemy Stats:")
    enemy.show_hp()
    print("")
    enemy.weapon.show_weapon()
    enemy.weapon.show_ammo()
    move=input(white+"\n\nYou can either attack them or run away\n[1] Attack\n[2] Run\n> ")
    clear()
    if move=="1":
      clear()
      print("You attacked them!")
      dd=random.randrange(1,you.weapon.dam)
      au=random.randrange(1,4)
      if you.weapon.ammo <= 0:
        you.weapon.ammo=0
        dd=0
      if dd==0:
        print(red+"You are all out of ammo!"+white)
      if you.weapon.ammo>100000:
        print(green+"It did "+str(dd)+" damage!"+white)
      else:
        print(green+"It did "+str(dd)+" damage!"+white)
        print(yellow+"You used "+str(au)+" ammo!"+white)
        you.weapon.ammo-=au
      if enemy.shield <= 0:
        enemy.health-=dd
      else:
        enemy.shield-=dd
      if enemy.shield < 0:
        enemy.shield=0
      if enemy.health <=0:
        enemy.health=0
        game.left-=1
        game.kills+=1
        print(green+"You won the fight!"+white)
        input()
        while True:
          clear()
          print(blue_back+"They dropped a "+enemy.weapon.name)
          print(cyan+"[1] Take it")
          print("[2] Leave it")
          d=input(white+"> ")
          if d=="1":
            print("You took the weapon")
            you.weapon=enemy.weapon
            break
          if d=="2":
            break
        break
      input()
      print("\n\nThey attacked you!")
      dt=random.randrange(1,enemy.weapon.dam)
      print(red+"It did "+str(dt)+" damage!"+white)
      if you.shield <= 0:
        you.health-=dt
      else:
        you.shield-=dt
      if you.health <=0:
        print("You lost the fight!")
        break
      if you.shield <0:
        you.shield=0
      input()
    if move=="2":
      print("They attacked you as you ran away")
      pa=random.randrange(1,enemy.weapon.dam)
      print(red+"It dealt "+str(pa)+" damage!"+white)
      input()
      if you.shield > 0:
        you.shield-=pa
      else:
        you.health-=pa
      if you.shield<=0:
        you.shield=0
      break


print(red+"Press ENTER to start animation")
input("")
#source=audio.play_file('StarWarsMainTheme.mp3')
os.system("python animation.py")
time.sleep(5)
input(blue+"\nWelcome to Star Wars Fight Simulator by   @FloCal35. In this game, you will use weapons within the Star Wars universe to fight AI and WIN!\n\n[Press ENTER to continue] ")
#source.paused = not source.paused
clear()
ppl=int(input(white+"How many people would you like in the match?\n> "))
people=ppl+1
if people>10001:
  os.system("clear")
  print("Ok, you can't do that many")
  time.sleep(3)
  os.system("clear")
  os.system("python main.py")
game=match(0,people)
you=human(100,0,fist)

while you.health > 0 and game.left > 1:
  clear()
  game.show()
  print("\n")
  you.weapon.show_weapon()
  you.weapon.show_ammo()
  print("")
  you.show_hp()
  loc=input(blue_back+"\n\nWhat will you do?"+green+"\n\n[1] Look for loot\n[2] Camp\n"+yellow+"> ")
  clear()
  if loc=="2":
    print("You decided to camp...")
    input()
    if game.left > 11:
      bb=random.randrange(1,10)
      if bb==1 or bb==2 or bb==3:
        game.left-=random.randrange(1,5)
      if bb==2:
        fight()
      clear()
  if game.left > 10:
    try:
      ch=random.randrange(1,(110-game.left))
    except:
      ch=random.randrange(1,10)
  elif game.left <=10:
    ch=random.randrange(1,10)
  if ch==2:
    fight()
  if ch==1 or ch==2 or ch==3:
    if game.left > 3:
      try:
        if game.left > 11:
          game.left-=random.randrange(1,10)
        elif game.left <= 11:
          game.left-=3
      except:
        game.left-=1
  if loc=="1":
    print(white+"You checked for loot")
    loot=random.randrange(1,6)
    if loot==4:
      print("You found ammo!")
      ammogain=random.randrange(1,you.weapon.gain)
      print("You found "+str(ammogain)+" ammo for your weapon")
      you.weapon.ammo+=ammogain
      input()
    elif loot==3:
      print("You found shield!")
      shieldnum=[5,25,50]
      shieldgain=random.choice(shieldnum)
      if you.shield < 100:
        you.shield+=shieldgain
        if you.shield>100:
          you.shield=100
      input()
    elif loot==2:
      print("You found health!")
      healthnum=[5,25,50]
      healthgain=random.choice(healthnum)
      if you.health < 100:
        you.health+=healthgain
        if you.health>100:
          you.health=100
      input()
    elif loot==1:
      print(white+"You found a weapon!")
      input()
      weaponfound=random.choice(starwarsweapons)
      while True:
        clear()
        print(blue_back+"The weapon is a "+weaponfound.name)
        print(cyan+"[1] Take it")
        print("[2] Leave it")
        tol=input(white+"> ")
        if tol=="1":
          you.weapon=weaponfound
          print(green+"You took the weapon!"+white)
          you.weapon.ammo+=you.weapon.gain
          input()
          break
        if tol=="2":
          break
    else:
      print("You didn't find anything!")
      input()
else:
  clear()
  if you.health > 0:
    victory()
    print(red_back+"You had "+str(game.kills)+" kills!"+white)
    input("")
    os.system("python3 credits.py")
  else:
    defeat()
    if game.left==1 or game.left==21:
      print("You came in "+str(game.left)+"(st) place!")
    elif game.left==3 or game.left==23:
      print("You came in "+str(game.left)+"(rd) place!")
    elif game.left==2 or game.left==22:
      print("You came in "+str(game.left)+"(nd) place!")
    else:
      print("You came in "+str(game.left)+"(th) place!")
    print("You had "+str(game.kills),"kills!"+white)
    input("")
    os.system("python credits.py")