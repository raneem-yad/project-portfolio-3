import time
import pyfiglet
from utils.theme import Colors
import utils.helpers as helpers
import user.user_func as user
import utils.tables as table


OPTION_TEXT = f"{Colors.MAGENTA}Enter your choice here: \n {Colors.RESET}"


def print_welcome_messages():
    helpers.txt_effect(Colors.BOLD+Colors.RED +
                       pyfiglet.figlet_format("Welcome to TaskTracker App!") + Colors.RESET)


def print_option_table(options):
    messages = ["Login", "Create Account", "App preview", "Quit App"]
    # Table headers
    headers = ["How we can Help you", "Press"]
    # create columns
    columns = table.create_columns(messages, options)
    intro_table = table.TablesDrawing(columns, headers)
    print(intro_table.print_table())


def validate_user_input(useroption, options):
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
    messages = ["Yes", "No, I'll try again", "Back Home!"]
    # Table headers
    headers = ["Would you like to create an account?", "Press"]
    # create columns
    columns = table.create_columns(messages, options)
    intro_table = table.TablesDrawing(columns, headers)
    print(intro_table.print_table())


def handel_extra_options(options):
    while True:
        user_option = input(OPTION_TEXT).strip()
        if validate_user_input(user_option, options):
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
    helpers.print_section_title(title='Login! Enter your Creditionals',
                                    is_sleep=False, text_color=Colors.MAGENTA)
    while True:
        username = input(
            f"{Colors.MAGENTA}Enter your username :\n {Colors.RESET}")
        password = input(
            f"{Colors.MAGENTA}Enter your password :\n {Colors.RESET}")
        # user login failed
        if (not user.login(username, password)):
            print(f"{Colors.RED}\nSorry,username or password are wrong.{Colors.RESET}")
            options = ['1', '2', '3']
            login_extra_options(options)
            handel_extra_options(options)
        # user login sucessed
        else:
            print(f"{Colors.MAGENTA} Welcome Back, {username}. Retrieving your Tasks... {Colors.RESET}")
            break


def create_account_input():
    helpers.print_section_title(title='Create New Account!',
                                    is_sleep=False, text_color=Colors.MAGENTA)
    
    while True:
        fullname = input(helpers.sentence('Enter your Full name!\n')).capitalize()
        email = input(helpers.sentence("Enter your Email address!:\n"))

        if not user.is_valid_email(email):
            print(helpers.sentence("Invalid or existing email address\n",txt_color=Colors.RED))
            continue

        username = input(helpers.sentence("Now enter a username. Make sure it does not have any spaces:\n"))
        if " " in username:
            print(helpers.sentence("Your username can't have spaces. Please try again.\n",txt_color=Colors.RED))
            continue

        if user.username_exist(username):
            print(helpers.sentence("Username already exists.\n",txt_color=Colors.RED))
            if input(helpers.sentence("Would you like to login instead? (Enter 'yes' or 'no'): ")).lower() == 'yes':
                login_input()
            continue

        while True:
            password = input(helpers.sentence("Enter your Password: \n"))
            confirm_password = input(helpers.sentence("Re-enter your Password: \n"))
            if password == confirm_password:
                break
            else:
                print(helpers.sentence("password and confirmPassword don't match. Please try again.\n",txt_color=Colors.RED))

        print(helpers.sentence(f"Creating New Account...\n",txt_color= Colors.YELLOW))
        user.add_new_user(fullname =fullname, username = username, email=email , password= password)
        print(helpers.sentence(f"New user has been added! \n",txt_color= Colors.YELLOW))


def handel_option(options):
    while True:
        user_option = input(OPTION_TEXT).strip()
        if validate_user_input(user_option, options):
            break
    if user_option == '1':
        login_input()

    elif user_option == '2':
        create_account_input()
        # clear_terminal()
        # get_username = create_account()
        # set_up_new_budget(get_username)
    # elif user_option == '3':
    #     delete_account()
    else:
        helpers.print_section_title(
            title='Quitting app... ', is_sleep=True, text_color=Colors.RED)
        helpers.print_section_title(title='Thanks for using Our APP: See You Soon  ',
                                    is_sleep=False, text_color=Colors.MAGENTA, emoji='\U0001F609')


def home():
    options = ["1", "2", "3", "4"]
    print_option_table(options)
    handel_option(options)


def main():
    print_welcome_messages()
    home()


main()
