grid=[["-"for i in  range(5)]for a in range(5)]
print("welocome to my hunt!!!!!!!!!!!!")
print("ths is the curent grid")
while True:
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
    