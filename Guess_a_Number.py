'''
Start
1. Select a random number in a range (A)
2. Accept  user input (B)
3. Check if A == B, if true, user has won, end. If false, move to next step
4. If A > B, let user know, reduce chances by 1
5. If A < B, let user know, reduce chances by 1
6. Repeat steps 2 - 5 until chances == 0
7. Let the user know they've exhausted all their chances, games over
End
'''

from random import randrange
a, b = 0, 20
C = 5
A = randrange(a, b)
print("Directions")
while C > 0:
    print("Please enter a guess for the number between",a," and ",b,": ")
    B = int(input())
    if A == B:
        print("You Win!")
        break
    elif A > B and a < B < b:
        print("Too Low")
        C -= 1
    elif A < B and a < B < b:
        print("Too High")
        C -= 1
    else:
        print("Out of range")
        C -= 1
if C == 0:
    print("The correct answer was ",A)
    print("Chances all used up")
print("game over")