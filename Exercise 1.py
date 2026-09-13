def print_right01(text):
    # calculate putting the final character in the 40th column
    spaces = 40 - len(text)
    # print the spaces followed by the text
    print(" " * spaces + text)

print_right01("Hello World")
print_right01("Hello World")
print_right01("Hello World")
print_right01("Hello World I love you")