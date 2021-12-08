#Variable to hold the number of increased values and previous set value
increasesInValue = 0
currentSet = []

#Open file and read contents
f = open("sonarInput.txt",)
sonarInput = f.readlines()
sonarInts = [int(i) for i in sonarInput]

#Compare each set with the next and increase the variable if the new set is larger
for i in range(len(sonarInts)):
    set1 = sum(sonarInts[i:i+3])
    set2 = sum(sonarInts[i+1:i+4])

    #Ensure the new set is at least 3 items
    if len(sonarInts[i+1:i+4]) < 3:
        break

    if set2 > set1:
        increasesInValue += 1

print("The number of increases in depth is %s" %increasesInValue)

