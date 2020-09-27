def replace_word(string, old, new):
    """new word replaces the old word in the string.

    Arguments:
        string {str} -- [description]
        old {str} -- [description]
        new {str} -- [description]
    """
    words = string.split(" ")
    for i in range(len(words)):
        if words[i] == old:
            print(i)
            words[i] = new
            # print(i)
    return " ".join(words)


text = "I like cats. Tom is my favorite cat ."
print(replace_word(text, "cat", "dog"))
print(text.replace("cat", "dog"))
