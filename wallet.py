# Import dependencies
import subprocess
import json
import os
from dotenv import load_dotenv
from bip_utils import Bip32, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from web3 import Web3
from bit import wif_to_key
from eth_account import Account
from bit import PrivateKeyTestnet

# Load and set environment variables
load_dotenv()
mnemonic = os.getenv("MNEMONIC")
depth = 3


# Import constants.py and necessary functions from bit and web3
from constants import *

# def get_addresses(mnemonic,coin,depth):
#     seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
#     bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)#ETHEREUM
    
    
#     if coin == 'BTC':
#         bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
#     elif coin == 'ETH':
#         bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(60)
#     elif coin == 'BITCOINTEST':
#         bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(1)
        
        
#     res = []
#     # Generate BIP44 account keys: m/44'/0'/0'
#     # Generate BIP44 chain keys: m/44'/0'/0'/0
#     bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
#     # Generate the address pool (first 20 addresses): m/44'/0'/0'/0/i
#     for i in range(20):
#         bip_obj_addr = bip_obj_chain.AddressIndex(i)
#         res.append(bip_obj_addr.PublicKey().ToAddress())
    
#     return res[0:depth]

def get_addresses(mnemonic,coin,depth):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    if coin == 'BTC':
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
    elif coin == 'ETH':
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(60)
    elif coin == 'BITCOINTEST':
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(1)
    res = []
    # Generate BIP44 account keys: m/44'/0'/0'
    # Generate BIP44 chain keys: m/44'/0'/0'/0
    bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
    # Generate the address pool (first 20 addresses): m/44'/0'/0'/0/i
    for i in range(20):
        bip_obj_addr = bip_obj_chain.AddressIndex(i)
        res.append([bip_obj_addr.PublicKey().ToAddress(),bip_obj_addr.PrivateKey().Raw().ToHex()])
    return res[0:depth] (edited) 

# Create a function called `derive_wallets`
def derive_wallets(mnemonic,coin,depth):
    return get_addresses(mnemonic,coin,depth)
#     print(derive_wallets(mnemonic,'BTC',depth))
#     print(derive_wallets(mnemonic,"ETH",depth))
#     print(derive_wallets(mnemonic,'BITCOINTEST',depth))



# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = ["ETH", "BITCOINTEST", "BTC"]
keys = {}
for coin in coins:
    keys[coin] = derive_wallets(mnemonic,coin,depth)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin,key):
    key = wif_to_key()
    if coin == 'ETH':
        return Account.privateKeyToAccount(key)
    elif coin == 'BTC':
        return PrivateKeyTestnet(key)
    elif coin == 'BITCOINTEST':
        return PrivateKeyTestnet(key)
    # replace with different addresses
    addresses = ["mn9CfkoXJpkCMkPbRcBfUphso7QaDmBmgz", "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"]

    outputs = []

    for address in addresses:
        outputs.append((address, 0.0001, "btc"))

    return(key.send(outputs))


# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }



# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()

