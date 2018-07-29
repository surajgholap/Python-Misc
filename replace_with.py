import re


seaString = """Berserk Guts is full of rage """
searchReg = re.compile(r'Berserk \w+')  # Regular expression
repString = searchReg.sub(r'Berserk Dog', seaString)  # Replace first string value in seaString
print(repString)
