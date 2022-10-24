#Erstelle ein Programm, dass Zufallszahlen zwischen 10 und 30 generiert.
 #Das Programm soll die Zufallszahlen zusammenzählen.
 # Sobald die Zahl 15 oder die Zahl 25 kommt, 
  #wird das Programm beendet und die Summe der vorherigen Zufallszahlen ausgegeben!
import random
sum = 0

while True:
    randInt = random.randrange(10, 30)
    if randInt == 15 or randInt == 25:
        break
    sum += randInt
print(randInt)
print(sum)


