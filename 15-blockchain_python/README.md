## Background
Your new startup is focusing on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well! The problem is, there are so many coins out there! It's
a good thing you understand how HD wallets work, since you'll need to build out a system that can create them.

You're in a race to get to the market. There aren't as many tools available in Python for this sort of thing, yet.
Thankfully, you've found a command line tool, `hd-wallet-derive` that supports not only BIP32, BIP39, and BIP44, but
also supports non-standard derivation paths for the most popular wallets out there today! However, you need to integrate
the script into your backend with your dear old friend, Python.

## Dependencies
- PHP must be installed on your operating system (any version, 5 or 7). Don't worry, you will *not* need to know any PHP.
- You will need to clone the [`hd-wallet-derive`](https://github.com/dan-da/hd-wallet-derive) tool.
- [`bit`](https://ofek.github.io/bit/) Python Bitcoin library.
- [`web3.py`](https://github.com/ethereum/web3.py) Python Ethereum library.

## Below are the steps in transacting on the blockchain
1. Install hd-derive library and get the address manually from command line
* ![Run hd-derive library manually from command line](images/hd-wallet-derive-library-installed.png)

2. Now lets automate this via Python and transact with Bitcoin or Ethereum

2. Generate a mnemonic and set it to an environment variable

3. Derive the wallet keys

4. Code to transact for btc from python shell is listed below: 

```btc_account = priv_key_to_account(BTCTEST, btc_pk) ```
```send_tx(BTCTEST,btc_account,'msQvwuLLPSgh6WUqn24HmNm5CyuEF7uhpv',0.0001)```

5. Code to transact for eth from python shell is listed below:

```eth_account = priv_key_to_account(ETH,eth_pk)```
```send_tx(ETH,eth_account,'0x1F309350dEA6040246e74Aa13b431F1bb39f9f96',1)```

6. The wallet.ipynb notebook shows additional transactions for Bitcoin within the notebook