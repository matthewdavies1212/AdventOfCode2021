#Variable to hold the number of increased values
increasesInValue = 0

#Open file and read contents
f = open("sonarInput.txt")
sonarInput = f.readlines()
sonarInts = [int(i) for i in sonarInput]

#Compare each value to the one prior to it. If it is larger, increment the increasesInValue variable then print the result
i = 1
while i < len(sonarInput):
    if sonarInput[i] > sonarInput[i-1]:
        increasesInValue += 1

    i += 1
print("The number of increases in depth is %s" %increasesInValue)

