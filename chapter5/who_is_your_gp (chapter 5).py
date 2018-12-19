# Игра "Кто твой дед"
'''
Доработайте программу «Кто твой папа?» так, чтобы можно было, введя имя человека, узнать, кто его дед.
Программа должна по-прежнему пользоваться одним словарем с парами «сын отец». Подумайте, как включить в этот словарь несколько поколений.
-


'''

print("Привет. Это игра \"Кто твой дед\"\n ")

son_father = {
	"son1" : ("father1", "grandfather1"),
	"son2" : ("father2", "grandfather2"),
	"son3" : ("father3", "grandfather3"),
	"son4" : ("father4", "grandfather4")
}

print('Пары сын - отец\n')

print(
	'''
	Выберите режим игры:
	0 - выход
	1 - найти батю
	2 - найти деда
	'''
	)

choice = input("\nВаш выбор: ")

'''
#Выводим словарь на экран
for keys, values in son_father.items():
	print(keys, "-", values[0], "-", values[1])
'''
# Находим отца
if choice == "1":
	son_name = input("\nНазовите имя сына, а я скажу, кто его отец: ")
	while son_name == "":
		son_name = input("\nНазовите имя сына, а я скажу, кто его отец: ")

	if son_name in son_father:
		print("\nОтец: ", son_father[son_name][0])
	else: 
		print("\nУ ", son_name, " нет отца :(")

# Находим деда
if choice == "2":
	son_name = input("\nНазовите имя сына, а я скажу, кто его дед: ")
	while son_name == "":
		son_name = input("\nНазовите имя сына, а я скажу, кто его дед: ")

	if son_name in son_father:
		print("\nДед: ", son_father[son_name][1])
	else: 
		print("\nУ ", son_name, " нет деда :(")

if choice == "0":
	print("\nДо свидания")










