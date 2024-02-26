from datetime import datetime
import utils.connecting as conn
import services.users_func as user
from utils.theme import Colors


DEMO_DATA = [
    [1, 'Prepare report', 'Compile monthly sales report', '2024-02-20', 'No'],
    [2, 'Meeting', 'Discuss project updates with team ', '2024-02-21', 'No'],
    [3, 'Presentation', 'Create slides for client presentation', '2024-02-25', 'No'],
    [4, 'Code review', 'Review recent changes in the codebase', '2024-02-23', 'No'],
    [5, 'Email follow-up', 'Follow up with clients on recent deals', '2024-02-22', 'No'],
    [6, 'Training session', 'Attend training session on new software', '2024-02-24', 'No']
]

TASKS_TABLE_HEADERS = ["Tasks", "Status"]
TASKS_FULL_TABLE_HEADERS = [" ", "Tasks","Due Date" ,"Status" , "Priority" , "More Details"]
SHEET_NAME = 'tasks'
connected_sheet = conn.get_sheet()
tasks_sheet = connected_sheet.worksheet(SHEET_NAME)

ID_COLUMN_INDEX = 1
USER_ID_COLUMN_INDEX = 2
TASK_COLUMN_INDEX = 3
PRIORITY_COLUMN_INDEX = 5
DUE_DATE_COLUMN_INDEX = 6
STATUS_COLUMN_INDEX = 7

def get_all_users_id():
    """
    Retrieves all User ID from the spreadsheet.

    Returns:
        List: The List of User ID.
    """
    return tasks_sheet.col_values(USER_ID_COLUMN_INDEX)

def get_all_tasks():
    """
    Retrieves all tasks data from the spreadsheet.

    Returns:
        list: A list containing all tasks data.
    """
    return tasks_sheet.col_values(TASK_COLUMN_INDEX)

def get_all_due_dates():
    """
    Retrieves all due dates data from the spreadsheet.

    Returns:
        list: A list containing all due dates data.
    """
    return tasks_sheet.col_values(DUE_DATE_COLUMN_INDEX)

def get_all_priorities():
    """
    Retrieves all priorities data from the spreadsheet.

    Returns:
        list: A list containing all priorities data.
    """
    return tasks_sheet.col_values(PRIORITY_COLUMN_INDEX)

def get_all_status():
    """
    Retrieves all status data from the spreadsheet.

    Returns:
        list: A list containing all status data.
    """
    return tasks_sheet.col_values(STATUS_COLUMN_INDEX)


def show_priority_label(priority):
    """
    Converts a priority level to a human-readable label.

    Args:
    - priority (str): The priority level ('1', '2', or '3').

    Returns:
    - str: The human-readable label for the priority level.
    """
    priority_labels = {'1': 'High Priority', '2': 'Mid Priority', '3': 'Low Priority'}
    return priority_labels.get(priority, 'Invalid Priority')
    
    
def show_status_label(status):
    """
    Converts a status to a human-readable label with color formatting.

    Args:
    - status (str): The status ('1' for 'Yes' or any other value for 'No').

    Returns:
    - str: The human-readable label for the status with color formatting.
    """
    status_labels = {'1': f"{Colors.GREEN}Yes{Colors.RESET}", '0': f"{Colors.RED}No{Colors.RESET}"}
    return status_labels.get(status, f"{Colors.RED}Invalid Status{Colors.RESET}")
    
def get_last_id():
    """
    Retrieves the last ID from the spreadsheet.

    Returns:
        str: The last ID value.
    """
    return tasks_sheet.col_values(ID_COLUMN_INDEX)[-1]

def get_user_id_for_task(username): 
    """
    Retrieves the user ID corresponding to the given username for a task.

    Args:
    - username (str): The username for which to retrieve the user ID.

    Returns:
    - int : The user ID .
    """
    return user.get_user_id_per_username(username)

def get_tasks_per_date(username , date):
    """
    Retrieves tasks associated with a specific date for a given username.

    Args:
    - username (str): The username for which to retrieve tasks.
    - date (str): The date in YYYY-MM-DD format.

    Returns:
    - list: A list of tasks with their priorities and statuses.
    """
    # get user id 
    user_id = get_user_id_for_task(username)
    if user_id is None:
        raise ValueError("Username not found.")
    
    ids = get_all_users_id()
    tasks = get_all_tasks()
    due_dates = get_all_due_dates()
    priorities = get_all_priorities()
    status = get_all_status()
    
    tasks_data = []
    for i in range(len(ids)): 
        if ids[i] == user_id and due_dates[i] == str(date):
            tasks_data.append([tasks[i],show_priority_label(priorities[i]),show_status_label(status[i])])
            
    if not tasks_data:
        print("No tasks found for the provided date.")
    return tasks_data



def add_new_task(task, details,priority,username): 
    """
    Adds a new task to the worksheet.

    Args:
    - task (str): The name of the task.
    - details (str): Additional details about the task.
    - priority (str): The priority of the task.
    - username (str): The username associated with the task.

    Raises:
    - ValueError: If the user ID cannot be retrieved or if the last ID is invalid.
    """
    
    user_id = get_user_id_for_task(username)
    if user_id is None:
        raise ValueError("Username not found.")

    last_id = int(get_last_id())
    if last_id is None or last_id < 0:
        raise ValueError("Invalid last ID.")
    
    new_task_id = last_id + 1
    today_date = str(datetime.now().date())
    status = '0'

    new_task = [new_task_id, user_id, task, details, priority,today_date,status]
    conn.update_worksheet(new_task, SHEET_NAME)
    
    
def update_status(task_name): 
    """
    Updates the status of a task in the worksheet.

    Args:
    - task_name (str): The name of the task to update.

    Raises:
    - ValueError: If the task name is not found in the worksheet.
    """
    cell = tasks_sheet.find(task_name)
    if not cell:
        raise ValueError("Task not found in the worksheet.")

    updated_task_row_position = cell.row
    updated_task_col_position = STATUS_COLUMN_INDEX
    tasks_sheet.update_cell(updated_task_row_position, updated_task_col_position, '1')
    
    
def del_task(task_name):
    """
    Deletes a task from the worksheet.

    Args:
    - task_name (str): The name of the task to delete.

    Raises:
    - ValueError: If the task name is not found in the worksheet.
    """
    task_cell = tasks_sheet.find(task_name)
    if not task_cell:
        raise ValueError("Task not found in the worksheet.")

    tasks_sheet.delete_rows(task_cell.row)
    
def validate_date(date_str):   
    """
    Validate if the input string represents a valid date in the format 'YYYY-MM-DD'.

    Args:
    - date_str (str): The input string to validate.

    Returns:
    - bool: True if the input string is a valid date, False otherwise.
    
    Raises:
    - ValueError: If the input string does not represent a valid date.
    """
    try:
        # Parse the input date string using strptime() method
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        # If the parsing fails, raise a ValueError
        raise ValueError("Invalid date format. Please enter a date in the format 'YYYY-MM-DD'.")
