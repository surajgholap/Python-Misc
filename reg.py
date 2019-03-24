import re


def main():
    inp = input("Enter the input")
    reg = re.compile('\d+.\d+.\d+.*\d*')
    a = reg.search(inp)
    print(a)

if __name__ == "__main__":
    main()
