# Игра "Кто твой папа"
'''
Напишите программу «Кто твой папа?», в которой пользователь будет вводить имя человека, а програм­ма - называть отца этого человека. Чтобы было интереснее, можно «научить» программу родственным отношениям среди литературных персонажей, исторических лиц и современных знаменитостей. Предоставьте пользователю возможность добавлять, заменять и удалять пары «СЫН - отец».
'''

print("Привет. Это игра \"Кто твой Папа\"\n ")

son_father = {
	"son1" : "father1",
	"son2" : "father2",
	"son3" : "father3",
	"son4" : "father4"
}

print('Пары сын - отец\n')


#Выводим словарь на экран
for keys, values in son_father.items():
	print(keys, "-", values)


son_name = input("\nНазовите имя, а я скажу, кто его отец: ")
while son_name == "":
	son_name = input("\nНазовите имя, а я скажу, кто его отец: ")

if son_name in son_father:
	print("\nОтец: ", son_father[son_name])
else: 
	print("\nУ ", son_name, " нет отца :(")





