x = 5

match x:
    case 1 | 7 | 9:
        print("Fount 1 ")
    case 2:
        pass
    case 3:
        pass
    case 8:
        print("you input number 8")
    case _:
        print("No match found")

# if (x == 1) or ( x == 7 ) or (x == 9):
#     pass
# elif x == 5:
#     pass
# elif x == 6:
#     pass
# else:
#     pass