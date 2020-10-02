def check(x):
    if x == 1 or x ==2 or x ==3:
        print('Yes')
    elif x != 2 or x != 3:
        print("also true")

    elif x in (2, 3) or x in (5, 4):
        print("Here")

    elif (
        x == 10
        or x == 20
        or x == 30
        and x == 40
    ):
        print("Why even?")

    elif (
        x == 10
        or x == 20
        or x == 30
    ):
        print("Why even?")
