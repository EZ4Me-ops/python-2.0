import random
grid=[["-"for i in  range(5)]for a in range(5)]
print("welocome to my hunt!!!!!!!!!!!!")

treasurerow=random.randint(0,4)
treasurecollum=random.randint(0,4)

attempt=0
while True:
    print("ths is the curent grid")
    for row in grid:
        for item in row:
            print(item,end=" ")
        print()
    try:
        row=int(input("inpt a row number frm 0-4"))
        colllm=int(input("inpt a colum number from 0-4"))
    except:
        print("select a number between 0-4")
        continue

    if row not in range (5) or colllm not in range (5):
        print("sry man choose somthing else it doesnt iffit in the code sry ")
        continue

    attempt=attempt+1
    
    if row==treasurerow and colllm==treasurecollum:
        print("good job you found it in ",attempt,"attempts")
        break
    else:
        print("cry about it try again")
        grid[row][colllm]="x"

    