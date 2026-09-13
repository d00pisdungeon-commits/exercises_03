def triangle(text, height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        block = text * i
        print(block + spaces)

triangle("H", 6)

def triangle01(char, level):
    for i in range(level):
        print(char*(i+1))

triangle01("H", 6)

# the first parameter is the text, the second is the height
# range runs from two given points, so 1 to the height + 1 to account for 0
# adding the line about text times i is same as writing function as one line