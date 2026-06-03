dictionary={}

while True:
    print("mini dictionary App") 
    print("1.add/update a word")
    print("2.Retrive a word definiton")
    print("3. delete a word")
    print("4.view all words")
    print("5.exit")

    choice=input("choose a option (1-5)") 

    if choice=="1":
        word=input("enter a word-")
        definition=input("enter a definiton-")
        dictionary[word]=definition
        print (dictionary)

    
    

