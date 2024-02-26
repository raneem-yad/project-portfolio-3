import re
import utils.connecting as conn
import hashlib

SHEET_NAME = 'users'
connected_sheet = conn.get_sheet()
users_sheet = connected_sheet.worksheet(SHEET_NAME)

ID_COLUMN_INDEX = 1
USERNAME_COLUMN_INDEX = 2
EMAIL_COLUMN_INDEX = 4
PASSWORD_COLUMN_INDEX = 5


def get_all_users():
    """
    Retrieves all user data from the spreadsheet.

    Returns:
        list: A list containing all user data.
    """
    return users_sheet.get_all_values()


def get_all_emails():
    """
    Retrieves all email addresses from the spreadsheet.

    Returns:
        list: A list containing all email addresses.
    """
    return users_sheet.col_values(EMAIL_COLUMN_INDEX)


def get_all_usernames():
    """
    Retrieves all usernames from the spreadsheet.

    Returns:
        list: A list containing all usernames.
    """
    return users_sheet.col_values(USERNAME_COLUMN_INDEX)


def get_all_id():
    """
    Retrieves all ID from the spreadsheet.

    Returns:
        List: The List of ID.
    """
    return users_sheet.col_values(ID_COLUMN_INDEX)


def get_last_id():
    """
    Retrieves the last ID from the spreadsheet.

    Returns:
        str: The last ID value.
    """
    return users_sheet.col_values(ID_COLUMN_INDEX)[-1]


def get_login_info():
    """
    Retrieves login information (usernames and passwords) from the spreadsheet.

    Returns:
        Tuple: A typle containing two lists, the first list contains usernames and the second list contains passwords.
    """

    usernames_column = users_sheet.col_values(USERNAME_COLUMN_INDEX)
    passwords_column = users_sheet.col_values(PASSWORD_COLUMN_INDEX)
    return usernames_column, passwords_column


def login(username, password):
    """
    Validates the provided username and password.

    Args:
        username (str): The username to validate.
        password (str): The password to validate.

    Returns:
        bool: True if the username and password are valid, False otherwise.
    """
    usernames, passwords = get_login_info()

    if username in usernames:
        index = usernames.index(username)
        return passwords[index] == hash_password(password)
        
    return False
    

def username_exists(username):
    """
    Checks if the provided username already exists in the database.

    Args:
        username (str): The username to check.

    Returns:
        bool: True if the username exists, False otherwise.
    """
    return username in get_all_usernames()


def add_new_user(fullname, username, email, password):
    """
    Adds a new user to the Sheet.

    Args:
        fullname (str): The full name of the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
    """
    last_id = int(get_last_id())
    new_user_id = last_id + 1
    secure_password = hash_password(password)
    new_user = [new_user_id, username, fullname, email, secure_password]
    conn.update_worksheet(new_user, SHEET_NAME)


def get_user_id_per_username(username):
    usernames = get_all_usernames()
    if username in usernames:
        index = usernames.index(username)
        id = get_all_id()[index]
        return id
    else : 
        print("username doesn't exist")
    

def is_valid_email(email):
    """
    Checks if the provided email address is valid and not already in use.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid and not already in use, False otherwise.
    """
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex_email, email) and email not in get_all_emails()


def hash_password(password):
    """
    Hashes the provided password using SHA-256 algorithm.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    try:
        password_bytes = password.encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        return hash_object.hexdigest()
    except Exception as e:
        print(f"Error hashing password: {e}")
        return None