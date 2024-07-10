try:
    numerator =int(input("enter a number to divide"))
    denominator =int(input("enter a number to divide by:"))
    result=numerator/denominator
    print(result)
# handling multiple exception
except ZeroDivisionError:
    print("you can't divide any number by zero!!!")
except Exception:
    print("Something fishy :)")