#creating the 4 x 5 2D list intialized at 0
four_five = [[0 for i in range(5)] for i in range (4)]

#replacing 0s with randomly generated numbers in range 0-10 from module random
from random import randint
for i in range(len(four_five)):
    for j in range(len(four_five[0])):
        four_five[i][j] = randint(0,10)
        print(four_five[i][j], end ='\t')
    print()

print("\nMultiplying each element by 7.2...\n")

#multiplying each element by 7.2
for i in range(len(four_five)):
    for j in range(len(four_five[0])):
        four_five[i][j] *= 7.2
        print(f'{four_five[i][j]:.2f}', end ='\t')
    print()




        