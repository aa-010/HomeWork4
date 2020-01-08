inputString = input("Введите строку\n")
resulString = []

coutnEntry = 0
boolResult = False

for i in range(len(inputString)):

    if inputString[i+1] == "B" and inputString[i+2] == "8":

        resulString.append(inputString[i+1])
        resulString.append(inputString[i+2])
        coutnEntry += 1
        i+2
        continue

    elif inputString[i+1] == "8" and inputString[i+2] == "B":

        resulString.append(inputString[i+1])
        resulString.append(inputString[i+2])
        coutnEntry += 1
        i+2
        continue


if (coutnEntry >= int(inputString[0])):
    boolResult = True

print(coutnEntry)
#resulString = ''.join(resulString)
print(resulString, boolResult)