#####################
# Importing libraries
#####################
import subprocess 
import json
import os
from dotenv import load_dotenv
from constants import *
from bit import Key, PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI
from bit import *
from web3 import Web3
from eth_account import Account 

######################################
# Web3 connection and loading mnemonic
######################################
# Nodes runing with POW
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1.8545"))

# Loading EV
load_dotenv

# Loading Mnemonic EV
mnemonic = os.getenv('MNEMONIC')

#######################
# Functions to transact
#######################
def derive_wallets(mnemonic, coin, numderive):
    """Use the subprocess library to call the ./derive php file script from Python"""
    command = 'php hd-wallet-derive.php -g --mnemonic="'+str(mnemonic)+'" --numderive='+str(numderive)+' --coin='+str(coin)+' --format=jsonpretty' 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return json.loads(output) 

# Create a coin object to hold child wallets
coins = {'eth':derive_wallets(mnemonic=mnemonic,coin=ETH,numderive=3),'btc-test': derive_wallets(mnemonic=mnemonic,coin=BTCTEST,numderive=3)}

eth_privatekey = coins['eth'][0]['privkey']
btc_privatekey = coins['btc-test'][0]['privkey']

def priv_key_to_account(coin, priv_key):
    """Convert the privkey string in a child key to an account object that bit or web3.py can use to transact"""
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
eth_account = priv_key_to_account(ETH,eth_privatekey)
btc_account = priv_key_to_account(BTCTEST,btc_privatekey)

def create_tx(coin, account, recipient, amount):
    """create the raw, unsigned transaction that contains all metadata needed to transact"""
    global tx_data
    if coin ==ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount}
        )
        tx_data = {
            "to": recipient,
            "from": account.address,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }
        return tx_data

    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])   

def send_tx(coin, account, recipient, amount):
    """call create_tx, sign the transaction, then send it to the designated network"""
    if coin =='ETH':
        tx_eth = create_tx(coin,account, recipient, amount)
        sign_tx_eth = account.sign_transaction(tx_eth)
        result = w3.eth.sendRawTransaction(sign_tx_eth.rawTransaction)
        print(result.hex())
        return result.hex()
    else:
        tx_btctest= create_tx(coin,account,recipient,amount)
        sign_tx_btctest = account.sign_transaction(tx_btctest)
        from bit.network import NetworkAPI
        NetworkAPI.broadcast_tx_testnet(sign_tx_btctest)       
        return sign_tx_btctest