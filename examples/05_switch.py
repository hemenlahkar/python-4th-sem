a = 0

while a < 1 or a > 12:
    a = int(input("Enter the month number: "))

match a:
    case 1:
        result = "January"
    case 2:
        result = "February"
    case 3:
        result = "March"
    case 4:
        result = "April"
    case 5:
        result = "May"
    case 6:
        result = "June"
    case 7:
        result = "July"
    case 8:
        result = "August"
    case 9:
        result = "September"
    case 10:
        result = "October"
    case 11:
        result = "November"
    case 12:
        result = "December"
        
print("Entered Month is ", result)