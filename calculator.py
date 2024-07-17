import history as H

riya = True
print("1-Addition \n2-Substraction\n3-Division\n4-Multiplication\n5-power to\n6-Rounding\n7-Remaining\n8-Show History\noo-Exit")

while riya is True:
    oppe = H.opp()
    if oppe == 0:
        exit()
    First = int(input("Enter the First Digit:"))
    if First == 00:
        print("Closing the app")
        exit()
    Sec = int(input("Enter the sec digit:"))
    if Sec == 00:
        print("Closing the app")
        exit()
    if oppe == 1:
        Sum = First + Sec
        Total = f"{First}+{Sec}={Sum}"
        H.add_file(Total)
        print(Sum)
    elif oppe == 2:
        Sum = First - Sec
        Total = f"{First}-{Sec}={Sum}"
        H.add_file(Total)
        print(Sum)
    elif oppe == 3:
        Sum = First / Sec
        Total = f"{First}/{Sec}={Sum}"
        H.add_file(Total)
        print(Sum)
    elif oppe == 4:
        Sum = First * Sec
        Total = f"{First}/{Sec}={Sum}"
        H.add_file(Total)
        print(Sum)
    elif oppe == 5:
        Sum = First ** Sec
        Total = f"{First}^{Sec}={Sum}"
        H.add_file(Total)
        print(Sum)
    elif oppe == 6:
        Sum = First // Sec
        Total = f"{First}//{Sec}={Sum}"
        H.add_file(Total)
        print(Sum)
    elif oppe == 7:
        Sum = First % Sec
        Total = f"{First}%{Sec}={Sum}"
        H.add_file(Total)
        print(Sum)
    else:
        print("Wrong input")



