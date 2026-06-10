print("temperature converter")

def c_f(c):
    f=c*9/5+32
    print(f)





def f_c(f):
    c=f-32*5/9
    print(c)

while True:
    print("temperature converter")
    print("1.celsius to fahrenheit")
    print("2.fahrenhiet to celsius")
    print("3.exit")

    if input=="1":
        ask=input("what temp you wanna covert?")
        c_f(ask)

    elif input=="2":
        ask=input("what temp you wanna covert?")
        f_c(ask)
    elif input=="3":
        break
