# opening file in write mode
file=open("Anime.txt","w")

# write in the file
file.write("two plus two equals nine trust\n")
file.write("my fav anime is jjk\n")
file.close()

# opening file in write mode
file=open("Anime.txt","w")

# write in the file
file.write("twotwo equals nine trust\n")
file.write("my fav\n")
file.close()








# opening file in append mode
file=open("Anime.txt","a")

# write in the file
file.write("twotwo equals nine trust\n")
file.write("my fav\n")
file.close()
















# opening file in read mode
file=open("Anime.txt","r")

# reading from a file
daata=file.read()
file.close()
print(daata)




















