#Open file and read contents
f = open("diveInput.txt")
DiveInput = [line.rstrip() for line in f.readlines()]

#Variables to store x,y coordinates along with the submarine's aim
x = 0
y = 0
aim = 0

#Dependant on the command, track the appropriate movement and modify the submarine's aim
for input in DiveInput:
    command = input.split(' ')
    if "forward" in command[0]:
        x += int(command[1])
        y += int(command[1]) * aim
    else:
        if str(command[0]) == "up":
            aim -= int(command[1])

        elif str(command[0]) == "down":
            aim += int(command[1])
        else:
            break

print(str.format("X is {0} and Y is {1}", x,y))
print(str.format("Final result is: {0}", x * y))