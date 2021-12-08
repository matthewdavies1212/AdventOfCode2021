#Open file and read contents
f = open("diveInput.txt")
DiveInput = [line.rstrip() for line in f.readlines()]

#Variables to store x,y coordinates
x = 0
y = 0

#Dependant on the command, track the appropriate movement
for input in DiveInput:
    command = input.split(' ')
    if "forward" in command[0]:
        x += int(command[1])
    else:
        if str(command[0]) == "up":
            y -= int(command[1])
        elif str(command[0]) == "down":
            y += int(command[1])
        else:
            break

print(str.format("X is {0} and Y is {1}", x,y))
print(str.format("Final result is: {0}", x * y))