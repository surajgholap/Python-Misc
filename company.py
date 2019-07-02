S = 'John Do-e; John Do-e; Peter Benjamin Parker; Mary Jane Watson-Parker;\
 John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker'
C = 'Example'


def solution(S, C):
    # write your code in Python 3.6
    comp = C.lower()
    listOfEmp = S.split("; ")
    # print(listOfEmp)
    new = []
    new2 = []
    for i in listOfEmp:
        i = i.lower()
        i = i.replace("-", "")
        newlis = i.split(" ")
        temp = "<"+newlis[0]+newlis[-1]
        temp1 = temp
        count = 2
        while temp in new:
            temp = temp1
            temp = temp + str(count)
            count += 1
        new.append(temp)
        temp = temp + "@" + comp + ".com>"
        new2.append(temp)
    # print(new)
    final = []
    for i, j in zip(listOfEmp, new2):
        final.append("{} {}; ".format(i, j))
    print("".join(final))


solution(S, C)
