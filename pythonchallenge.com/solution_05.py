from pickle import load

with open("banner.p", "rb") as f:
    data = load(f)

print(data)

for i in data:
    for tup in i:
        print(tup[0]*tup[1], end="")
    print()
