#Task 2:
#В научном институте Василия работают 5 профессоров. Помогите написать функцию Василию для расчета максимальной разницы в зарплатах у этих профессоров.

#Пример работы:
#Вводит 400, 900, 300, 555, 787 - Выводит 600
#Вводит 345, 346, 300, 543, 600 - Выводит 300

inputList = []

for i in range(1,6):
    inputList.append(int(input(i)))

result = max(inputList) - min(inputList)

print("Результат", result)

