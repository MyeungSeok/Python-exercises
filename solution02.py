def findAlphabet(string):

    answer = ""
    for i in string:
        if(i.isalpha()):
            answer = answer + i

    print(answer)


file = open('prob02_text.txt', 'r')
string = file.read()
file.close()

findAlphabet(string)
