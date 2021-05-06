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
  def show_sld(self):
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

TIEF=weapon("TIE Fighter",30,100,10,6,blue)
TIEI=weapon("TIE Interceptor",40,100,10,3,blue)
TIER=weapon("TIE Reaper",20,100,10,10,blue)
#_________________
XWing=weapon("X-Wing",30,100,10,6,blue)
AWing=weapon("A-Wing",40,100,10,3,blue)
UWing=weapon("U-Wing",20,100,10,10,blue)

#self, name, dam, ammo, gain, accuracy, colo

starwarsweapons=[TIEF,TIEI,TIER]
enemyships=[XWing,AWing,UWing]

def fight():
  print("Someone found you!! Initiate the dogfight!")
  input()
  enemy=human(random.randrange(1,100),random.randrange(0,100),random.choice(starwarsweapons))
  while True:
    if you.weapon.ammo < 0:
      you.weapon.ammo=0
    clear()
    print(blue_back+"Your Stats:")
    you.show_hp()
    you.show_sld()
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

game=match(0,30)
you=human(100,0,random.choice(enemyships))

while you.health > 0 and game.left > 1:
  clear()
  game.show()
  print("\n")
  you.weapon.show_weapon()
  you.weapon.show_ammo()
  print("")
  you.show_hp()
  you.show_sld()
  loc=input(blue_back+"\n\nWhat will you do?"+green+"\n\n[1] Explore Debris\n[2] Fly in circles\n"+yellow+"> ")
  clear()
  if loc=="2":
    print("You decided to fly in circles...")
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
    print(white+"You explored the debris and found...")
    loot=random.randrange(1,6)
    if loot==4:
      print("You found ammo!")
      ammogain=random.randrange(1,you.weapon.gain)
      print("You found "+str(ammogain)+" ammo for your weapon")
      you.weapon.ammo+=ammogain
      input()
    elif loot==3:
      print("You charged your shields!")
      shieldnum=[1,2,3,4,5,6,7]
      shieldgain=random.choice(shieldnum)
      if you.shield < 100:
        you.shield+=shieldgain
        if you.shield>100:
          you.shield=100
      input()
    elif loot==2:
      print("You found a health pickup!")
      healthnum=[5,25,50]
      healthgain=random.choice(healthnum)
      if you.health < 100:
        you.health+=healthgain
        if you.health>100:
          you.health=100
      input()
    elif loot==1:
      print(white+"You found another ship!")
      input()
      weaponfound=random.choice(enemyships)
      while True:
        clear()
        print(blue_back+"The ship is a "+weaponfound.name)
        print(cyan+"[1] Switch ships")
        print("[2] Stay put")
        tol=input(white+"> ")
        if tol=="1":
          you.weapon=weaponfound
          print(green+"You switched ships!"+white)
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
    os.system("python3 credits.py")