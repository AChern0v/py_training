# Анаrраммы 

import random



#создадим последовательность слов. из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")

word = random.choice(WORDS)
correct = word
jumble = ""

#подсказка
hint = ""

# право на подсказку
hint_answer = ""

if word == WORDS[0]:
	hint = "\nПодсказка: Так называется этот язык\n"
elif word == WORDS[1]:
	hint = "\nПодсказка: Так называется эта игра\n"
elif word == WORDS[2]:
	hint = "\nПодсказка: Антоним к слову \" сложная\" \n"
elif word == WORDS[3]:
	hint = "\nПодсказка: Антоним к слову \" простая\" \n"
elif word == WORDS[4]:
	"\nПодсказка: Правильный о...\n"
elif word == WORDS[5]:
	hint = "\nПодсказка: На это ставят стакан\n"



while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]

print(
'''
		Добро пожаловать в игру 'Анаграммы'!
Надо переставить буквы так. чтобы получилось осмысленное слово.
(Для выхода нажмите Enter, не вводя своей версии.)

''')

print("Boт анаграмма: ", jumble)

guess = " "

attempt = 0

while guess != correct and guess != "":
	print("\nK сожалению. вы неправы.")
	guess = input("Попробуйте отгадать исходное слово: ")
	attempt += 1
	if guess != correct:
		hint_answer = input("Дать подсказку? ")
		if hint_answer == "Да" or hint_answer == "да":
			print(hint)
		

#Очки за правильный ответ
score = 11

tmp = attempt

for i in range(tmp):
	score -= tmp
	tmp = 0
#Штрафные баллы за подсказку
if hint_answer == "Да":
	score /= 2
	

if guess == correct:
	print("\nДa. именно так! Вы отгадали! Вам понадобилось попыток: ", attempt)

print("\n Ваши очки: ", score)
print("\nCnacибo за игру.")

