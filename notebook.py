
# Когда переменную вызывают, обычно, ей сразу присваивают какие то данные
#cat_name = "Арчи"
box = []
menu = True
menu_number = 0
# 1. напечатать снайперскую винтовку

# цикл while (вайл)
while  menu:
    print("===Меню===")
    print("1.Показать список")
    print("2.Выход из программы")
    print("3.Добавить задачу")
    print("==============") 
    menu_number = input("выберите опцию: ")
    menu_number = int(menu_number)
    if(menu_number == 1):
        for index,x in enumerate(box):
            print(str(index + 1) + ": " + x)
    if(menu_number == 2):
        menu = False
        print('=====КОНЕЦ=====')
    if(menu_number == 3):
        spisok = input("введите задачу: ")
        box.append(spisok)