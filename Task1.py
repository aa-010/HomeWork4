#Task 1:
#Василий давно занимается математическими аномалиями. Сейчас ему открылся новый способ анализа чисел - берется натуральное число и считается сумма всех его чисел на которое это число делится без остатка(т.е. делителей). Василий хочет автоматизировать эту процедуру. Напишите функцию, которая облегчит его изыскания.

#Пример работы:
#Вводит 6 - Выводит 12
#Вводит 10 - Выводит 18

n = int(input("Введите число\n"))
i = 1
resultList = []

while i*i <= n:
    if n%i == 0:
        if i == n//i:
            resultList.append(i)
        else:
            resultList.append(i)
            resultList.append(n//i)
    i+=1

resultList.sort()
sum = 0
for i in resultList:
    sum = sum + i
print(resultList)
print(sum)
