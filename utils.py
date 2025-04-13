from web3 import Web3
from config import INFURA_URL

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def get_contract(address, abi):
    return w3.eth.contract(address=Web3.to_checksum_address(address), abi=abi)

def to_wei(amount):
    return w3.to_wei(amount, 'ether')

def from_wei(amount):
    return w3.from_wei(amount, 'ether')
