import random
import png

def binaryPrint(img):
    print(img.astype(int))

def getArray(size):
    image = []
    image.append([0]*size[0])
    for i in range(size[1]-2):
        row = []
        row.append(0)
        prevPixel = 0
        for j in range(size[0]-2):
            pixel = 0
            if prevPixel == 0 and image[i][j+1] == 0 and random.random() < 0.03:
                pixel = 255
            prevPixel = pixel
            row.append(pixel)
        row.append(0)
        image.append(row)
    image.append([0]*size[1])
    return image

def invert(image):
    if random.random() < 0.5:
        image.reverse()
        for row in image:
            row.reverse()
    return image

def generateCollectionFile(array, folder, i):
    png.from_array(array, 'L').save(folder+str(i+1)+".png")
