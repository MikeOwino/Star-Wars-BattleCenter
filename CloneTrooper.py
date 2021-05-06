import time,os,random
def clear():
  os.system("clear")
  
def wait(x):
  time.sleep(x)

white = "\033[0;37m" 
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
bright_black = "\033[0;90m"

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

class human:
  def __init__ (self, name, health, weapon, shield):
    self.name=name
    self.health=health
    self.weapon=weapon
    self.item=item
    self.shield=shield
  def show_shield(self):
    if self.shield > 90:
      sld=s1
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 80 and self.shield < 91:
      sld=s2
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 70 and self.shield < 81:
      sld=s3
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 60 and self.shield < 71:
      sld=s4
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 50 and self.shield < 61:
      sld=s5
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 40 and self.shield < 51:
      sld=s6
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 30 and self.shield < 41:
      sld=s7
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 20 and self.shield < 31:
      sld=s8
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 10 and self.shield < 21:
      sld=s9
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    elif self.shield > 0 and self.shield < 11:
      sld=s10
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
    else:
      sld=h11
      print(blue_back+"Total Shield:  "+sld+"|  "+cyan+str(self.shield)+white)
  def show_name(self):
    print(self.name)
  def show_hp(self):
    if self.health > 90:
      hlth=h1
      print(green+"Total Health:  "+hlth+"|  "+green+str(self.health)+white)
    elif self.health > 80 and self.health < 91:
      hlth=h2
      print(green+"Total Health:  "+hlth+"|  "+green+str(self.health)+white)
    elif self.health > 70 and self.health < 81:
      hlth=h3
      print(green+"Total Health:  "+hlth+"|  "+green+str(self.health)+white)
    elif self.health > 60 and self.health < 71:
      hlth=h4
      print(green+"Total Health:  "+hlth+"|  "+green+str(self.health)+white)
    elif self.health > 50 and self.health < 61:
      hlth=h5
      print(yellow+"Total Health:  "+hlth+"|  "+yellow+str(self.health)+white)
    elif self.health > 40 and self.health < 51:
      hlth=h6
      print(yellow+"Total Health:  "+hlth+"|  "+yellow+str(self.health)+white)
    elif self.health > 30 and self.health < 41:
      hlth=h7
      print(yellow+"Total Health:  "+hlth+"|  "+yellow+str(self.health)+white)
    elif self.health > 20 and self.health < 31:
      hlth=h8
      print(red+"Total Health:  "+hlth+"|  "+red+str(self.health)+white)
    elif self.health > 10 and self.health < 21:
      hlth=h9
      print(red+"Total Health:  "+hlth+"|  "+red+str(self.health)+white)
    elif self.health > 0 and self.health < 11:
      hlth=h10
      print(red+"Total Health:  "+hlth+"|  "+red+str(self.health)+white)
    else:
      hlth=h11
      print(red+"Total Health:  "+hlth+"|  "+red+str(self.health)+white)

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
      print(yellow+"Total Ammo:  "+bar+white+" |  "+yellow)
    else: 
      print(yellow+"Total Ammo:  "+bar+white+"|  "+yellow+str(self.ammo))

class item:
  def __init__ (self, name, price):
    self.name=name
    self.price=price
  def show_price(self):
    print(self.price)
  def show_item(self):
    print(self.name)


knife=weapon("Knife",8,110e11,2,10,grey_back)
rocket_launcher=weapon("Rocket Luncher",150,2,1,2,orange_back)
EWEB=weapon("E-WEB Mounted Machine Gun",50,110e11,100,4,blue_back)
DC17=weapon("Dual DC-17 blaster pistols",30,30,10,13,blue_back)
DC15S=weapon("DC-15S Blaster",20,30,10,4,grey_back)
DC15X=weapon("DC-15X Sniper Rifle",75,10,3,20,blue_back)
DC15=weapon("DC-15 Blaster Rifle",20,50,15,5,grey_back)
Z6=weapon("Z-6 Heavy Repeating Blaster", 50, 100, 20, 2, blue_back )
E5=weapon("E-5 Blaster",15,50,5,2,grey_back)
DC17M=weapon("DC-17m",35,50,7,5,blue_back)
OP=weapon("OP",100,100,30,50,orange_back)
SBDA=weapon("Super Battle Droid Arm Gun", 30, 50, 10, 4, blue_back)
DKA=weapon("Droidika Arm Cannons", 50, 110e11,100,5,orange_back)
#self, name, dam, ammo, gain, accuracy, colo

beskar=item("Small peice of Beskar", 50)
head=item("B-1 Battle Droid Head",15)
helmet=item("Helmet of a dead trooper",20)
stock=item("Empty weapon stock", 5)
scope=item("Weapon Scope",13)
wee=item("Weapon Energy Emitter", 21)
wfc=item("Weapon Firing Chanber", 11)
wpr=item("Weapon Power Regulator", 27)
restrainbolt=item("Restraining Bolt",15)
KyberChrystal=item("Kyber Chrystal", 120)
noneitem=item("None",0)

weapons=[knife,rocket_launcher,EWEB,DC17,DC15S,DC15X,DC15,E5,Z6,DC17M]
enemyweapons=[E5,E5,E5,E5,E5,E5,E5,E5,EWEB,knife,DC17,DC15S,DC15]
items=[beskar,KyberChrystal,head,head,head,head,head,head,head,head,head,head,head,head,helmet,helmet,helmet,helmet,helmet,helmet,helmet,helmet,stock,stock,stock,stock,stock,stock,scope,scope,scope,wee,wee,wee,wfc,wfc,wfc,wpr,wpr,wpr]
battles1=0
battlesrun=0
battlesl=0


last4letters=random.randint(1000,9999)
name="CT-"+str(last4letters)
Rank=["Private","Corporal","Sergeant","Sergeant Major","2nd Lieutenant","Lieutenant","Captain","Major","Battalion Commander","Regimental Commander","Senior Commander","Marshal Commander"]
RankPoints=2
money=15
listplace=0
CurrentRank=Rank[listplace]

you=human(name,100,DC15S,0)
you.item=noneitem

e1h=random.randint(1,50)
b1bd=human("B-1 Battle Droid",e1h,E5,0)

e2h=random.randint(10,75)
scd=human("Commando Droid",e2h,E5,0)

e3h=random.randint(20,60)
superbd=human("Super Battle Droid", e2h, SBDA,0)

e4h=random.randint(30,70)
roll=human("Droidika", e3h,DKA,50)

nonenemy=human("You've completed the story mode!",100,rocket_launcher,100)

enemychoice=[b1bd,scd,superbd,roll,nonenemy,nonenemy,nonenemy]
elistplace=0
CurrentEnemy=enemychoice[elistplace]

c=0
i=0
#Yes I was lazy


q1="The TIE Fighter flown by Moff Gideon is called... \nA-TIE X32 or B-Outland TIE- "
q2="How many passengers could the HAVw A6 Juggernaut hold.\nA-200 or B-300- "
q3="When he died, Kylo Ren (Ben Solo) was\nA-35 or B-30 years old- "
q4="The BLT-B Y-wing was produced during this war...\nA-Galactic Civil or B-Clone Wars- "
q5="The Arquitens-class light cruiser had (A-5 or B-3) months\nof consumables- "
q6="What sniper rifle does/did Din Djarin carry...\nA-Modified DLT-19X B-Amban Sniper Rifle- "
q7="The RK-3 blaster pistol was made by...\nA-SonnBlas B-MerrSon- " 
q8="The official name for the Death Star (1) plans was called Project...\nA-Omega One B-Star Dust- "
q9="Sabine Wren weilded this ancient mandalorian weapon...\nA-Dual WESTAR-35 pistols B-The Darksaber- "
q10="Qui Gon Jin was an apprentice to this jedi master...\nA-Mace Windu B-Count Dooku- "
q11="Captain Phasma's awesome armor was made from this material... \nA-Titanium B-Chromium- "
q12="The E-11D was designed for...\nA-Long range combat B-Close range combat- "
q13="The ELG-3A was used by this person...\nA-Rey Palpatine/Skywalker/WhoKnowsWhat B-Padme Amidala- "

questions=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]


print(red+"Press ENTER to start animation")
intro=input("")
if intro=="hack":
  clear()
else:
  os.system("python CTAnimate.py")
print(blue+"Your clone name is")
wait(.75)
clear()
print(blue+"Your clone name is.")
wait(.75)
clear()
print(blue+"Your clone name is..")
wait(.75)
clear()
print(blue+"Your clone name is...")
wait(.75)
clear()
print(blue+"Your clone name is "+orange_back+"CT-"+str(last4letters)+white)
wait(.5)
print("\n")
wait(.5)
input("[Press ENTER to continue]\n")
clear()
while you.health>0 and money>=0 and RankPoints>=0 and listplace<=11:
  print(blue_back+name)
  print(magenta+"Rank- "+CurrentRank)
  print("")
  you.show_hp()
  print("")
  you.weapon.show_weapon()
  you.weapon.show_ammo()
  print("")
  print(cyan+"Rank Points-",str(RankPoints))
  print(yellow+"€redits-",str(money))
  print()
  print(magenta+"Your current item...")
  you.item.show_item()
  print(white+"_______________________\n")
  print(blue+"  1. Fight a battle")
  print(blue+"  2. Shop")
  print(blue+"  3. Rank up (10 rank points)")
  move=input(">"+white)
  if move=="1":
    clear()
    print(yellow+"Which would you like to do...")
    print("  1. Story Mode (face off against 3 differant opponents to win big $$$ at the end")
    print("  2. Fight a random opponent (reccomended if you need $$$ and rank points)")
    fightmove=input("> "+white)
    if fightmove=="1":
      #put enemies in chronological order
      print("You started a fight")
      input()
      enemy=CurrentEnemy
      while True:
        if you.weapon.ammo < 0:
          you.weapon.ammo=0
        clear()
        print(blue_back+"Your Stats:")
        you.show_hp()
        print("")
        you.weapon.show_weapon()
        you.weapon.show_ammo()
        print(red_back+"\n\n")
        enemy.show_name()
        print("Stats:\n")
        enemy.show_hp()
        enemy.show_shield()
        print("")
        enemy.weapon.show_weapon()
        enemy.weapon.show_ammo()
        move=input(white+"\n\nYou can either attack them or run away\n1. Attack\n2. Run\n> ")
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
            if enemy.shield>0:
              enemy.shield-=dd
            else:
              enemy.health-=dd
            print(green+"It did "+str(dd)+" damage!"+white)
            print(yellow+"You used "+str(au)+" ammo!"+white)
            you.weapon.ammo-=au
          if enemy.health <=0:
            enemy.health=0
            print(green+"You won the fight!"+white)
            battles1+=1
            input()
            if enemy==roll:
              clear()
              print(blue+"Congradulations, you have completed the story mode")
              print("You got",yellow+"100 €redits")
              print(blue+"And "+magenta+"25 Rank Points")
              money+=100
              RankPoints+=25
              input()
              break
            else:
              wingain=random.randint(1,2)
              if wingain==1:
                while True:
                  clear()
                  found=random.choice(items)
                  you.item=found
                  print(blue_back+"You found a..."+green)
                  you.item.show_item()
                  input()
                  print(white+"You can sell it for"+yellow)
                  you.item.show_price()
                  print("€redits"+white)
                  input()
                  break
              else:
                while True:
                  clear()
                  print(blue_back+"They dropped a "+enemy.weapon.name)
                  print(cyan+"1. Take it")
                  print("2. Leave it")
                  d=input(white+"> ")
                  if d=="1":
                    print("You took the weapon")
                    you.weapon=enemy.weapon
                    break
                  if d=="2":
                    ...
                  break
              credgain=random.randint(5,30)
              clear()
              print("You got"+yellow,str(credgain),"€redits"+white)
              elistplace+=1
              CurrentEnemy=enemychoice[elistplace]
              money+=credgain
              input()
              clear()
              pointgain=random.randint(3,7)
              print("You got"+yellow,str(pointgain),"Rank Points"+white)
              RankPoints+=pointgain
              input()
              clear()
              break
          input()
          print("\n\nThey attacked you!")
          dt=random.randrange(1,enemy.weapon.dam)
          print(red+"It did "+str(dt)+" damage!"+white)
          if you.health <=0:
            print("You lost the fight!")
            battlesl+=1
            elistplace-=1
            break
          input()
          you.health-=dt
        if move=="2":
          battlesrun+=1
          print("They attacked you as you ran away")
          pa=random.randrange(1,enemy.weapon.dam)
          print(red+"It dealt "+str(pa)+" damage!"+white)
          input()
          you.health-=pa
          elistplace-=1
          clear()
          credgain=random.randint(0,10)
          print("You got"+yellow,str(credgain),"€redits"+white)
          money+=credgain
          input()
          clear()
          pointgain=random.randint(0,3)
          print("You got"+yellow,str(pointgain),"Rank Points"+white)
          RankPoints+=pointgain
          input()
          clear()
          break
      clear()
    elif fightmove=="2":
      input(red+"You started a fight..."+white)
      enemy=human("None",random.randrange(1,100),random.choice(enemyweapons),0)
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
        move=input(white+"\n\nYou can either attack them or run away\n1. Attack\n2. Run\n> ")
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
            enemy.health-=dd
            print(green+"It did "+str(dd)+" damage!"+white)
            print(yellow+"You used "+str(au)+" ammo!"+white)
            you.weapon.ammo-=au
          if enemy.health <=0:
            enemy.health=0
            print(green+"You won the fight!"+white)
            battles1+=1
            input()
            wingain=random.randint(1,2)
            if wingain==1:
              while True:
                clear()
                found=random.choice(items)
                you.item=found
                print(blue_back+"You found a..."+green)
                you.item.show_item()
                input()
                print(white+"You can sell it for"+yellow)
                you.item.show_price()
                print("€redits"+white)
                input()
                break
            else:
              while True:
                clear()
                print(blue_back+"They dropped a "+enemy.weapon.name)
                print(cyan+"1. Take it")
                print("2. Leave it")
                d=input(white+"> ")
                if d=="1":
                  print("You took the weapon")
                  you.weapon=enemy.weapon
                  break
                if d=="2":
                  ...
                break
            credgain=random.randint(5,30)
            clear()
            print("You got"+yellow,str(credgain),"€redits"+white)
            money+=credgain
            input()
            clear()
            pointgain=random.randint(3,7)
            print("You got"+yellow,str(pointgain),"Rank Points"+white)
            RankPoints+=pointgain
            input()
            clear()
            break
          input()
          print("\n\nThey attacked you!")
          dt=random.randrange(1,enemy.weapon.dam)
          print(red+"It did "+str(dt)+" damage!"+white)
          if you.health <=0:
            print("You lost the fight!")
            battlesl+=1
            break
          input()
          you.health-=dt
        if move=="2":
          battlesrun+=1
          print("They attacked you as you ran away")
          pa=random.randrange(1,enemy.weapon.dam)
          print(red+"It dealt "+str(pa)+" damage!"+white)
          input()
          you.health-=pa
          clear()
          credgain=random.randint(0,10)
          print("You got"+yellow,str(credgain),"€redits"+white)
          money+=credgain
          input()
          clear()
          pointgain=random.randint(0,3)
          print("You got"+yellow,str(pointgain),"Rank Points"+white)
          RankPoints+=pointgain
          input()
          clear()
          break
      clear()
  elif move=="2":
    clear()
    print(blue_back+"Shop"+white)
    print("")
    print("  "+grey_back+"1. Buy"+white)
    print("  "+grey_back+"2. Sell"+white)
    print(red+"You can exit by pressing ENTER")
    shopchoice=input(blue+">"+white)
    if shopchoice=="1":
      clear()
      print(blue_back+"Shop-->Buy"+white)
      print("  "+grey_back+"1. Weapons"+white)
      print("  "+grey_back+"2. Other Items"+white)
      print(red+"Anything in red is the price in €redits")
      itemschoice=input(blue+">"+white)
      if itemschoice=="1":
        clear()
        print(blue_back+"Shop-->Buy-->Weapons"+white)
        print(red+"[125] "+grey_back+"1. Rocket Launcher"+white)
        print(red+"[100] "+grey_back+"2. E-WEB Mounted Machine Gun"+white)
        print(red+"[75]  "+grey_back+"3. Z-6 Heavy Repeating Blaster"+white)
        print(red+"[50]  "+grey_back+"4. DC-17m Interchangeable Weapon System"+white)
        print(red+"[50]  "+grey_back+"5. DC-15X Sniper Rifle"+white)
        print(red+"[30]  "+grey_back+"6. Duel DC-17 Blaster Pistols"+white)
        print(red+"[20]  "+grey_back+"7. DC-15 Blaster Rifle"+white)
        print(red+"[10]  "+grey_back+"8. DC-15S Blaster"+white)
        weaponschoice=input(blue+">"+white)
        if weaponschoice=="1":
          you.weapon=rocket_launcher
          you.weapon.ammo+=you.weapon.gain
          print("You bought a rocket launcher for",yellow+"125 €redits")
          money-=125
          input()
          clear()
        elif weaponschoice=="2":
          you.weapon=EWEB
          you.weapon.ammo+=you.weapon.gain
          print("You bought a E-WEB for",yellow+"100 €redits")
          money-=100
          input()
          clear()
        elif weaponschoice=="3":
          you.weapon=Z6
          you.weapon.ammo+=you.weapon.gain
          print("You bought a Z-6 for",yellow+"75 €redits")
          money-=75
          input()
          clear()
        elif weaponschoice=="4":
          you.weapon=DC17M
          you.weapon.ammo+=you.weapon.gain
          print("You bought a DC-17m for",yellow+"50 €redits")
          money-=50
          input()
          clear()
        elif weaponschoice=="5":
          you.weapon=DC15X
          you.weapon.ammo+=you.weapon.gain
          print("You bought a DC-15X for",yellow+"50 €redits")
          money-=50
          input()
          clear()
        elif weaponschoice=="6":
          you.weapon=DC17
          you.weapon.ammo+=you.weapon.gain
          print("You bought 2 DC-17's for",yellow+"30 €redits")
          money-=30
          input()
          clear()
        elif weaponschoice=="7":
          you.weapon=DC15
          you.weapon.ammo+=you.weapon.gain
          print("You bought a DC-15 for",yellow+"20 €redits")
          money-=20
          input()
          clear()
        elif weaponschoice=="8":
          you.weapon=DC15S
          you.weapon.ammo+=you.weapon.gain
          print("You bought a DC-15s for",yellow+"10 €redits")
          money-=10
          input()
          clear()
        else:
          clear()
      elif itemschoice=="2":
        clear()
        print(blue_back+"Shop-->Buy-->Other Items"+white)
        print(red+"[10]  "+grey_back+"1. Health Stem (quick, small health regained)"+white)
        print(red+"[25]  "+grey_back+"2. Medkit (slow, more health regained)"+white)
        print(red+"[15]  "+grey_back+"3. Ammo pack (quick, small amount of ammo)"+white)
        print(red+"[35]  "+grey_back+"4. Ammo box (slow, more ammo)"+white)
        itemschoice=input(blue+">"+white)
        if itemschoice=="1":
          print("You bought a ",yellow+"health stim!"+white)
          print("[NOTE: This will take 15 seconds]")
          hac1=input("")
          if hac1=="hack":
            clear()
          else:
            os.system("python wait15.py")
          healthgain=random.randint(3,20)
          if you.health < 100:
            you.health+=healthgain
          if you.health>100:
            you.health=100
          print("You gained"+green,str(healthgain),"Health!")
          money-=10
          input()
          clear()
        elif itemschoice=="2":
          print("You bought a",yellow+"Medkit!"+white)
          print("[NOTE: This will take 30 seconds]")
          hac2=input("")
          if hac2=="hack":
            ...
          else:
            os.system("python wait30.py")
          healthgain=random.randint(17,70)
          if you.health < 100:
            you.health+=healthgain
          if you.health>100:
            you.health=100
          print("You gained"+green,str(healthgain),"Health!")
          money-=25
          input()
          clear()
        elif itemschoice=="3":
          print("You bought a",yellow+"ammo pack!"+white)
          print("[NOTE: This will take 15 seconds]")
          hac3=input("")
          if hac3=="hack":
            ...
          else:
            os.system("python wait15.py")
          tfa=1/2*(you.weapon.gain)
          ammogain=random.randrange(1,tfa)
          print("You got"+green,str(ammogain),white+"ammo for your weapon")
          you.weapon.ammo+=ammogain
          money-=15
          input()
          clear()
        elif itemschoice=="4":
          print("You bought a",yellow+"ammo box!"+white)
          print("[NOTE: This will take 30 seconds]")
          hac4=input("")
          if hac4=="hack":
            ...
          else:
            os.system("python wait30.py")
          ag=2*(you.weapon.gain)
          ammogain=random.randrange(1,ag)
          print("You got"+green,str(ammogain),white+"ammo for your weapon")
          you.weapon.ammo+=ammogain
          money-=35
          input()
          clear()
        else:
          clear()
      else:
        clear()
    elif shopchoice=="2":
      clear()
      print(blue_back+"Shop-->Sell"+white)
      print("  "+grey_back+"1. Current Item"+white)
      print("  "+grey_back+"2. Weapon"+white)
      sellmove=input(blue+">"+white)
      if sellmove=="1":
        clear()
        if you.item==noneitem:
          print(red+"Error, cannot sell 'None'"+white)
          input()
          clear()
        else:
          print(red+"You sold your"+magenta)
          you.item.show_item()
          print(red+"for"+yellow)
          you.item.show_price()
          print("€redits"+white)
          input()
          sellgain=you.item.price
          money+=sellgain
          clear()
          you.item=noneitem
      elif sellmove=="2":
        clear()
        print(red+"Are you sure you want to sell your current weapon\nYou will be given the starting weapon but will get half the €redits")
        sure=input(">"+white).lower()
        if sure=="yes" or sure=="y" or sure=="sure" or sure=="yep":
          if you.weapon==rocket_launcher:
            print("You sold your",green,"rocket launcher",white,"for",yellow,"75 €redits")
            money+=75
            you.weapon=DC15S
            input()
            clear()
          elif you.weapon==EWEB:
            print("You sold your",green,"E-WEB",white,"for",yellow,"50 €redits")
            money+=50
            you.weapon=DC15S
            input()
            clear()
          elif you.weapon==Z6:
            print("You sold your",green,"Z-6",white,"for",yellow,"35 €redits")
            money+=35
            you.weapon=DC15S
            input()
            clear()
          elif you.weapon==DC17M:
            print("You sold your",green,"DC-17m",white,"for",yellow,"25 €redits")
            money+=25
            you.weapon=DC15S
            input()
            clear()
          elif you.weapon==DC15X:
            print("You sold your",green,"DC-15X",white,"for",yellow,"25 €redits")
            money+=25
            you.weapon=DC15S
            input()
            clear()
          elif you.weapon==DC17:
            print("You sold your",green,"DC-17's",white,"for",yellow,"15 €redits")
            money+=15
            you.weapon=DC15S
            input()
            clear()
          elif you.weapon==DC15:
            print("You sold your",green,"DC-15",white,"for",yellow,"10 €redits")
            money+=10
            you.weapon=DC15S
            input()
            clear()
          elif you.weapon==DC15S:
            print("Sorry, you can't sell that weapon")
            input()
            clear()
          elif you.weapon==E5 or you.weapon==SBDA or you.weapon==DKA:
            print("Sorry, the republic doesn't accept CIA weapons")
            input()
            clear()
          else:
            clear()
        else:
          clear()
    else:
      clear()
  elif move=="3":
    if RankPoints<10:
      print(red+"You don't have enough "+yellow+"Rank Points"+white)
      input()
      clear()
    else:
      clear()
      RankPoints-=10
      listplace+=1
      CurrentRank=Rank[listplace]
      print("Your new rank is"+green,CurrentRank+white)
      input()
      clear()
  else:
    clear()
else:
  capture=random.randint(1,100)
  escape="False"
  if capture==2:
    clear()
    print(red+"GAME OVER!")
    input(white+"")
    print(yellow+"You ended with the rank"+orange_back,CurrentRank)
    input(white+"")
    print(green+"You won",str(battles1),"battles")
    input(white+"")
    print(grey_back+"You ran from",str(battlesrun),"battles")
    input(white+"")
    print(red+"You lost",str(battlesl),"battles")
    input(white+"")
    os.system("python credits.py")
  else:
    if escape=="False":
      print(green+"You got captured instead of killed. Answer the following question to escape\n")
      qes=random.choice(questions)
      print(qes)
      qesans=input(white+"> ").lower()
      if qesans=="b":
        escape+="true"
        print(green+"You escaped!")
        input()
        caphlth=random.randint(15,75)
        you.health+=caphlth
        print(white+"\nWhile you were captured, you gained",green+str(caphlth),"health!"+white)
      else:
        print(red+"Incorrect answer")  
        time.sleep(1)
        print(red+"GAME OVER!")
        input(white+"")
        print(yellow+"You ended with the rank"+orange_back,CurrentRank)
        input(white+"")
        print(green+"You won",str(battles1),"battles")
        input(white+"")
        print(grey_back+"You ran from",str(battlesrun),"battles")
        input(white+"")
        print(red+"You lost",str(battlesl),"battles")
        input(white+"")
        os.system("python credits.py")
    else:
      print(red+"You won't be that lucky")  
      time.sleep(1)
      print(red+"GAME OVER!")
      input(white+"")
      print(yellow+"You ended with the rank"+orange_back,CurrentRank)
      input(white+"")
      print(green+"You won",str(battles1),"battles")
      input(white+"")
      print(grey_back+"You ran from",str(battlesrun),"battles")
      input(white+"")
      print(red+"You lost",str(battlesl),"battles")
      input(white+"")
      os.system("python credits.py")