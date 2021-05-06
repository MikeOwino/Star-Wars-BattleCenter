import time, os
def clear():
  os.system("clear")
wait=0
timeleft=31
while wait<30:
  clear()
  wait+=1
  timeleft-=1
  print("Loading")
  print(timeleft)
  time.sleep(1)
  clear()
  wait+=1
  timeleft-=1
  print("Loading.")
  print(timeleft)
  time.sleep(1)
  clear()
  wait+=1
  timeleft-=1
  print("Loading..")
  print(timeleft)
  time.sleep(1)
  clear()
  wait+=1
  timeleft-=1
  print("Loading...")
  print(timeleft)
  time.sleep(1)
  clear()
else:
  clear()