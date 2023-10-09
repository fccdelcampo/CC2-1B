i = 5

while i >= 1:
    j = 1
    if i <= 5:
        while j < i:
            print(str(j), end=" ")
            j += 1
        if j == i:
            print(str(j))
    i -= 1
