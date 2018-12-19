# Возвращает перевернутый текст

word = input("Введите слово, и я переверну его: ")

'''
output = len(word) - 1

for i in range(output + 1):
	print(word[output - i])
'''
print(word[::-1]) # word[begin:end:step]
