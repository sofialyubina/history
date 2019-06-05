string = input()

string2 = string.split(" ")
for i in range(len(string2)):
    if string2[i].islower():
        continue
    else:
        result = string2[i]

print(result)
