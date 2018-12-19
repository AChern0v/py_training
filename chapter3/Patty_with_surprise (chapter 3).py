import random

patty = random.randint(1, 5)

print("Press \"Enter\" and get your patty with surprize\n\n")

if patty == 1:
    print("Сессия без комиссий")
elif patty == 2:
    print("Нормальная работа")
elif patty == 3:
    print("Суицид")
elif patty == 4:
    print("Насыщенная личная жизнь")
elif patty == 5:
    print("Достаточно денег")
else:
    print("Тебе не попался пирожок без сюрприза. Возможно, это к лучшему")
