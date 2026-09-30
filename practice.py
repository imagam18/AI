month = int(input("Enter the number of month:"))
day = 2
match day:  
    case 1|2|3|4|5|6|7 if month == 5:
        print("A week of may")
    case 1|2|3|4|5|6|7 if month == 6:
        print("A week of June")
    case _:
        print("Don't have answer")