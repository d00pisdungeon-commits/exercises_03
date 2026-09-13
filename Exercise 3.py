def rectangle(text, width, height):
    row = (text *width)[:width]
    for _ in range(height):
        print(row)
# these were my know nothing attempts, I think that it is feeding back into the range instead of using the range as a boundary
    #for i in range(1, height):
    #    horizontal = text * i
     #   vertical = text * height
      #  print (horizontal + vertical)

rectangle("L", 4, 6)