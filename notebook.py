import csv
def spisok1():
    print("===Меню===")
    print("1.Показать список")
    print("2.Выход из программы")
    print("3.Добавить новый продукт")
    print("==============") 
# Открываем файл с автоматическим закрытием после блока
data = []
with open('list.csv', 'r', encoding="utf-8") as file:
    content = csv.reader(file)
    data = list(content)      
# Файл уже закрыт
print(data)
# Когда переменную вызывают, обычно, ей сразу присваивают какие то данные
#cat_name = "Арчи"
box = []
menu = True
menu_number = 0

# цикл while (вайл)
while  menu:  
    spisok1()
    menu_number = input("выберите опцию: ")
    menu_number = int(menu_number)
    if(menu_number == 1):    
        for index,element in enumerate(data):
          pravda = False
          galochca = ""
          if(element[1] == "True"): 
              pravda = True
          if pravda:
              galochca = "☑️"     
          if not pravda:
              galochca = "🔲"             
          print(galochca + " " + element[0])
          
          
        
    if(menu_number == 2):
        menu = False
        print('=====КОНЕЦ=====')
    if(menu_number == 3):
        spisok = input("введите задачу: ")
        content.append(spisok)


        with open('list.txt', 'w', encoding='utf-8') as file:
            for element in content:
                file.write(element + "\n")  
            
        