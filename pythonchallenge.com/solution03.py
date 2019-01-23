from re import findall


# my idea
def findAlphabet(string):
    answer = ""
    for i, c in enumerate(string):
        if(3 <= i < len(string)-3):
            count = 0

            for j in range(1, 4):
                if(c.islower()):
                    if(string[i-j].isupper() and string[i+j].isupper()):
                        count = count+1
                    else:
                        break

            if(count == 3):
                if (string[i - 4].islower() and string[i + 4].islower()):
                    answer = answer + c

    print(answer)


# solution using regular expression
def findAlphabet2(string):
    answer = "".join(findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", string))
    print(answer)


file = open("prob03_text.txt", "r")
string = file.read()
file.close()

findAlphabet(string)
findAlphabet2(string)
