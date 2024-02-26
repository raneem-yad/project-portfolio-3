import time
from datetime import datetime
import pyfiglet
from tabulate import tabulate
from utils.theme import Colors
import utils.helpers as helpers
import utils.tables as table
import services.users_func as user
import services.tasks_func as tasks


OPTION_TEXT = f"{Colors.MAGENTA}Enter your choice here: \n {Colors.RESET}"
SLEEP_TIME = 0.8

def print_welcome_messages():
    """Prints welcome messages."""
    helpers.txt_effect(Colors.BOLD+Colors.RED +
                       pyfiglet.figlet_format("Welcome to TaskTracker App!") + Colors.RESET)


def print_option_table(options):
    """Prints the main menu option table."""
    messages = ["Login", "Create Account", "App Preview", "Quit App"]
    headers = ["How we can Help you", "Press"]
    columns = table.create_columns(messages, options)
    intro_table = table.TablesDrawing(columns, headers)
    print(intro_table.print_table())


def show_tasks_preview_table():
    """Prints a preview table of tasks."""
    messages = tasks.DEMO_DATA
    headers = tasks.TASKS_FULL_TABLE_HEADERS
    intro_table = table.TablesDrawing(messages, headers)
    print(intro_table.print_table())


def show_today_tasks_table(tasks):
    """Prints a table of today tasks."""
    messages = tasks
    headers = [f"{Colors.YELLOW}Today Tasks{Colors.RESET}",
               f"{Colors.YELLOW}Priority{Colors.RESET}", f"{Colors.YELLOW}Is Done?{Colors.RESET}"]
    intro_table = table.TablesDrawing(messages, headers)
    print(intro_table.print_table())
    

def print_task_option_table(options):
    """Prints the Tasks options table."""
    messages = ["Show Tasks for another date", "Add new Task","Back Home"]
    headers = ["Options", "Press"]
    columns = table.create_columns(messages, options)
    intro_table = table.TablesDrawing(columns, headers)
    print(intro_table.print_table())


def back_home():
    helpers.clear_terminal()
    print(helpers.sentence("backing to home...",txt_color=Colors.YELLOW))
    time.sleep(SLEEP_TIME)
    display_home_menu()


def login_extra_options(options):
    """Prints extra login options."""
    messages = ["Yes", "No, I'll try again", "Back Home!"]
    headers = ["Would you like to create an account?", "Press"]
    columns = table.create_columns(messages, options)
    intro_table = table.TablesDrawing(columns, headers)
    print(intro_table.print_table())


def validate_user_input(useroption, options):
    """Validates user input."""
    try:
        if useroption not in options:
            raise ValueError(
                f"You must enter a number between "
                f"{Colors.BLUE}{options[0]}{Colors.RESET} and "
                f"{Colors.BLUE}{options[-1]}{Colors.RESET}. "
                f"You entered {Colors.RED}{useroption}{Colors.RESET}")
    except ValueError as e:
        print(f"{Colors.RED} \n Invalid entry:{Colors.RESET} {e}.\n")
        return False
    return True


def handel_extra_options(options):
    """Handles extra options after login failure."""
    while True:
        user_option = input(OPTION_TEXT).strip()
        if validate_user_input(user_option, options):
            break

    # option one : means creating a new account
    if user_option == '1':
        helpers.clear_terminal()
        print("we will create a new account")
        create_account_input()
    elif user_option == '2':
        helpers.clear_terminal()
        print("re-enter your data")
    else:
        back_home()


def handel_task_option(options):
    """Handles user menu option input."""
    while True:
        user_option = input(OPTION_TEXT).strip()
        if validate_user_input(user_option, options):
            break
    if user_option == '1':
        print("Showing tasks for different date")

    elif user_option == '2':
        print("adding new tasks")
    else:
        back_home()


def show_tasks_section(username):
    helpers.print_section_title(title='Welcome to Tasks Tracker!')
    today_date = datetime.now().date()
    # demo_date = '2024-02-26'
    print(f"today date is {today_date}")
    user_tasks = tasks.get_tasks_per_date(username, today_date)
    # print(tabulate({"Today Tasks": user_tasks}, headers="keys"))
    show_today_tasks_table(user_tasks)
    # show tasks options
    options = ["1", "2","3"]
    print_task_option_table(options)
    handel_task_option(options) 


def login_input():
    """Handles user login input."""
    helpers.print_section_title(title='Login! Enter your Creditionals')
    while True:
        username = input(helpers.sentence(txt="Enter your username :\n"))
        password = input( helpers.sentence(txt="Enter your password :\n"))
        # user login failed
        if (not user.login(username, password)):
            print(helpers.sentence(txt="\nSorry,username or password are wrong.",txt_color=Colors.RED))
            options = ['1', '2', '3']
            login_extra_options(options)
            handel_extra_options(options)
        # user login sucessed
        else:
            print(
                f"{Colors.MAGENTA} Welcome Back, {username}. Retrieving your Tasks... {Colors.RESET}")
            show_tasks_section(username)
            break


def create_account_input():
    """Handles user account creation input."""
    helpers.print_section_title(title='Create New Account!',
                                is_sleep=False, text_color=Colors.MAGENTA)

    while True:
        fullname = input(helpers.sentence(
            'Enter your Full name!\n')).capitalize()
        email = input(helpers.sentence("Enter your Email address!:\n"))

        if not user.is_valid_email(email):
            print(helpers.sentence(
                "Invalid or existing email address\n", txt_color=Colors.RED))
            continue

        username = input(helpers.sentence(
            "Now enter a username. Make sure it does not have any spaces:\n"))
        if " " in username:
            print(helpers.sentence(
                "Your username can't have spaces. Please try again.\n", txt_color=Colors.RED))
            continue

        if user.username_exists(username):
            print(helpers.sentence(
                "Username already exists.\n", txt_color=Colors.RED))
            if input(helpers.sentence("Would you like to login instead? (Enter 'yes' or 'no'): ")).lower() == 'yes':
                login_input()
            continue

        while True:
            password = input(helpers.sentence("Enter your Password: \n"))
            confirm_password = input(
                helpers.sentence("Re-enter your Password: \n"))
            if password == confirm_password:
                break
            else:
                print(helpers.sentence(
                    "password and confirmPassword don't match. Please try again.\n", txt_color=Colors.RED))

        print(helpers.sentence(f"Creating New Account...\n", txt_color=Colors.YELLOW))
        user.add_new_user(fullname=fullname, username=username,
                          email=email, password=password)
        print(helpers.sentence(
            f"New user has been added! \n", txt_color=Colors.YELLOW))


def handel_option(options):
    """Handles user menu option input."""
    while True:
        user_option = input(OPTION_TEXT).strip()
        if validate_user_input(user_option, options):
            break
    if user_option == '1':
        login_input()

    elif user_option == '2':
        create_account_input()
    elif user_option == '3':
        show_tasks_preview_table()
    else:
        helpers.print_section_title(
            title='Quitting app... ', is_sleep=True, text_color=Colors.RED)
        helpers.print_section_title(title='Thanks for using Our APP: See You Soon  ',
                                    is_sleep=False, text_color=Colors.MAGENTA, emoji='\U0001F609')


def display_home_menu():
    """
    Displays the home menu with options and handles user input.
    """
    options = ["1", "2", "3", "4"]
    print_option_table(options)
    handel_option(options)


def run_task_tracker():
    """
    Runs the TaskTracker application.
    """
    print_welcome_messages()
    display_home_menu()


run_task_tracker()
