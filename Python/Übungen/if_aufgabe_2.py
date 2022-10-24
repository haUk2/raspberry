		# Erstelle zwei Zufallszahl zwischen 0 und 100
		
		# Wenn die erste Zahl kleiner ist als die zweite UND die erste Zahl kleiner ist als 50
		# dann gib aus "Zahl 1 ist kleiner als Zahl 2 und Mini"
		
		# Wenn die erste Zahl kleiner ist als 30 oder die zweite Zahl kleiner ist als 30
		# dann gib aus "Eine der beiden ist kleiner als 30"
		
		# Wenn die erste Zahl kleiner ist als 50 UND die zweite Zahl ungleich 50 ist
		# dann gib aus "Erste Zahl klein, zweite kein 50iger"

import random

randomNumber1 = random.randrange(100)
randomNumber2 = random.randrange(100)
print(randomNumber1)
print(randomNumber2)

if randomNumber1 < randomNumber2 and randomNumber1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

if randomNumber1 < 30 or randomNumber2 < 30:
    print("Eine der beiden ist kleiner als 30")

if randomNumber1 < 50 and randomNumber2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")

