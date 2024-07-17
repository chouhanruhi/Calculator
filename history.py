def add_file(entry):
    file = open('History.txt',"a")
    file.write(entry + "\n")

#shows the history upom command


def show():
    file = open('History.txt', "r")
    history = file.readlines()
    try:
        if history:
            print("History:")
            for line in history:
                print(line.strip())
        else:
            print("No History found!")
    except Exception as e:
        print(f"an error occured while reading history:{e}")

def opp():
    ree = True
    while ree is True:
        enter = input("choose from the options:")
        try:
            Entery = int(enter)
            if Entery == 8:
                show()
            else:
                ree = False
                return Entery
        except ValueError:
            print("wrong input! Try again")


