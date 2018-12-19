import random

WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)

print("\n", word, "\n")

print("В слове ", len(word), " букв")

correct = input("\nОтгадайте слово: ")



number_of_letter = 0

'''
def letter_in_word():
	for i in range(len(word)):
		if letter == word[i]:
			number_of_letter += 1 
	if number_of_letter > 0:
		print("\nДа, в слове ", number_of_letter, " буква ", letter)
	else:
		print("\nНет")

'''
while correct != word:
	print("\nОтвет неверный")
	hint = input("\nДать подсказку? ")
	if hint == "Да" or hint == "да":
		letter = input("\nУгадайте, есть ли в слове буква ")
		for i in range(len(word)):
			if letter == word[i]:
				number_of_letter += 1 
		if number_of_letter > 0:
			print("\nДа, в слове ", number_of_letter, " буква ", letter)
			number_of_letter = 0
		else:
			print("\nНет")	
	else:
		correct = input("\nОтгадайте слово: ")	




print("\nПоздравляю, вы угадали слово")
		


	


'''
def hint():
	hint = input("\nДать подсказку? ")
	if hint == "Да" or hint == "да":
		letter = input("\nУгадайте, есть ли в слове буква ")
		letter_in_word()
'''			




