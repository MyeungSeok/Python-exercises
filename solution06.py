from zipfile import ZipFile
from re import findall


file = ZipFile("./channel.zip")

fileName = "90052.txt"
while(True):
    string = file.read(fileName).decode("utf-8")

    print(string)

    nextNum = findall("Next nothing is ([0-9]+)", string)
    if(nextNum):
        fileName = nextNum[0] + ".txt"
    else:
        print("exit")
        break

# read the zip comments
fileName = "90052.txt"
result = []
while(True):
    string = file.read(fileName).decode("utf-8")
    comment = file.getinfo(fileName).comment.decode("utf-8")

    result.append(comment)

    nextNum = findall("Next nothing is ([0-9]+)", string)
    if(nextNum):
        fileName = nextNum[0] + ".txt"
    else:
        print("exit")
        break

print("".join(result))
