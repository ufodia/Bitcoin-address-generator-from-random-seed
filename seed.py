from hdwallet import BIP44HDWallet, BIP84HDWallet, BIP49HDWallet
from hdwallet.cryptocurrencies import BitcoinMainnet
from hdwallet.utils import generate_mnemonic

def generate_addresses_and_keys(language, strength):
    mnemonic = generate_mnemonic(language=language, strength=strength)

    bip44_hdwallet = BIP44HDWallet(cryptocurrency=BitcoinMainnet, account=0, change=False, address=0)
    bip44_hdwallet.from_mnemonic(mnemonic=mnemonic, language=language)
    p2pkh_address = bip44_hdwallet.p2pkh_address()
    p2sh_address = bip44_hdwallet.p2sh_address()

    bip84_hdwallet = BIP84HDWallet(cryptocurrency=BitcoinMainnet, account=0, change=False, address=0)
    bip84_hdwallet.from_mnemonic(mnemonic=mnemonic, language=language)
    p2wpkh_address = bip84_hdwallet.p2wpkh_address()

    bip49_hdwallet = BIP49HDWallet(cryptocurrency=BitcoinMainnet, account=0, change=False, address=0)
    bip49_hdwallet.from_mnemonic(mnemonic=mnemonic, language=language)
    p2wpkh_in_p2sh_address = bip49_hdwallet.p2wpkh_in_p2sh_address()

    private_key_hex = bip44_hdwallet.private_key()
    private_key_wif = bip44_hdwallet.wif()

    return mnemonic, p2pkh_address, p2sh_address, p2wpkh_address, p2wpkh_in_p2sh_address, private_key_hex, private_key_wif

def get_strength_from_words(number_of_words):
    if number_of_words == 12:
        return 128
    elif number_of_words == 15:
        return 160
    elif number_of_words == 18:
        return 192
    elif number_of_words == 21:
        return 224
    elif number_of_words == 24:
        return 256
    else:
        raise ValueError("Invalid number of words. Only 12, 15, 18, 21, or 24 are allowed.")

if __name__ == "__main__":
    language = "english"
    print("Choose the number of words for the seed phrase (12, 15, 18, 21, 24):")
    number_of_words = int(input())

    try:
        strength = get_strength_from_words(number_of_words)
    except ValueError as e:
        print(e)
        exit()

    iteration_count = int(input("Enter the number of iterations: "))

    def format_line(label, data, width=30):
        return f"{label:<{width}}: {data}\n"

    with open("seeds.txt", "a") as file:
        for _ in range(iteration_count):
            result = generate_addresses_and_keys(language, strength)
            mnemonic, p2pkh, p2sh, p2wpkh, p2wpkh_in_p2sh, key_hex, key_wif = result

            file.write(format_line("SEED PHRASE", mnemonic))
            file.write(format_line("P2PKH Address", p2pkh))
            file.write(format_line("P2SH Address", p2sh))
            file.write(format_line("P2WPKH Address", p2wpkh))
            file.write(format_line("P2WPKH in P2SH Address", p2wpkh_in_p2sh))
            file.write(format_line("Private Key (Hex)", key_hex))
            file.write(format_line("Private Key (WIF)", key_wif))
            file.write("*" * 100 + "\n")

