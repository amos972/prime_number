primenumber = []
for i in range(1, 1001):
    if i > 1:
        for j in range(2, i):
            if (i%j)==0:
                break
        else:
            primenumber.append(i)
print(primenumber)