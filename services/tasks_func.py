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
    return tasks_sheet.col_values(TASK_COLUMN_INDEX)

def get_all_due_dates():
    return tasks_sheet.col_values(DUE_DATE_COLUMN_INDEX)

def get_all_priorities():
    return tasks_sheet.col_values(PRIORITY_COLUMN_INDEX)

def get_all_status():
    return tasks_sheet.col_values(STATUS_COLUMN_INDEX)


def show_priority_label(priority):
    if priority == '1':
        return "High Priority"
    elif priority == '2':
        return "Mid Priority"
    else :
        return "Low Priority"
    
def show_status_label(status):
    if status == '1':
        return f"{Colors.GREEN} Yes {Colors.RESET}"
    else :
        return f"{Colors.RED} No {Colors.RESET}"
    

def get_tasks_per_date(username , date):
    # get user id 
    user_id = user.get_user_id_per_username(username)
    # retieve data from excel sheet 
    ids = get_all_users_id()
    tasks = get_all_tasks()
    due_dates = get_all_due_dates()
    priorities = get_all_priorities()
    status = get_all_status()
    # check if there is  tasks with the date provided 
    tasks_data = []
    for i in range(len(ids)): 
        if ids[i] == user_id and due_dates[i] == str(date):
            tasks_data.append([tasks[i],show_priority_label(priorities[i]),show_status_label(status[i])])
    # return this tasks
    return tasks_data