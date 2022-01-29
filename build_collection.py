from utils.image import *
from utils.metadata import *

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

while i < amount:
    array = getArray(size)
    array = invert(array)
    if array in full:
        continue
    full.append(array)
    generateCollectionFile(array, folder, i)
    i = i+1

ipfsCode = input('\nPut IPFS code of uploaded images without slashes, colons or "ipfs":\n')

ipfsURI = "ipfs://"+ipfsCode+"/"

for i, array in enumerate(full):
    meta = getMetadata(array)
    generateMetadata(meta, mdtemplate, metadata_folder, i, ipfsURI)
