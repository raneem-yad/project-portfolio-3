import time
import pyfiglet
# from tabulate import tabulate
from utils.theme import Colors
import utils.helpers as helpers
import user.user_func as user
import utils.tables as table



options = ["1","2","3","4"]
def print_welcome_messages():
    # helpers.clear_terminal()
    helpers.txt_effect(Colors.BOLD+Colors.RED +
                       pyfiglet.figlet_format("Welcome to TaskTracker App!") + Colors.RESET)

def print_option_table():
    messages = ["Login","Create Account","App preview","Quit App"]
    # Table headers
    headers = ["How we can Help you", "Press"]
    # create columns 
    columns = table.create_columns(messages,options)
    intro_table = table.TablesDrawing(columns,headers)
    print(intro_table.print_table())


def validate_user_input(option):
    """
    Validates any inputs with 4 options
    """
    try:
        if option not in options:
            raise ValueError(
                f"You must enter a number between "
                f"{Colors.BLUE}{options[0]}{Colors.RESET} and "
                f"{Colors.BLUE}{options[-1]}{Colors.RESET}. "
                f"You entered {Colors.RED}{option}{Colors.RESET}")
    except ValueError as e:
        print(" ")
        print(f"{Colors.RED}Invalid entry:{Colors.RESET} {e}.\n")
        return False
    return True

def login_input():
    helpers.clear_terminal()
    print("login window")
    while True:
        username = input(f"{Colors.MAGENTA}Enter your username :\n {Colors.RESET}")
        password = input(f"{Colors.MAGENTA}Enter your password :\n {Colors.RESET}")
        if(not user.login(username,password)):
            print(" ")
            print(f"{Colors.Red}Sorry,username or password are wrong.{Colors.RESET}")
            print("Would you like to create an account?")

                # 1. Yes
                # 2. No, I'll try again
                # """)

def handel_option():
    while True:
        user_option = input(f"{Colors.MAGENTA}Enter your choice here: \n {Colors.RESET}")
        if validate_user_input(user_option):
            break
    if user_option == '1':
        login_input()
        # log_in()
    # elif user_option == '2':
    #     clear_terminal()
    #     get_username = create_account()
    #     set_up_new_budget(get_username)
    # elif user_option == '3':
    #     delete_account()
    else:
        helpers.clear_terminal()
        print("----------------------------------\n")
        print(f"{Colors.RED}Quitting app... {Colors.RESET}")
        print(" ")
        print("----------------------------------")
        time.sleep(1.5)
        helpers.clear_terminal()
        print("----------------------------------\n")
        print(f"{Colors.MAGENTA}Thanks for using Our APP: See You Soon  {Colors.RESET}")
        print(" ")
        print("----------------------------------")

def main():

    print_welcome_messages()
    print_option_table()
    handel_option()
    

main()
