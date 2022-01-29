import numpy as np
import io, json

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

def generateMetadata(md, mdtemplate, metadata_folder, i, ipfsURI):
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
