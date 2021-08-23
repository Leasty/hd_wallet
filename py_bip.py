{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3dc944ce-3ac6-41d6-b363-72f6635d7cfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Master key (bytes): ac84119ca8f65cb7221dc0b2cd5ea4faf9930501814ca5b2447d64413f221183\n",
      "Master key (extended): tprv8ZgxMBicQKsPf11THB62Cq2cf7pgBvj2NV3vjiWcSikTfKr9AzF2i9DDnLmAHm4563K8fVGPtENAfPxvcz6iUWerCVrFjRV7SkZuwQ6Tu2h\n",
      "Master key (WIF): cTN3rSB16RX9S9vk99KrFq8kvCMriFbxAkq1Sr98TkYxYM5czSNd\n"
     ]
    }
   ],
   "source": [
    "from bip_utils import Bip32, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes\n",
    "from dotenv import load_dotenv\n",
    "import os\n",
    "load_dotenv()\n",
    "mnemonic = os.getenv(\"MNEMONIC\")\n",
    "seed_bytes = Bip39SeedGenerator(mnemonic).Generate()\n",
    "# For Bitcoin Testnet keys, sub in Bip44Coins.BITCOIN_TESTNET\n",
    "# For bitcoin mainnet keys, sub in Bip44Coins.BITCOIN\n",
    "if coin = BTC:\n",
    "    bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_TESTNET)\n",
    "elif coin = ETH\n",
    "\n",
    "bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)\n",
    "\n",
    "def get_addresses(mnemonic, coin, depth=3):\n",
    "    \n",
    "    res = []\n",
    "    # Generate BIP44 chain keys: m/44'/0'/0'/0\n",
    "    bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)\n",
    "    # Generate the address pool (first 20 addresses): m/44'/0'/0'/0/i\n",
    "    for i in range(20):\n",
    "        bip_obj_addr = bip_obj_chain.AddressIndex(i)\n",
    "        res.append(bip_obj_addr.PublicKey().RawCompressed().ToHex())\n",
    "        \n",
    "    return res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "096ea894-e126-4abe-a24b-6a2a596e1cb1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
