import json
from utils import w3, get_contract, to_wei
from config import ERC20_TOKEN_ADDRESS, WALLET_PRIVATE_KEY, WALLET_ADDRESS, GAS_LIMIT, GAS_PRICE_GWEI, AMOUNT_TO_SEND

# Minimal ERC-20 ABI
ERC20_ABI = json.loads('[{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"type":"function"}]')

def send_airdrop(recipients):
    contract = get_contract(ERC20_TOKEN_ADDRESS, ERC20_ABI)
    nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
    gas_price = w3.to_wei(GAS_PRICE_GWEI, 'gwei')
    txs = []

    for i, address in enumerate(recipients):
        tx = contract.functions.transfer(address, to_wei(AMOUNT_TO_SEND)).build_transaction({
            'chainId': 1,
            'gas': GAS_LIMIT,
            'gasPrice': gas_price,
            'nonce': nonce + i,
        })
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=WALLET_PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"🚀 Sent to {address} — tx hash: {tx_hash.hex()}")
        txs.append(tx_hash.hex())

    return txs
