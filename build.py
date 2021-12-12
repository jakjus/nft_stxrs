import png
import random
import numpy as np
import io, json

folder = "generated_images/"
metadata_folder = "generated_metadata/"
amount = 10000
size = (16, 16)

# Do you remember the sky when we first met? ... What?     Oh

full = []


mdtemplate = {
                 "description": "*", 
                 "image": "ipfs://URI/1.png", 
                 "name": "*",
                 "attributes": [], 
             }

i = 0

def getArray():
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

def getBinaryStars(img):
    diag = img[:-1,:-1]*img[1:,1:]
    diag2 = img[1:,:-1]*img[:-1,1:]
    bs = diag.sum()+diag2.sum()
    return bs

def getAlignedStars(img):
    horiz = img.sum(axis=0)
    vert = img.sum(axis=1)
    return np.max([horiz.max(), vert.max()])

def getStars(img):
    return img.sum()

def binaryPrint(img):
    print(img.astype(int))

def getOuterCircle(img):
    if img[4:-4,4:-4].sum() == 0:
        return True
    else:
        return False

def getCentered(img):
    if img[5:-5,5:-5].sum() == img.sum():
        return True
    else:
        return False

def getMetadata(image):
    img = np.array(image)
    img = img == 255
    binaryStars = getBinaryStars(img)
    stars = getStars(img)
    maxAlignedStars = getAlignedStars(img)
    outerCircle = getOuterCircle(img)
    centered = getCentered(img)
    return {'stars': stars, 'binaryStars': binaryStars, 'maxAlignedStars': maxAlignedStars, 'outerCircle': outerCircle, 'centered': centered}

def generateMetadata(md):
    fullmd = mdtemplate
    fullmd['name'] = '** '+str(i+1)+' **'
    fullmd['image'] = ipfsURI+str(i+1)+'.png'
    fullmd['attributes'] = []
    fullmd['attributes'].append({"trait_type": "Stars", "value": str(md['stars'])}) 
    fullmd['attributes'].append({"trait_type": "Binary Stars", "value": str(md['binaryStars'])}) 
    fullmd['attributes'].append({"trait_type": "Max Aligned Stars", "value": str(md['maxAlignedStars'])}) 
    if md['outerCircle']:
        p = 'Outer Circle'
    elif md['centered']:
        p = 'Centered'
    else:
        p = 'Scattered'
    fullmd['attributes'].append({"trait_type": "Characteristic", "value": p}) 
    with io.open(metadata_folder+str(i+1)+".json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(fullmd, ensure_ascii=False))

def generateFile(array):
    png.from_array(array, 'L').save(folder+str(i+1)+".png")

while i < amount:
    array = getArray()
    array = invert(array)
    if array in full:
        continue
    full.append(array)
    generateFile(array)
    i = i+1

ipfsCode = input('\nPut IPFS code of uploaded images without slashes, colons or "ipfs":\n')

ipfsURI = "ipfs://"+ipfsCode+"/"

for i, array in enumerate(full):
    meta = getMetadata(array)
    generateMetadata(meta)
