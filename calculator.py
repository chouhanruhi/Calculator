riya = True
print("1-Addition \n2-Substraction\n3-Division\n4-Multiplication\n5-power to\n6-Rounding\noo-Exit")

while riya is True:
    First = int(input("Enter the first digit"))
    if First == 00:
        print("Closing the app")
        exit()
    Sec = int(input("Enter the sec digit:"))
    if Sec == 00:
        print("Closing the app")
        exit()
    opp = int(input("Enter the Operator:"))
    if opp == 1:
        Sum = First + Sec
        print(sum)
    elif opp == 2:
        Sum = First - Sec
        print(sum)
    elif opp == 3:
        Sum = First / Sec
        print(sum)
    elif opp == 4:
        Sum = First * Sec
        print(sum)
    elif opp == 5:
        Sum = First ** Sec
        print(sum)
    elif opp == 6:
        Sum = First // Sec
        print(sum)
    elif opp == 7:
        Sum = First % Sec
        print(sum)
    elif opp == 00:
        riya  = False
        print("Closing the app")
    else:
        print("Wrong input")



