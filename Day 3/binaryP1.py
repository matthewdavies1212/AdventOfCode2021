#Open file and read contents
f = open("binaryInput.txt")
binaryData = [line.rstrip() for line in f.readlines()]

#Couldn't get 2D array working in python so rework the arrays to make finding the most common number easier
reformedData = [''] * len(binaryData[0])
i = 0
for data in binaryData:
    for i in range(0,len(data)):
        reformedData[i] += data[i]


mostCommon = []
leastCommon = []
#Calculate most common and least common binary digits
for results in reformedData:
    count1 = 0
    count0 = 0
    for digit in results:
        if digit == "1":
            count1 += 1
        elif digit == "0":
            count0 += 1
        else:
            print("Unknown value")
            break
    
    if count0 > count1:
        mostCommon.append("0")
        leastCommon.append("1")
    else:
        mostCommon.append("1")
        leastCommon.append("0")

#Convert from Binary to decimal
binaryCommon = int(''.join(mostCommon),2)
binaryLeast = int(''.join(leastCommon),2)
print(str.format("Power consumption is {0} * {1} = {2}", binaryCommon,binaryLeast, binaryLeast * binaryCommon))
