print("мой ноутбук")
print("==============")


# Когда переменную вызывают, обычно, ей сразу присваивают какие то данные
#cat_name = "Арчи"
box = input("введите задачу: ")
print(box)
menu = True
menu_number = 0
# 1. напечатать снайперскую винтовку

# цикл while (вайл)
while  menu:
    menu_number = input("выберите опцию: ")
    menu_number = int(menu_number)
    if(menu_number == 1):
        print(box)
    if(menu_number == 2):
        menu = False
        print('=====КОНЕЦ=====')