from solders.keypair import Keypair
import base58
import json
import os
from datetime import datetime

# Create 'wallets' folder if not exists
os.makedirs("wallets", exist_ok=True)

# Generate a new wallet
wallet = Keypair()
public_key = str(wallet.pubkey())
secret_key_bytes = wallet.to_bytes()
secret_key_b58 = base58.b58encode(secret_key_bytes).decode()

# Prepare wallet data
wallet_data = {
    "public_key": public_key,
    "secret_key_base58": secret_key_b58
}

# Create unique filename using timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"wallets/sol_wallet_{timestamp}.json"

# Save to file
with open(filename, "w") as f:
    json.dump(wallet_data, f, indent=4)

# Print summary
print("✅ New wallet generated and saved:")
print("🔑 Public Key:", public_key)
print("📁 Saved to:", filename)
