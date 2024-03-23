from web3 import Web3

def cprint(text, color):
    """
    Prints colored text to the console.

    Args:
        text (str): The text to print.
        color (str): The color of the text.
    """
    colors = {
        "black": "\033[0;30m",
        "red": "\033[0;31m",
        "green": "\033[0;32m",
        "yellow": "\033[0;33m",
        "blue": "\033[0;34m",
        "magenta": "\033[0;35m",
        "cyan": "\033[0;36m",
        "white": "\033[0;37m",
        "reset": "\033[0m",
    }
    print(colors[color] + text + colors["reset"])


def approve(web3: Web3, to_symbol: str, tx_hash: bytes) -> None:
    """
    Approves a token for spending.

    Args:
        web3 (Web3): The Web3 instance.
        to_symbol (str): The symbol of the token to approve.
        tx_hash (bytes): The transaction hash of the approval transaction.
    """
    cprint(f'\n>>> approve {to_symbol} : https://www.example.com 'green')

