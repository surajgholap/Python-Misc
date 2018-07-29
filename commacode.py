# Function that accepts a list as an argument and gives back
#      string of the list


def commacode(text):
    words = ','.join(text)
    return words


# List and passing it to the function
spam = ['cat', 'rat', 'lat', 'mat', 'bat']
words = commacode(spam)
print(words)
