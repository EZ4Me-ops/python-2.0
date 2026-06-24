import datetime

title=input("what is the name of your journal? ")
title=title+".txt"

def add_entry():
    ask=input("what do you want to write? ")
    timeee=datetime.datetime.now()
    date=timeee.strftime("%d-%b-%Y %I:%M:%S %p")
    file=open(title,"a")
    file.write(date+"  "+ask+"\n")
    file.close()

def view_entry():
    file=open(title,"r")
    daataa=file.read()
    file.close()
    print(daataa)

while True:
    
    print("1.add journal ")
    print("2.view entry ")
    print("3.exit ")

    option=input("what you wanna open'1-3' ")

    if option=="1":
        add_entry()

    elif option=="2":
        view_entry()

    elif option=="3":
        break 

