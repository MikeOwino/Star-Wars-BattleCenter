import random,time,os
from time import sleep
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
pink_back="\033[0;45m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
brown="\033[0;33m"

def ewok():
  print(brown+"                            . ")
  print(brown+"                           -: ")
  print(brown+"                          `s  ")
  print(brown+"                          :y` ")
  print(brown+"                         .os  ")
  print(brown+"           ..----``      +h.  ")
  print(brown+"          :ooyyhhys/::.` oo   ")
  print(brown+"         .ssosyssyysyhs.`s:   ")
  print(brown+"         os+oyyhhysshy: -y`   ")
  print(brown+"        :yo/ohddmdmhyh+ /y    ")
  print(brown+"      .+yy:-/hdmy/+hhy:`s+    ")
  print(brown+"    ./ysyhhsoss+++oyhh+:o/`   ")
  print(brown+"   .+yhmmmmmmdmddddhmy//o++.  ")
  print(brown+"  `+yddmhhhhhddddhmNh+oyhhs.  ")
  print(brown+"  :shmdhyyhhhhhdddNNNhydNmo`  ")
  print(brown+" `+hmNddhhhhhhhmNMMMMNddmy.   ")
  print(brown+" `odmmmmdhyyhdNmNNMMMNyh/`    ")
  print(brown+" -ymNysmhdhmNNNddmNNNNy+      ")
  print(brown+" :hmmh:odmMMNmmdhhdNNmh-      ")
  print(brown+" `-++o..yNMMMNmmmmmNNmh       ")
  print(brown+"        .smMMMNNNddNNdo       ")
  print(brown+"         .sNMMNNNNNNNd:       ")
  print(brown+"        -dNMMMNNNNNMhh`       ")
  print(brown+"        -ossohmNNNNNoo        ")
  print(brown+"             +yyydy:h-        ")
  print("")
  print(brown+"          EWOK HUNT           ")


def defeat():
  print(red+"'||' '|'                     '||''|.    ||               '||  ")
  print(red+"  || |     ...   ... ...      ||   ||  ...    ....     .. ||  ")
  print(red+"   ||    .|  '|.  ||  ||      ||    ||  ||  .|...||  .'  '||  ")
  print(red+"   ||    ||   ||  ||  ||      ||    ||  ||  ||       |.   ||  ")
  print(red+"  .||.    '|..|'  '|..'|.    .||...|'  .||.  '|...'  '|..'||. ")


def clear():
  os.system("clear")

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

class human:
  def __init__ (self, health, weapon):
    self.health=health
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
class match:
  def __init__ (self, kills):
    self.kills=kills
  def show(self):
    print(yellow+"Your kills--  "+blue+str(game.kills)+yellow)
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

spear=weapon("Ewok Spear",20,110e11,2,2,grey_back)
sling=weapon("Fairy Slingshot",30,5,1,3,blue_back)
E11=weapon("E-11 Blaster",20,100,7,3,grey_back)
DLT19=weapon("DLT-19 Heavy Repeating blaster",50,100,10,2,grey_back)
nihl=weapon("Nothing",0,110e11,0,0,white)
#self, name, dam, ammo, gain, accuracy, colo

ewoks=[spear,spear,sling]
stormtroopers=[E11,DLT19]





ewok()
input()

input(blue+"\nWelcome to Ewok Hunt!\nGet thrown onto the forest moon of Endor with nothing\nbut an E-11 or DLT-19 (if you get lucky).\nKill as many ewoks as you can before the catch you\n\n[Press ENTER to continue] ")
clear()
game=match(0)
you=human(100,nihl)

def battle():
  clear()
  roundweapon=random.choice(stormtroopers)
  you.weapon=roundweapon
  enemy=human(random.randrange(1,100),random.choice(ewoks))
  input(red+"You spotted an ewok..."+white)
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
    move=input(white+"\n\nPress enter to attack\n>")
    clear()
    if move=="":
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
        enemy.health-=dd
        print(green+"It did "+str(dd)+" damage!"+white)
        print(yellow+"You used "+str(au)+" ammo!"+white)
        you.weapon.ammo-=au
      if enemy.health <=0:
        enemy.health=0
        print(green+"You won the fight!"+white)
        game.kills+=1
        input()
        break
      input()
      print("\n\nThey attacked you!")
      dt=random.randrange(1,enemy.weapon.dam)
      print(red+"It did "+str(dt)+" damage!"+white)
      if you.health <=0:
        print("You lost the fight!")
        break
      input()
      you.health-=dt

while you.health>0:
  attack=random.randint(1,3)
  if attack==1:
    clear()
    print(magenta+"You were not spotted by any ewoks")
    healthgain=random.randint(5,35)
    print("You gained",green+str(healthgain)+magenta,"health"+white)
    you.health+=healthgain
    input()
  else:
    battle()
    

clear()
defeat()
print(red+"You did not survive a night on Endor")
print("Man them ewoks be (e)woke XD")
print("")
print("You killed a total of",yellow+str(game.kills),red+"ewoks")
input()
os.system("python credits.py")
#time.sleep(2)
#user=input(yellow+"What is your username (so you can #be added to the leaderboard)- ")
#kills=str(game.kills)
#message=user,kills
#write=message
#
#
#writeuser = open("users.txt","a")
#writeuser.write(write)
#writeuser.close()
#input()
#clear()
#print(green+"Your username has been added!")