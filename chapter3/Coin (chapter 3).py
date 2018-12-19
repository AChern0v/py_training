import random

attempt = 100

eagle = 0
tails = 0


while attempt > 0:
    result = random.randint(1, 2)
    if result == 1: 
        eagle += 1
    else:
        tails += 1
    

    attempt -= 1

print("Орел: " + str(eagle))
print("\nРешка: " + str(tails))
