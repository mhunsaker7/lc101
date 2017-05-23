def counting_characters(text):
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
            
    keys = char_count.keys()
    for char in keys:
        print(char + ": " + str(char_count[char]))

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
counting_characters(text)