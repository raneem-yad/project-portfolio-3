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
user_tasks = []


def show_tasks_preview_table():
    """Prints a preview table of tasks."""
    messages = tasks.DEMO_DATA
    headers = tasks.TASKS_FULL_TABLE_HEADERS
    intro_table = table.TablesDrawing(messages, headers)
    print(intro_table.print_table())


def show_today_tasks_table(tasks):
    """
    Displays today's tasks in a table format.

    Formats and prints the tasks for the current day in a table.
    The tasks are displayed along with their priority and completion status.

    Args:
    - tasks (list): A list of tasks for the current day.
    """
    messages = tasks
    headers = [f"{Colors.YELLOW}Today Tasks{Colors.RESET}",
               f"{Colors.YELLOW}Priority{Colors.RESET}", f"{Colors.YELLOW}Is Done?{Colors.RESET}"]
    intro_table = table.TablesDrawing(messages, headers, indexed=True)
    print(intro_table.print_table())


def print_task_option_table(options):
    """
    Prints the Tasks options table.
    
    Args:
    - options (list): A list of valid menu options.
    """
    messages = ["Show Tasks for another date", "Add new Task",
                "Make Task as Done", "Delete Task", "Back Home"]
    headers = ["Options", "Press"]
    columns = table.create_rows(messages, options)
    intro_table = table.TablesDrawing(columns, headers)
    print(intro_table.print_table())


def back_home():
    """
    Navigates back to the home menu.

    Clears the terminal, prints a message indicating
    that the user is returning to the home menu, waits
    for a specified sleep time, and then displays the
    home menu again.
    """
    helpers.clear_terminal()
    print(helpers.sentence("backing to home...", txt_color=Colors.YELLOW))
    time.sleep(SLEEP_TIME)
    display_home_menu()


def login_extra_options(options):
    """
    Prints extra login options.
    
    Args:
    - options (list): A list of valid menu options.
    """
    messages = ["Yes", "No, I'll try again", "Back Home!"]
    headers = ["Would you like to create an account?", "Press"]
    columns = table.create_columns(messages, options)
    intro_table = table.TablesDrawing(columns, headers)
    print(intro_table.print_table())


def validate_user_input(useroption, options):
    """
    Validates user input against a list of valid options.

    Checks if the user's input is included in the provided list of options.
    If the input is not valid, raises a ValueError with a descriptive message.
    Prints an error message and returns False if the input is invalid.
    Returns True if the input is valid.

    Args:
    - user_option (str): The user's input option.
    - options (list): A list of valid options.

    Returns:
    - bool: True if the input is valid, False otherwise.
    """
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
    """
    Handles extra options after login failure.

    Prompts the user to choose an action from the provided options.
    If the chosen action is to create a new account, clears the terminal and
    guides the user through creating a new account.
    If the chosen action is to re-enter data, clears the terminal and prompts
    the user to re-enter their login credentials.
    If the chosen action is to go back home, returns to the home menu.

    Args:
    - options (list): A list of valid menu options.
    """
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


def create_new_task(username):
    """
    Guides the user through creating a new task.

    Prompts the user to enter a task name, additional details, and priority level.
    Validates the priority input to ensure it is within the acceptable range (1-3).
    If the input is invalid, prompts the user again.
    If the input is valid, adds the new task and displays a confirmation message.

    Args:
    - username (str): The username of the user creating the task.
    """
    helpers.print_section_title(title='Create New Task!',
                                is_sleep=False, text_color=Colors.MAGENTA)

    while True:
        task = input(helpers.sentence(
            'Name your Task!\n')).capitalize()
        task_details = input(helpers.sentence(
            "Enter more details if there is no more details Press Enter!:\n"))

        priority = input(helpers.sentence(
            'What the Task Priority from 1-3, 1 is the Highest!\n'))
        if priority not in ["1", "2", "3"]:
            print(helpers.sentence(
                "Invalid input! Type 1 or 2 or 3! \n", txt_color=Colors.RED))
            continue

        break
    print(helpers.sentence(f"Adding New Task...\n", txt_color=Colors.YELLOW))
    tasks.add_new_task(task=task, details=task_details,
                       priority=priority, username=username)
    print(helpers.sentence(
        f"New user has been added! \n", txt_color=Colors.YELLOW))
    show_tasks_section(username)


def update_task_status(username):
    """
    Updates the status of a task for the specified user.

    Prompts the user to enter the task number they want to change.
    Checks if the task number is valid and if the task status is not 'Done'.
    If the task number is invalid or the task status is 'Done', displays an error message and prompts the user again.
    If the task number is valid and the task status is not 'Done', updates the task status, waits for a specified sleep time,
    and then displays the updated task section.

    Args:
    - username (str): The username of the user whose task status is being updated.
    """
    while True:
        task_index = int(input(helpers.sentence(
            'Which Task you want to change! Enter Task Number\n')).strip())

        if task_index not in list(range(len(user_tasks))):
            print(helpers.sentence(
                "Invalid input! Make Sure Than Task Number exist! \n", txt_color=Colors.RED))
            # continue
        elif (user_tasks[task_index][2]).strip() == 'Yes':
            print(helpers.sentence(
                "Invalid Task! You choosed a task with Done Status! \n", txt_color=Colors.RED))
            continue
        else:
            break

    print(helpers.sentence(
        f"Updating Task Status number {task_index}...\n", txt_color=Colors.YELLOW))
    tasks.update_status(task_name=user_tasks[task_index][0])
    time.sleep(SLEEP_TIME)
    print(helpers.sentence(
        f"Task has been updated! \n", txt_color=Colors.YELLOW))
    show_tasks_section(username)


def delete_task(username):
    """
    Deletes a task for the specified user.

    Prompts the user to enter the task number they want to delete.
    Checks if the task number is valid.
    If the task number is invalid, displays an error message and prompts the user again.
    If the task number is valid, deletes the task, waits for a specified sleep time,
    and then displays the updated task section.

    Args:
    - username (str): The username of the user whose task is being deleted.
    """
    while True:
        task_index = int(input(helpers.sentence(
            'Which Task you want to Delete it!\n')).strip())

        if task_index not in list(range(len(user_tasks))):
            print(helpers.sentence(
                "Invalid input! Make Sure Than Task Number exist! \n", txt_color=Colors.RED))
            continue
        else:
            break

    print(helpers.sentence(
        f"deleting Task number {task_index}...\n", txt_color=Colors.YELLOW))
    tasks.del_task(task_name=user_tasks[task_index][0])
    time.sleep(SLEEP_TIME)
    print(helpers.sentence(
        f"Task has been updated! \n", txt_color=Colors.YELLOW))
    show_tasks_section(username)


def show_tasks_per_specific_date(username):
    """
    Displays tasks for a specific due date for the specified user.

    Prompts the user to enter a task due date in the format 'YYYY-MM-DD'.
    Validates the input to ensure it is in the correct format.
    If the input is invalid, displays an error message and prompts the user again.
    If the input is valid, displays the selected date, and then shows tasks due on that date.

    Args:
    - username (str): The username of the user whose tasks are being displayed.
    """
    while True:
        task_due_date = input(helpers.sentence(
            'Enter a task due date (YYYY-MM-DD): \n'))

        if not tasks.validate_date(task_due_date):
            print(helpers.sentence(
                "Invalid input! Make Sure the date is in Correct Form! \n", txt_color=Colors.RED))
            continue
        else:
            break
    print(f"Selected date is {task_due_date}")
    helpers.print_section_title(title=f'Selected date is{task_due_date}')
    show_tasks_per_date(username, task_due_date)
    


def handel_task_option(options, username):
    """
    Handles user menu option input for tasks.

    Prompts the user to choose an option from the provided list of options.
    Validates the user input to ensure it matches one of the options.
    If the input is valid, executes the corresponding action based on the selected option.
    If the input is invalid, prompts the user again.

    Args:
    - options (list): A list of valid menu options.
    - username (str): The username of the user whose tasks are being handled.
    """
    options = ["1", "2", "3", "4", "5"]

    """Handles user menu option input."""
    while True:
        user_option = input(OPTION_TEXT).strip()
        if validate_user_input(user_option, options):
            break
    if user_option == '1':
        show_tasks_per_specific_date(username)

    elif user_option == '2':
        create_new_task(username)

    elif user_option == '3':
        update_task_status(username)

    elif user_option == '4':
        delete_task(username)

    else:
        back_home()


def show_tasks_section(username):
    """
    Displays the tasks section for the specified user.

    Prints a welcome message to the tasks tracker.
    Retrieves the current date and displays it.
    Shows tasks for the current date.

    Args:
    - username (str): The username of the user whose tasks are being displayed.
    """
    helpers.print_section_title(title='Welcome to Tasks Tracker!')
    today_date = datetime.now().date()
    # demo_date = '2024-02-26'
    print(f"today date is {today_date}")
    show_tasks_per_date(username, today_date)


def show_tasks_per_date(username, date):
    """
    Displays tasks for the specified date for the given user.

    Retrieves tasks for the specified user and date.
    Displays the tasks in a table format.
    Shows options for task management.
    Handles user input for task management options.

    Args:
    - username (str): The username of the user whose tasks are being displayed.
    - date (datetime.date): The date for which tasks are being displayed.
    """
    global user_tasks
    user_tasks = tasks.get_tasks_per_date(username, date)
    # print(tabulate({"Today Tasks": user_tasks}, headers="keys"))
    show_today_tasks_table(user_tasks)
    # show tasks options
    options = ["1", "2", "3", "4", "5"]
    print_task_option_table(options)
    handel_task_option(options, username)


def create_account_input():
    """
    Guides the user through creating a new account.

    Prompts the user to enter their full name, email address, desired username,
    and password. Validates the email address format and checks if the username
    is available. If the username already exists, offers the option to log in
    instead. Ensures that the password and confirm password match before creating
    the new account.

    """
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


def login_input():
    """
    Guides the user through the login process.

    Prompts the user to enter their username and password. Validates the credentials
    and checks if they match an existing user. If the login fails, offers additional
    options such as creating a new account, retrying login, or returning to the home menu.
    If the login is successful, displays a welcome message and retrieves the user's tasks.

    """
    helpers.print_section_title(title='Login! Enter your Creditionals')
    while True:
        username = input(helpers.sentence(txt="Enter your username :\n"))
        password = input(helpers.sentence(txt="Enter your password :\n"))
        # user login failed
        if (not user.login(username, password)):
            print(helpers.sentence(
                txt="\nSorry,username or password are wrong.", txt_color=Colors.RED))
            options = ['1', '2', '3']
            login_extra_options(options)
            handel_extra_options(options)
        # user login sucessed
        else:
            break
    print(
        f"{Colors.MAGENTA} Welcome Back, {username}. Retrieving your Tasks... {Colors.RESET}")
    show_tasks_section(username)


def handel_option(options):
    """
    Handles user menu option input.

    Prompts the user to enter a menu option and validates the input.
    If the input is valid, executes the corresponding action based on the selected option.

    Args:
    - options (list): A list of valid menu options.
    """
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


def print_option_table(options):
    """
    Prints the main menu option table.

    Creates a table with the provided messages and options.
    Displays the table to the user.

    Args:
    - options (list): A list of valid menu options.
    """
    messages = ["Login", "Create Account", "App Preview", "Quit App"]
    headers = ["How we can Help you", "Press"]
    columns = table.create_rows(messages, options)
    intro_table = table.TablesDrawing(columns, headers)
    print(intro_table.print_table())


def display_home_menu():
    """
    Displays the home menu with options and handles user input.
    """
    options = ["1", "2", "3", "4"]
    print_option_table(options)
    handel_option(options)


def print_welcome_messages():
    """Prints welcome messages."""
    helpers.txt_effect(Colors.BOLD+Colors.RED +
                       pyfiglet.figlet_format("Welcome to TaskTracker App!") + Colors.RESET)


def run_task_tracker():
    """
    Runs the TaskTracker application.
    """
    print_welcome_messages()
    display_home_menu()


if __name__ == "__main__":
    run_task_tracker()
