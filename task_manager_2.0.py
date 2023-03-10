# =====importing libraries===========

# Some text formatting codes


from datetime import datetime
from datetime import date
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
BOLD = '\033[1m'
WHITE = '\033[0m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
PINK = '\033[95m'

# Imports date class from datetime module


# ========function definitions=======

# Definition for user registration


def reg_user():

    print(f'{BLUE}User registration{WHITE}')

    # This condition only allows the admin to add new users.
    if login_user != 'admin':
        print(
            f'{PINK}\n⚠ You must be logged in as admin to register user.{WHITE}')
    else:
        print(f'{GREEN}\nUser registration login validated.{WHITE}')

        # This temporarily stores new username input.

        reg_username = input('\nEnter new username: ')

        # This checks that the username does not already exist.
        while reg_username in username_list:

            print(f'{PINK} \n⚠ This username already exits. Try again.{WHITE}')

            reg_username = input('\nEnter new username: ')

        # This temporarily stores new password input.
        reg_password = input('\nEnter new password: ')

        # This stores second entry of new password.
        check_password = input('\nRe-enter new password: ')

        # This checks/confirms both entries of new password are the same.
        if reg_password == check_password:

            # This ensures that the list of users is updated immediately after new user is added.
            username_list.append(reg_username)

            # This ensures that the list of passwords is also updated in realtime.
            password_list.append(reg_password)

            # Opens user.txt file for editting.
            file1 = open('user.txt', 'a+', encoding='utf-8')

            # Writes username and password in text file.
            file1.write('\n'+reg_username + ', ' + reg_password)

            file1.close()  # Closes the text file.

            print(f'{GREEN}\nRegistration succesful{WHITE}')

        else:
            print(
                f'{PINK}\n⚠ Registration unsuccesful. Password mismatch. Try again.{WHITE}')


# Definition for task assignment to users

def add_task():

    print(f'\n{BLUE}Task assignment.{WHITE}')

    # This temporarily stores username to be assigned a task.
    task_username = input('Enter the name of the user: ')

    if task_username in username_list:  # This Checks if username is registered.

        print(f'{GREEN}\nUsername validated!{WHITE}')

        task_title = input('\nEnter title for the task: ')

        task_description = input('\nEnter description for task: ')

        task_due = input('\nEnter task due date (dd mmm yyyy): ').title()

        date_today = date.today()  # imports today's date.

        # Converts date to dd mm yyyy format.
        task_date = date_today.strftime('%d %b %Y')

        # Stores default value for task completion as 'No'.
        task_complete = 'No'

        # Opens tasks.txt so txt can be added.
        file2 = open('tasks.txt', 'a+')

        # This writes the task details into tasks.txt.
        file2.write('\n' + task_username + ', ' + task_title + ', ' +
                    task_description + ', ' + task_due + ', ' + task_date + ', ' + task_complete)

        file2.close()  # Closes task.txt file.

        print(f'{GREEN}\nTask added succesfully.')

    else:
        print(
            f'{PINK}\n⚠ This user does not exist.Register user or contact IT Support.{WHITE}')


# Definition for view all tasks function.

def view_all():

    print(f'{BLUE}\nView all assignments.{WHITE}')

    # Opens tasks.txt for read-only.
    file2 = open('tasks.txt', 'r', encoding='utf-8')

    # TODO for number, line in enumerate(task_data, 1): for line in file2
    for number, line in enumerate(file2, 1):

        # Splits stored login details from txt into two parts.
        line_list = line.split(', ')

        print(f'''
{CYAN}════════════════════════════════{YELLOW}{BOLD}TASK NUMBER {number}{CYAN}══════════════════════════════════════{WHITE}

\nTask:                                                           {line_list[1]}
\nAssigned to:                                                    {line_list[0]}
\nDate assigned:                                                  {line_list[4]}
\nDue date:                                                       {line_list[3]}
\nTask complete?:                                                 {line_list[5]}
\nTask description:
\n{YELLOW}{line_list[2]}

{CYAN}════════════════════════════════════════════════════════════════════════════════════{WHITE}
''')

    file2.close()  # Closes task.txt file.


# Definition for view my task function

def view_mine():

    print(f'{BLUE}\nView my task.{WHITE}')

    # Opens tasks.txt for read-only.
    file2 = open('tasks.txt', 'r', encoding='utf-8')

    # Stores the entire content of tasks.txt in a list, line by line.
    task_data = file2.readlines()

    # loops through task data and counts and assigns number to each task.
    for number, line in enumerate(task_data, 1):

        # Splits stored login details from txt into two parts.
        line_list = line.split(', ')

        # This checks if the logged-in username is assigned/associated to any task(s), so it can be printed.
        # Alternatively we could have done if login_user == line_list[0]
        if login_user in line_list:
            print(f'''
{CYAN}════════════════════════════════{YELLOW}{BOLD}TASK NUMBER {number}{CYAN}══════════════════════════════════════{WHITE}

\nTask:                                                           {line_list[1]}
\nAssigned to:                                                    {line_list[0]}
\nDate assigned:                                                  {line_list[4]}
\nDue date:                                                       {line_list[3]}
\nTask complete?:                                                 {line_list[5]}
\nTask description:
\n{YELLOW}{line_list[2]}

{CYAN}════════════════════════════════════════════════════════════════════════════════════{WHITE}
''')

        file2.close()  # Closes task.txt file.


# This defines the function for overwritting tasks.txt with editted data.

def rewrite_task(list=[]):
    with open('tasks.txt', 'w') as file2:
        for line in list:
            # This overwrites the data in tasks.txt with new edited data.
            file2.write(line)


# This defines the view stats function.

def view_stats():

    # This condition only allows the admin to view statistics.
    if login_user != 'admin':
        print(
            f'{PINK}\n⚠ You must be logged in as admin to view statistics.{WHITE}')

    else:
        print(f'{GREEN}\n View statistics login validated.{WHITE}')

        print(f'{BLUE}\nStatistics{WHITE}')

        print(f"\n{CYAN}════════════════════════════════{YELLOW}{BOLD}TASK OVERVIEW{CYAN}══════════════════════════════════════{WHITE}")

        # The following opens task_overview.txt for read-only.
        file3 = open('task_overview.txt', 'r', encoding='utf-8')

        for line in file3:
            # Essential to remove all trailing white spaces to avoid \n included in lists.
            line = line.strip()
            line_list = line.split(', ')  # Converts each line into list.
            print(
                f"\n{line_list[0]}     {YELLOW}{line_list[1]}{WHITE}")

        file3.close()  # Closes user.txt file.

        print(f"\n{CYAN}════════════════════════════════{YELLOW}{BOLD}USER OVERVIEW{CYAN}══════════════════════════════════════{WHITE}")

        # The following opens user_overview.txt for read-only.
        file4 = open('user_overview.txt', 'r', encoding='utf-8')
        for line in file4:
            # Essential to remove all trailing white spaces to avoid \n included in lists.
            line = line.strip()
            line_list2 = line.split(', ')  # Converts each line into list.
            print(
                f"\n{line_list2[0]}     {YELLOW}{line_list2[1]}{WHITE}")

        file4.close()  # Closes tasks.txt file.

        print(f"\n{CYAN}════════════════════════════════{YELLOW}{BOLD}END OF REPORT{CYAN}══════════════════════════════════════{WHITE}")

# This defines the looong function to generate the task and user reports.


def generate_reports():
    # This condition only allows the admin to view statistics.
    if login_user != 'admin':
        print(
            f'{PINK}\n⚠ You must be logged in as admin to view statistics.{WHITE}')

    else:
        print(f'{GREEN}\n Generate reports login validated.{WHITE}')

        # --------------This block of code generates the task report----------------

        # These store variables to count number of tasks,completed,uncompleted and overdue tasks.
        tasks_count = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0
        percent_incomplete = 0
        percent_overdue = 0

        # The following finds today's date as datetime object.
        today = datetime.now()

        # Opens tasks.txt for read only.
        file2 = open('tasks.txt', 'r', encoding='utf-8')

        # Stores the entire content of tasks.txt in a list, line by line.
        task_data = file2.readlines()

        # The following loop counts number of tasks,completed,uncompleted and overdue tasks.
        for item in task_data:
            tasks_count += 1
            item_list = item.split(', ')
            if item_list[-1] == 'Yes\n' or item_list[-1] == 'Yes':
                completed_tasks += 1
            else:
                uncompleted_tasks += 1

            # The following loop checks and counts overdue uncompleted tasks.

            if item_list[-1] == 'No\n' or item_list[-1] == 'No':
                due_date = item_list[3]

                # Converts string due_date to datetime object for comparison
                due_datetime = datetime.strptime(due_date, "%d %b %Y")

                # Compares the dates
                if due_datetime < today:  # Or today > due date.
                    overdue_tasks += 1
                elif due_datetime > today:
                    pass
                else:
                    print(f"Some deadline date(s) may be in wrong format")

        # The following calculates (and rounds up) percentages for incomplete and orverdue tasks.
        # Try except handles zero division errors without affecting accuracy of calculations.
        try:
            percent_incomplete = (uncompleted_tasks/tasks_count)*100
        except:
            ZeroDivisionError: percent_incomplete = 0.0
        percent_incomplete = round(percent_incomplete, 1)
        try:
            percent_overdue = (overdue_tasks/uncompleted_tasks)*100
        except:
            ZeroDivisionError: percent_overdue = 0.0
        percent_overdue = round(percent_overdue, 1)

        file2.close()  # Closes tasks.txt file.

        # Te following opens/creates 'task_overview.txt.' and adds data.

        # Creates blank copy/resets file for editting.
        file3 = open('task_overview.txt', 'w+')
        file3.close()

        # Adds counted data line by line.
        file3 = open('task_overview.txt', 'a+')

        file3.write(f"Total number of tasks, {tasks_count}")
        file3.write(f"\nNumber of completed tasks, {completed_tasks}")
        file3.write(f"\nNumber of uncompleted tasks, {uncompleted_tasks}")
        file3.write(f"\nNumber of overdue tasks, {overdue_tasks}")
        file3.write(
            f"\nPercentage of incomplete tasks, {percent_incomplete}%")
        file3.write(f"\nPercentage of complete tasks, {percent_overdue}%")

        file3.close()

        print(f"\n{GREEN} Task report successfully generated.{WHITE}")

        # --------------This block of code generates the user report----------------

        # This stores total number of users
        total_users = len(username_list)

        # This will store username and number of task in pairs.
        number_tasks = {}

        # This will store username and number of uncompleted task in pairs.
        number_uncompleted = {}

        # This will store username and number of uncompleted task in pairs.
        number_completed = {}

        # This will store username and number of overdue task in pairs.
        number_overdue = {}

        # This will store username and percentage of tasks assigned in pairs.
        percent_alltasks = {}

        # This will store username and percentage of user completed tasks in pairs.
        percent_complete = {}

        # This will store username and percentage of user uncompleted tasks in pairs.
        percent_uncompleted = {}

        # This will store username and percentage of user overdue tasks in pairs.
        percent_overdue_user = {}

        for name in username_list:
            # Creates initial values for username/number of tasks
            number_tasks[name] = 0
            # Creates intial values for username and number of uncompleted task in pairs.
            number_uncompleted[name] = 0
            # Creates intial values for username and number of completed task in pairs.
            number_completed[name] = 0
            # Creates intial values for username and number of completed task in pairs.
            number_overdue[name] = 0
            # Creates initial values for username and percentage of tasks assigned in pairs.
            percent_alltasks[name] = 0
            # Creates initial values for username and percentage of user completed tasks in pairs.
            percent_complete[name] = 0
            # Creates initial values for username and percentage of user uncompleted tasks in pairs.
            percent_uncompleted[name] = 0
            # Creates initial values for username and percentage of user overdue tasks in pairs.
            percent_overdue_user[name] = 0

        # This opens tasks.txt for read-only.
        file2 = open('tasks.txt', 'r', encoding='utf-8')
        for line in file2:

            # Essential to remove all trailing white spaces to avoid \n included in lists.
            line = line.strip()

            # Splits stored task data into a list.
            task_data = line.split(', ')

            # Stores first word in line as username.
            username = task_data[0]

            # Stores last word in line (Yes or No)
            task_status = task_data[-1]

            # The following stores the date and converts to datetime object for comparison.
            due_date = task_data[3]
            due_datetime = datetime.strptime(due_date, "%d %b %Y")

            # The following counts number of tasks,completed, uncompleted and overdue tasks.

            if username in number_tasks:
                number_tasks[username] += 1

            if username in number_uncompleted and task_status == 'No':
                number_uncompleted[username] += 1
                if due_datetime < today:
                    number_overdue[username] += 1
            else:
                number_completed[username] += 1

            # The following calculates and stores various user percentage values.

        for username in username_list:

            # Percentage of total number of tasks assigned to each user.
            try:
                percent_alltasks[username] = (
                    number_tasks[username]/tasks_count)*100
            except:
                ZeroDivisionError: percent_alltasks = 0.0
            percent_alltasks[username] = round(
                percent_alltasks[username], 1)

            # Percentage of tasks assigned to user that has been completed by user.
            try:
                percent_complete[username] = (
                    number_completed[username]/number_tasks[username])*100
            except:
                ZeroDivisionError: percent_complete = 0.0
            percent_complete[username] = round(
                percent_complete[username], 1)

            # Percentage of tasks assigned to user that has yet to be completed by user.
            try:
                percent_uncompleted[username] = (
                    number_uncompleted[username]/number_tasks[username])*100
            except:
                ZeroDivisionError: percent_uncompleted = 0.0
            percent_uncompleted[username] = round(
                percent_uncompleted[username], 1)

            # Percentage of tasks assigned to user which is overdue completion date.
            try:
                percent_overdue_user[username] = (
                    number_overdue[username]/number_tasks[username])*100
            except:
                ZeroDivisionError: percent_overdue_user = 0.0
            percent_overdue_user[username] = round(
                percent_overdue_user[username], 1)

        file2.close()  # Closes the text file.

        # Creates blank copy/resets file for editting.
        file4 = open('user_overview.txt', 'w+')
        file4.close()

        # Adds counted data line by line.
        file4 = open('user_overview.txt', 'a+')

        file4.write(f"Total number of users, {total_users}")
        file4.write(f"\nTotal number of tasks, {tasks_count}")

        for username in username_list:
            file4.write(
                f"\nThe Total number of tasks assigned to {username} is, {number_tasks[username]}")
            file4.write(
                f"\nThe percentage of the total amount of tasks assigned to {username} is, {percent_alltasks[username]}%")
            file4.write(
                f"\nThe percentage of tasks completed by {username} is, {percent_complete[username]}%")
            file4.write(
                f"\nThe percentage of tasks not completed by {username} is, {percent_uncompleted[username]}%")
            file4.write(
                f"\nThe percentage of overdue tasks assigned to {username} is, {percent_overdue_user[username]}%")

        file4.close()  # Closes the text file.

        print(f"\n{GREEN} User report successfully generated.{WHITE}")


# ====Login Section====
username_list = []  # Stores initial and subsequent usernames.
password_list = []  # Stores initial and subsequent passwords.

# The following reads the regsitered usernames and passwords from user.txt
# and populates/updates the user and password lists from user.txt file.

# This opens user.txt for read-only.
file1 = open('user.txt', 'r', encoding='utf-8')
for line in file1:

    # Essential to remove all trailing white spaces to avoid \n included in lists.
    line = line.strip()

    # Splits stored login details from txt into two parts.
    login_data = line.split(', ')

    # Stores first part of login details as username.
    username = login_data[0]

    # Stores second part of login details as password.
    password = login_data[1]
    username_list.append(username)
    password_list.append(password)

file1.close()  # Closes the text file.


while True:

    print(f'{BLUE}\nWelcome to the login section.{WHITE}')

    # This stores user input into login_user variable.
    login_user = input('\nEnter username: ')

    # This stores user input into login_pass variable.
    login_pass = input('\nEnter password: ')

    try:
        # This tests if wether username and password can be found in username list and password list
        # and checks if they both have the same corresponding positions.
        if username_list.index(login_user) == password_list.index(login_pass):
            print(f'{GREEN}\nUsername and password accepted!{WHITE}')
            break
        else:
            print(f'{PINK}\n⚠ Invalid username or password. Try again.{WHITE}')

    except ValueError:  # This error handling tries to avoid crashes due to ValueError.
        print(f'{PINK}\n⚠ Invalid username or password. Try again.{WHITE}')


print("\n")

# This block presents the menu to the user and
# makes sure that the user input is converted to lower case.

while True:

    print(f'{BLUE}{BOLD}\nWELCOME TO THE MAIN MENU.{WHITE}')

    menu = input(f'''{BLUE}\nSelect one of the following Options below:
\n{YELLOW}r{WHITE} - Registering a user (admin only)
\n{YELLOW}a{WHITE} - Adding a task
\n{YELLOW}va{WHITE} - View all tasks
\n{YELLOW}vm{WHITE} - View my task
\n{YELLOW}gr{WHITE} - Generate reports (admin only)
\n{YELLOW}vs{WHITE} - View statistics (admin only)
\n{YELLOW}e{WHITE}- Exit
: {WHITE}''').lower()

    # This block allows new registration of user and password.

    if menu == 'r':
        reg_user()

    # This block allows tasks to be assigned to users.
    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

        # Opens tasks.txt for read only.
        file2 = open('tasks.txt', 'r', encoding='utf-8')

        # Stores the entire content of tasks.txt in a list, line by line.
        task_data = file2.readlines()

        file2.close()  # Closes tasks.txt file.

        print(f'''{BLUE}\nYou can make the following changes:
    \nMark a task as completed.  
    \nChange completion date for {YELLOW}uncompleted{BLUE} task.
    \nAssign {YELLOW}uncompleted{BLUE} task to different user.''')

        choice = int(input(
            f"\n{BLUE}Enter the task number you wish to edit or -1 to return to main menu:{WHITE} "))

        if choice == -1:
            continue  # Returns loop to main menu.

        elif choice > 0 and choice <= len(task_data):

            # Creates a single list item based on the user choice/task number.
            edit_data = task_data[choice - 1]

            # Splits the single list into indexed items that can be changed.
            edit_data_list = edit_data.split(', ')

            # This section checks that the task is not already completed and allows user to edit task completion.

            # Ensures that completed tasks cannot be edited.
            if edit_data_list[-1] == "Yes\n" or edit_data_list[-1] == "Yes":

                print(
                    f"\n{PINK}This task is already completed and cannot be edited{WHITE}")

                continue  # Returns loop to main menu.

            # This checks that the task is not yet completed
            elif edit_data_list[-1] == "No\n" or edit_data_list[-1] == "No":

                print(
                    f"\n{BLUE}Do you want to mark this task as complete?{WHITE}")

                print(
                    f"{PINK}\nIf task is marked as complete, you cannot make any further changes.{WHITE}")

                choice_2 = input(
                    f"\n{BLUE}Enter {YELLOW}Y{BLUE} to complete task or {YELLOW}N{BLUE} to leave task uncompleted: {WHITE}").lower()

                if choice_2 == "y":

                    # Changes last item in edit_data_list ("No") to "Yes".
                    edit_data_list[-1] = "Yes\n"

                    print(
                        f"\n{GREEN}The task has been succesfully marked as completed.{WHITE}")

                    # Joins the list items together as 1 item.
                    edit_data = ', '.join(edit_data_list)

                    # Replaces the item in task_data with new edited item.
                    task_data[choice - 1] = edit_data

                    # Applies my function to rewrite task.txt with edited data.
                    rewrite_task(task_data)

                    continue  # Returns loop to main menu.

                elif choice_2 == "n":
                    print(
                        f"\n{GREEN}No changes have been made to task completion.{WHITE}")

                else:
                    print(f"{PINK}\n⚠ Wrong entry. Please try again.{WHITE}")
                    continue  # Returns loop to main menu.

                # This section allows the user to change completion date.

                print(f"{BLUE}\nDo you want to change the task completion date?")

                choice_3 = input(f"\nEnter Y or N: {WHITE}").lower()
                if choice_3 == "y":

                    new_date = input(
                        f"\n{BLUE}Enter the new task completion date in format DD MMM YYYY:{WHITE} ")

                    # Changes 3rd item(date) to new completion date/deadline.
                    edit_data_list[3] = new_date

                    print(
                        f"\n{GREEN}The task date has been succesfully changed.{WHITE}")

                    # Joins the list items together as 1 item.
                    edit_data = ', '.join(edit_data_list)

                    # Replaces the item in task_data with new edited item.
                    task_data[choice - 1] = edit_data

                    # Applies my function to rewrite task.txt with edited data.
                    rewrite_task(task_data)

                elif choice_3 == "n":
                    print(
                        f"\n{GREEN}No changes have been made to task completion date.{WHITE}")

                else:
                    print(f"{PINK}\n⚠ Wrong entry. Please try again.{WHITE}")

                # This section allows the user to assign the task to a new user.
                print(f"{BLUE}\nDo you want to assign the task to a different user?")

                choice_4 = input(f"\nEnter Y or N:{WHITE} ").lower()

                if choice_4 == "y":
                    new_user = input(
                        f"\nEnter name of user you want to re-assign task to: {WHITE}")

                    if new_user in username_list:

                        # Changes 1st item(username) to different user.
                        edit_data_list[0] = new_user

                        print(
                            f"\n{GREEN}The task has been succesfully re-assigned.{WHITE}")

                        # Joins the list items together as 1 item.
                        edit_data = ', '.join(edit_data_list)

                        # Replaces the item in task_data with new edited item.
                        task_data[choice - 1] = edit_data

                        # Applies my function to rewrite task.txt with edited data
                        rewrite_task(task_data)

                    else:
                        print(
                            f"{PINK}\n⚠ This user is not registered or does not exist.Please try again.{WHITE}")

                elif choice_4 == "n":
                    print(
                        f"\n{GREEN}No changes have been made to assigned user of the task.{WHITE}")

                else:
                    print(f"{PINK}\n⚠ Wrong entry. Please try again.{WHITE}")

        else:
            print(f"{PINK}\n⚠ Wrong entry. Please try again.{WHITE}")

    elif menu == 'gr':
        generate_reports()

    elif menu == 'vs':
        generate_reports()
        view_stats()

    elif menu == 'e':
        print('\nGoodbye!!!👋')
        exit()

    else:
        print(f"{PINK}\n⚠ This option does not exist, Please Try again.")
