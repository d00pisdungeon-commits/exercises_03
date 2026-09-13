def bottle_verse(number):
    if number > 2:
        print(f"{number} bottles of beer on the wall, {number} bottles of beer.")
        print(f"Take one down and pass it around, {number - 1} bottles of beer on the wall.")
    elif number == 2:
        print(f"2 bottles of beer on the wall, {number} bottles of beer.")
        print(f"Take one down and pass it around, 1 bottle of beer.")
    elif number == 1:
        print(f"1 bottle of beer on the wall, {number} bottle of beer.")
        print(f"Take one down and pass it around, no more bottles of beer on the wall.")
    elif number == 0:
        print(f"No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, 99 bottles of beer on the wall.")

bottle_verse(2)

#else if and the function defining line of text with variable input is important here