from urllib.request import urlopen
from re import findall

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022/"
while(True):
    with urlopen(url) as f:
        string = str(f.read(200))
        print(string)

    nextNum = findall("the next nothing is ([0-9]+)", string)

    if(nextNum):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nextNum[0] + "/"
    else:
        print("exit")
        break
