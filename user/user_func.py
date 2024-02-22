import utils.connecting as conn
# which sheet in our spreadsheet love_sandwiches

connected_sheet = conn.get_sheet()
sales = connected_sheet.worksheet('users')

def get_all_user():
    data = sales.get_all_values()
    return data


def get_login_info():
    """Get the username and password column to check if the user exist or not
    """
    # username is in column 2
    # password is in column 5
    columns = []
    for ind in [2,5]:
        column = sales.col_values(ind)
        columns.append(column)
    return columns

def login(username, password):
    users = get_login_info()
    usernames = users[0]
    passwords = users[1]
    
    if username in usernames:
        # Get the index of the item to compare it with password
        index = usernames.index(username)
        # print(f"we found a user with username '{username}' with index: {index}")
        if (passwords[index] == password):
            # print(f"the password is {password}")
            return True
        else: 
            # print(" the password is wrong") 
            return False
    else:
        # print(f"'{username}' is not in the users.")
        return False
    
