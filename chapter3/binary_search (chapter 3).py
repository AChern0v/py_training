print("Сейчас этот компудахтер будет отгадывать число, которое ты введёшь\n")
x = int(input("Вводи: "))

# Создаём и заполняем список

list = []
i = 1


while i <= 100:	
	list.append(i)
	i += 1

# Счётчик попыток
attempt = 0
start = 0
end = len(list) - 1
m = int(end / 2)

while list[m] != x and start < end:
	attempt += 1
	if x > int(list[m]):
		start = m + 1
	else:
		end = m - 1
	m = int((start + end) / 2)
	

if start > end:
	print("\nКомпудахтер понял, что числа нет в массиве")
	print("\n Ему понадобилось ", attempt, " попыток")
else:
	print("Компудахтер отгадал число! Это: ", list[m])
	print("\n Ему понадобилось ", attempt, " попыток")
		
	
