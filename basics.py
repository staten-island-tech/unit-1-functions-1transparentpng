# Integers (numbers)
a = int('5')
bill = input("How much was the bill?")
print(int(bill)* .5)

# Floats (numbers with decimals)
bruh = 3.14

# Lists (store stuff)
names = ["Aiden", "Michael", "bob"]
for person in names:
    print(person) # this prints everything in the index by numerical order (Aiden is 0, Michael is 1, bob is 2)

# Boolean (True or False)
x = True
y = False
# evaluations use == rather than =
if x == True:
    print (f"Yes, x was {x}")
else:
    print("Aw man, x was false. :(")

x1 = 10
y1 = 3
if x1 == 10 and y1 == 5:
    print("WOOHOO")
elif x1 == 9 or y1 == 4: # elif = else if
    print("..yay?")
else:
    print("awwwh..")

# f string to "combine" stuffz
name = input("What is thy name?")
print(f"Ah, hello there sir {name}!")

## little youtuber registry thing, i guess
search = input("Who u lookin for?") # Asks to input the youtuber ur looking for
registry = ["Markiplier", "Jacksepticeye", "Squiddo", "Ashswagg"] # Registered youtubers
for yters in registry: 
    found = False
    if yters == search:
        found = True
    if found == True:
        print(f"Found {search} in the registry!")

    
