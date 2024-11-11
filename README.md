# Bitcoin Address Generator

## Overview
This Python script generates Bitcoin addresses and corresponding private keys using the BIP44, BIP84, and BIP49 standards. It allows users to create multiple addresses from a mnemonic seed phrase of varying lengths (12, 15, 18, 21, or 24 words).

## Features
- Generates BIP39 compliant mnemonic seed phrases.
- Supports multiple address types: P2PKH, P2SH, P2WPKH, and P2WPKH-in-P2SH.
- Outputs private keys in both Hex and WIF formats.
- Configurable number of iterations for batch address generation.

## Prerequisites
Before running the script, ensure you have the `hdwallet` package installed:

     pip install hdwallet
     


## Usage
Run the script in a Python environment. The user will be prompted to:
1. Choose the number of words for the seed phrase (12, 15, 18, 21, or 24).
2. Enter the number of iterations for generating sets of addresses and keys.

The results will be saved to a file named `seeds.txt` in the following format:
   - Seed Phrase : <mnemonic>
   - P2PKH Address : <address>
   - P2SH Address : <address>
   - P2WPKH Address : <address>
   - P2WPKH in P2SH Address : <address>
   - Private Key (Hex) : <key>
   - Private Key (WIF) : <key>


## Disclaimer
This script is for educational purposes only. Do not use the generated addresses and keys for real transactions. It's essential to understand the risks involved in generating and handling private keys.

## License
[MIT](https://opensource.org/licenses/MIT)

## Donate: 
**BTC**: `1GZdNtQYa2DN4b3hLekrYErv9c8WLqbBTm`
