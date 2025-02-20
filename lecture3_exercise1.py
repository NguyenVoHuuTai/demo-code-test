total = 0
for i in range(3,100,2):
    total = total + 1/i**i
one_over_the_total = 1/total
print("The result is: ",round(one_over_the_total, 2))

