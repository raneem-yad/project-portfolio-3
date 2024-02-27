import os
import time
import sys

from utils.theme import Colors


def clear_terminal():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def txt_effect(text_to_print):
    """
    Prints text with a typing effect.

    Args:
        text_to_print (str): The text to be printed with the effect.
    """
    for character in text_to_print:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)

    time.sleep(0.7)


def print_section_title(title, is_sleep=False, text_color=Colors.MAGENTA, emoji=""):
    """
    Prints a section title with optional sleep delay.

    Args:
        title (str): The title to be printed.
        is_sleep (bool, optional): Whether to introduce a sleep delay after printing the title. Default is False.
        text_color (str, optional): The color of the title text. Default is Colors.MAGENTA.
        emoji (str, optional): An emoji to be included in the title. Default is an empty string.
    """
    clear_terminal()
    print("----------------------------------\n")
    print(f"{text_color}{title} {emoji}{Colors.RESET}\n")
    print("----------------------------------")
    if is_sleep:
        time.sleep(1.5)


def sentence(txt, txt_color=Colors.MAGENTA):
    """
    Formats a sentence as a question.

    Args:
        txt (str): The sentence to be formatted.
        txt_color (str): The color to be formatted.

    Returns:
        str: The formatted sentence.
    """
    return f"{txt_color}{txt} {Colors.RESET}"
