i = int(input("input: "))
j = 1
sum = 0;
while j <= i:
    sum += j
    if j == 1:
        string = str(j) + '+'
    elif j <= i - 1:
        string = string + str(j) + '+'
    else:
        string = string + str(j)
    j += 1
print(f"formula: {string}")
print(f"output: {sum}")
