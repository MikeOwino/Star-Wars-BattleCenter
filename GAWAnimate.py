import time,os
from replit import audio
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

def clear():
  os.system("clear")

def wait(x):
  time.sleep(x)

#source=audio.play_file('StarWarsMainTheme.mp3')
clear()
print(blue+"A long time ago, in a galaxy far far away....")
time.sleep(5)
print(yellow+"      _                                       ")  
print(yellow+"  ___| |_ __ _ _ __  __      ____ _ _ __ ___  ")
print(yellow+" / __| __/ _` | '__| \ \ /\ / / _` | '__/ __| ")
print(yellow+" \__ \ || (_| | |     \ V  V / (_| | |  \__ \ ")
print(yellow+" |___/\__\__,_|_|      \_/\_/ \__,_|_|  |___/ ")
wait(2)
clear()
print(yellow+"            ________   ___   ____                              ")
print(yellow+"           / __   __| / _ \ |  _ \                             ")
print(yellow+"     ______> \ | |   |  _  ||    /__________________________   ")
print(yellow+"    / _______/ |_|   |_| |_||_|\___________________________ \  ")
print(yellow+"   / /                                                     \ \ ")
print(yellow+"  | |"+red+"   ____    ___        __   "+white+"          |  _  |           "+yellow+"| |")
print(yellow+"  | |"+red+"  / ___|  / \ \      / /   "+white+"          |=(_)=|           "+yellow+"| |")
print(yellow+"  | |"+red+" | |  _  / _ \ \ /\ / /    "+white+"          |     |           "+yellow+"| |")
print(yellow+"  | |"+red+" | |_| |/ ___ \ V  V /     "+white+"  / _  _ \       /  _  \    "+yellow+"| |")
print(yellow+"  | |"+red+"  \____/_/   \_\_/\_/      "+white+" |=(_)(_)=|     |-=(_)=-|   "+yellow+"| |")
print(yellow+"  | |"+red+"                           "+white+"  \   '  /       \     /    "+yellow+"| |")
print(yellow+"   \ \_________________________    _   ___   ____   _______/ / ")
print(yellow+"    \________________________  |  | | / _ \ |  _ \ / _______/  ")
print(yellow+"                             | |/\| ||  _  ||    / > \         ")
print(yellow+"                              \_/\_/ |_| |_||_|\_\|__/         ")



wait(1.5)
print("")
print(white+"   "+blue_back+"         __           ______     _____     ______ ____      "+white)
print(white+"   "+blue_back+"        / /  __ __   / __/ /__  / ___/__ _/ /_  // __/      "+white)
print(white+"   "+blue_back+"       / _ \/ // /  / _// / _ \/ /__/ _ `/ //_ </__ \       "+white)
print(white+"   "+blue_back+"      /_.__/\_, /  /_/ /_/\___/\___/\_,_/_/____/____/       "+white)
print(white+"   "+blue_back+"           /___/                                            "+white)
input()
print(blue+"Welcome to the Star Wars: Galaxy At War sneak peek")
wait(.5)
print("Fly your factions ships against the opposing one in randomized dogfights\n\n(NOTE: This is a sneak peek so everything is subject to change)")
input(white+"\n[Press ENTER to continue]\n")
#source.paused = not source.paused
clear()