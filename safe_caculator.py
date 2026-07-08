while True:

    try:
        num1=int(input("type one number"))
        num2=int( input("type one number"))
    except:
        print("invalid number pls try agian")
        continue

    operator=input("write a operator like +,-,x,/")

    try:
        
        if operator=="+":
            one=num1+num2
            print(one)

        elif operator=="-":
            two=num1-num2
            print(two)

        elif operator=="x":
            three=num1*num2
            print(three)

        elif operator=="/":
            four=num1/num2
            print(four)
        else:
            raise ValueError()
        
    except ZeroDivisionError:
        
        print("cannot divide by zero")
        continue

    except ValueError:
        print ("select a valid operator")
        continue

    stop=input(" do you really wanna stop") 
    if stop=="yes":
        break