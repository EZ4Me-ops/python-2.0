import random
while True:
    name=input("what is your full name? ")
    nameparts=name.split(" ")
    print(nameparts)
    if len(nameparts)<2:
        print("enter your full name")
        continue

    firstname=nameparts[0]
    lastname=nameparts[-1]
    # print(firstname)
    # print(lastname)
    username1=lastname+firstname
    # print(username1)
    username2=lastname[:3]+firstname[:3]
    # print(username2)
    username3=firstname[:3]+lastname[-3:]
    # print(username3)
    username4=firstname+str(random.randint(1,10))
    print (username4)

    # usernames=[username1,username2,username3]
    # username=random.choice(usernames)
    # print(username )




