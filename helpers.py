import os
import time
import sys

def clear_terminal():
    '''
    Call this function to clear
    the terminal of the last section.
    It resets colorama colors also.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    
def txt_effect(text_to_print):
    '''
    This prints all of the text slowly.
    '''
    for character in text_to_print:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.009)
    
    time.sleep(0.7)