import sys
from PIL import Image, ImageOps

format = ['.jpg','.jpeg','.png']
index1 = sys.argv[1].find('.')
index2 = sys.argv[2].find('.')


if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif (sys.argv[1][index1:] in format) == False or (sys.argv[2][index2:] in format == False):
    sys.exit('Invalid file-format')
elif sys.argv[1][index1:] != sys.argv[2][index2:]:
    sys.exit('Different file-format')


shirt = Image.open('shirt.png')
shirt_size = shirt.size

try:
    image1 = ImageOps.fit(Image.open(sys.argv[1]), size = shirt_size)
except FileNotFoundError:
    sys.exit('File not found')
image1.paste(shirt,shirt)
image1.save(sys.argv[2])
print(image1.size)
