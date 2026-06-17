print("temperature converter")

def c_f(c):
    f=c*1.8+32
    print(f)


def f_c(f):
    c=(f-32)/1.8
    print(c)

while True:
    print("temperature converter")
    print("1.celsius to fahrenheit")
    print("2.fahrenhiet to celsius")
    print("3.exit")

    choice=input("chose option 1-3")

    if choice=="1":
        ask=float(input("what temp you wanna covert?"))
        c_f(ask)

    elif choice=="2":
        ask=float(input("what temp you wanna covert?"))
        f_c(ask)
    elif choice=="3":
        break
