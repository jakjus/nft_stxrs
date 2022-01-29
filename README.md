## nft_stxrs
![Banner](example/bg.png)
Random NFT (Non-Fungible Token) generator. Generated images are random white pixels (stars) on a black background (sky).  Stars cannot be adjacent vertically or horizontally, but can be adjacent diagonally (binary stars).

Every generated image is **unique**.

Script generates **images** and **metadata**, compliant with [ERC721 standard](https://docs.opensea.io/docs/metadata-standards). 

By default, *10000* images of size *16x16 pixels* and its metadata. It is adjustable in `build_collection.py`.

> Check the final result on [My OpenSea](https://opensea.io/collection/stxrs)!

### Installation
`pip install -r requirements.txt`

### Usage
`python build_collection.py` - build a NFT collection.
1. During execution, a prompt will ask you to insert IPFS code.
2. Go to IPFS hosting provider, like [Pinata](https://app.pinata.cloud/) and upload already generated folder `generated_images`.
3. Get IPFS URI of the uploaded folder from the Pinata UI. Strip it from "ipfs://" and "/" at the end (according to script instructions).
4. Paste it back into the prompt to continue generating metadata.
5. Done - your images and metadata is generated.

`python build_background.py` - build a background image (`bg.png`) - useful in NFT Markets, like OpenSea, as a Twitter banner or other.

### Blockchain contract
Blockchain contract is not a subject of this repository, but you can look up the custom alteration of ERC721 contract in `contract_data/contract`. It has a few additional features, one of which is the ability to transfer funds from contract's address back to deployer.
