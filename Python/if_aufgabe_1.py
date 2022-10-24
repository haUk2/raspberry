

import random

randomNumber = random.randrange(100)
print(randomNumber)

if randomNumber < 20:
    print("Mini")
elif randomNumber < 50:
    print("Medium")
elif randomNumber > 50:
    print("Large")



