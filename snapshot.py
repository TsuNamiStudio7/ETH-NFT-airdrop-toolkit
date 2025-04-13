import json
from utils import w3, get_contract
from config import NFT_CONTRACT_ADDRESS

# Minimal ERC-721 ABI (only the needed parts)
ERC721_ABI = json.loads('[{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"name":"owner","type":"address"}],"type":"function"}]')

def get_nft_holders():
    contract = get_contract(NFT_CONTRACT_ADDRESS, ERC721_ABI)
    total = contract.functions.totalSupply().call()
    holders = set()
    print(f"📦 Total NFTs: {total}")
    for token_id in range(total):
        try:
            owner = contract.functions.ownerOf(token_id).call()
            holders.add(owner.lower())
        except:
            continue
    return list(holders)

if __name__ == "__main__":
    addresses = get_nft_holders()
    print(f"✅ Found {len(addresses)} unique holders")
