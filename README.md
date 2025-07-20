
# 🪙 Solana Wallet Generator

A lightweight Python script to generate Solana wallets using the `solana` and `base58` libraries.

## 🚀 Features
- Generate new Solana keypairs
- Get base58-encoded secret key
- Print public address and private key

## 📦 Requirements
```bash
pip install solana base58
````

## 🧑‍💻 Usage

```python
from solana.keypair import Keypair
import base58

wallet = Keypair()
print("Public Key:", str(wallet.public_key))
print("Secret Key:", base58.b58encode(wallet.secret_key).decode())
```

## ⚠️ Warning

Keep your secret key safe and **never share it**. This gives full control of your wallet.
