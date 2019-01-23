from PIL import Image
from re import findall


img = Image.open("./oxygen.png")

width = img.size[0]
height = img.size[1]/2

pixels = []
for i in range(0, width, 7):
    pixels.append(img.getpixel((i, height)))

print(pixels)

result = ""
for r, g, b, a in pixels:
    if(r == g == b):
        result = result + chr(r)
print(result)

# convert ascii code to text
print("".join(map(lambda x: chr(x), map(lambda x: int(x), findall("(\\d+)", result)))))
