cars={"toyota":"supra", "ford":"f150", "ferrari":"spyder","lamborgini":"aventador",}
print(cars)
# get keys
print(cars.keys())
# get values
print(cars.values())
# get value using key
print(cars["ford"])
# get all items
for i in cars:
    print(i,"_",cars[i])

# add items
cars["GMC"]="Gimmy"
print(cars)

# update item
cars["GMC"]="jimmy"
print(cars)

# remove item
del cars["GMC"]
print(cars)

# check if a key exicts
print("ferrari" in cars)  
print("ferrari" not in cars)  