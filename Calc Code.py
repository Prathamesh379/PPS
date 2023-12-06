def lines(some_number):
    print()
    print("-"*some_number)

# Code for basic calculater
lines(100)
num1=int(input("\nEnter Your First Number: "))
num2=int(input("\nEnter Your secound Number: "))
lines(100)
        
while True:
    try: 
        print("\nSelect Your Operation")
        print("1 For ADDITION")
        print("2.For SUBTRACTION")
        print("3.For MULTIPLY")
        print("4.For DIVISION")
        lines(100)
        operation=int(input("\nEnter Number given to each operation: "))


        if operation == 1 :
            num3=num1+num2
            print("\nThe sum is", num3)
            lines(100)
            break
        elif operation == 2 :
            num3=num1-num2
            print("\nSubtraction is",num3)
            lines(100)
            break
        elif operation == 3 :
            num3=num1*num2
            print("\nThe multipication is", num3)
            lines(100)
            break
        elif operation ==4 :
            num3=num1/num2
            print("\nThe Division is",num3)
            lines(100)
            break
        else:
            print("\nPlease, Enter valid operation Value from 1 to 4")
            lines(100)
    
    except:
        continue
