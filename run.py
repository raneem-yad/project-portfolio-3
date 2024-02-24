import time
import pyfiglet
from utils.theme import Colors
import utils.helpers as helpers
import user.user_func as user
import utils.tables as table




OPTION_TEXT = f"{Colors.MAGENTA}Enter your choice here: \n {Colors.RESET}"
def print_welcome_messages():
    # helpers.clear_terminal()
    helpers.txt_effect(Colors.BOLD+Colors.RED +
                       pyfiglet.figlet_format("Welcome to TaskTracker App!") + Colors.RESET)

def print_option_table(options):
    messages = ["Login","Create Account","App preview","Quit App"]
    # Table headers
    headers = ["How we can Help you", "Press"]
    # create columns 
    columns = table.create_columns(messages,options)
    intro_table = table.TablesDrawing(columns,headers)
    print(intro_table.print_table())


def validate_user_input(useroption,options):
    """

    """
    try:
        if useroption not in options:
            raise ValueError(
                f"You must enter a number between "
                f"{Colors.BLUE}{options[0]}{Colors.RESET} and "
                f"{Colors.BLUE}{options[-1]}{Colors.RESET}. "
                f"You entered {Colors.RED}{useroption}{Colors.RESET}")
    except ValueError as e:
        print(" ")
        print(f"{Colors.RED}Invalid entry:{Colors.RESET} {e}.\n")
        return False
    return True


def login_extra_options(options):
    messages = ["Yes","No, I'll try again","Back Home!"]
    # Table headers
    headers = ["Would you like to create an account?", "Press"]
    # create columns 
    columns = table.create_columns(messages,options)
    intro_table = table.TablesDrawing(columns,headers)
    print(intro_table.print_table())
    

def handel_extra_options(options):  
    while True:
        user_option = input(OPTION_TEXT).strip()
        if validate_user_input(user_option,options):
            break
    
    # option one : means creating a new account
    if user_option == '1':
        helpers.clear_terminal()
        print("we will create a new account")
        # call create account function 
        # create_account()
    # option two : trying multipiles times to login in 
    # if tryed more than 3 times it will break out to the home window again
    elif user_option == '2':
        helpers.clear_terminal()
        print("re-enter your data")
    else: 
        helpers.clear_terminal()
        print("backing to home...")   
        time.sleep(0.8)
        home() 
        

     

def login_input():
    helpers.clear_terminal()
    print("login window")
    while True:
        username = input(f"{Colors.MAGENTA}Enter your username :\n {Colors.RESET}")
        password = input(f"{Colors.MAGENTA}Enter your password :\n {Colors.RESET}")
        # user login failed
        if(not user.login(username,password)):
            print(f"{Colors.RED}\nSorry,username or password are wrong.{Colors.RESET}")
            options = ['1','2','3']
            login_extra_options(options)
            handel_extra_options(options) 
        # user login sucessed
        else:
            print(f"{Colors.MAGENTA} Welcome Back, {username}. Retrieving your Tasks... {Colors.RESET}") 
            break   
           

def handel_option(options):
    while True:
        user_option = input(OPTION_TEXT).strip()
        if validate_user_input(user_option,options):
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


def home():
    options = ["1","2","3","4"]
    print_option_table(options)
    handel_option(options)

def main():
    print_welcome_messages()
    home()
    

main()
