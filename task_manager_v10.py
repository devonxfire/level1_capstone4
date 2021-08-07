

'''
NOTE TO EVALUATER:

- Updated this so that if a task is already complete, the user cannot edit it
- I don't get a runtime error when changing a task complete from No to Yes, so not sure how to fix that, but still seems to work
- Added percent of tasks complete per user
- Added percent of tasks incomplete per user
- Added users who's tasks are both incomplete and overdue
'''

# Searched for how to get the current date - https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import date

import os


def start():
    # Opening user.txt in read/write mode to variable user_file
    user_file = open("user.txt", "r+")

    # Login initially set to False
    login = False

    # While loop until login = True
    while login == False:
        # Asking user to enter user name and password
        user_name = input("\nPlease enter your username: ")
        user_password = input("Please enter your password: ")

        # Reading all the lines in user_file
        for line in user_file.readlines():
            # Unpacking 2 variables that are cast to list, separated by ", "
            valid_user, valid_password = line.strip().split(", ")
            # Login value changes to True if valid login
            if user_name == valid_user and user_password == valid_password:
                    login = True
        # Getting cursor back to beginning of the file
        user_file.seek(0)

        # If login False, user requested to re-enter valid credentials
        if login == False:
            print("Incorrect login details, please enter a valid username and password")
        # Getting cursor back to beginning of the file
        user_file.seek(0)

    # Menu options displayed for valid user if not 'admin'
    if user_name != 'admin':

        # def main_menu():
        menu_choice = input("""
Please select one of the following options:
r - register user (must be signed in as 'admin')
a - add task
va - view all tasks
vm - view my tasks
e - exit
""")

    # Menu choice for admin user
    else:
        # def main_menu_admin():
            menu_choice = input("""
Welcome to the Admin Menu

Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
""")

    # Defining reg_user function
    def reg_user(r):

        # Opening user file
        user_file = open("user.txt", "r+")
        new_user = input("Please enter your new username: ")
        # Unique user check - set by default to False
        unique_user = False
        # User name list - users will be appended to this list
        username_list = []

        # While loop for False
        while unique_user == False:

            # Splitting user name and password
            for line in user_file.readlines():
                user_name, password = line.strip().split(", ")
                username_list.append(user_name)

            # For loop on user list
            for user in username_list:
                # If user name unique then unique_user = True
                if new_user != user:
                    unique_user = True
                # If not unique, enter user name again
                if new_user == user:
                    print('This user name is already taken. Please enter a new user name: ')
                    reg_user('r')

        if unique_user == True:

            # If While loop broken, then password process starts
            new_password = input("Please enter your new password: ")
            # User must confirm password
            password_confirm = input("Please confirm your new password: ")

            # Writes new user name and password to user.txt
            if new_password == password_confirm:
                user_file.write(f"\n{new_user}, {new_password}")

                print("You have successfully registered a new user!")


            # Password confirmation
            else:
                print("Your confirmation password doesn't match, please try again")
                reg_user('r')
                # Closing user_file
            user_file.close()


    # Calling function if 'r' selected
    if menu_choice == "r" and user_name == 'admin':
        reg_user('r')


    # Error message if user is not admin and tries to register new user
    if menu_choice == "r" and user_name != 'admin':
        print("Only admin user is allowed to register new users! Please login again: ")
        start()

    # Defining add_task function
    def add_task(a):
            # If user wants to add a task


        tasks_file = open("tasks.txt", "r")
        line_count = 1
        # When there is a new line, the line count goes up by 1
        for line in tasks_file:
            if line != "\n":
                line_count += 1
        tasks_file.close()

        # Opening tasks.txt as variable tasks_file
        tasks_file = open("tasks.txt", "a+")
        # Set of user inputs to generate task details
        user_task = input("What is the name of the user you are assigning this task to?: ")
        task_name = input("What is the name of this task?: ")
        task_description = input("Please describe the task: ")
        # Getting today's date
        today = date.today()
        date_today = today.strftime("%d/%m/%Y")
        due_date = input("What date is this task due to be completed? (dd/mm/yyyy): ")
        task_complete = "No"

        # Writing all the inputs in order, to tasks.txt
        tasks_file.write(f"\n{line_count}, {user_task}, {task_name}, {task_description}, {date_today}, {due_date}, {task_complete}")
        # Closing tasks_file
        tasks_file.close()
    # Calling function if user selects 'a'
    if menu_choice == "a":
        add_task('a')

    # Defining view_all function
    def view_all(va):
    # If user wants to view all tasks

        # Opening tasks.txt in read mode
        tasks_file = open("tasks.txt", "r")
        # Fetching all the tasks info unpacked as list
        for line in tasks_file:
            line_count, user_task, task_name, task_description, date_today, due_date, task_complete = line.split(", ")
    # Printing the list values
            print(f"""
    Task Number: {line_count}
    Name: {user_task}
    Task Name: {task_name}
    Task Description: {task_description}
    Date Today: {date_today}
    Due Date: {due_date}
    Task Completed: {task_complete}             
    """)
    # Calling function if 'va' selected
    if menu_choice == "va":
        view_all('va')
        # Letting user login and return to main menu (don't know how to go straight to menu without login)
        print("Please login again to return to the main menu\n")
        start()

    # Defining view_mine function
    def view_mine(vm):
        # If user wants to see their specific task/s

        # Opening and reading from tasks.txt
        tasks_file = open("tasks.txt", "r")
        # Fetching all the tasks info unpacked as list
        for line in tasks_file:
            line_count, user_task, task_name, task_description, date_today, due_date, task_complete = line.split(
                ", ")
            # Will print out only tasks for the logged in user
            if user_task == user_name:
                print(f"""
Task Number: {line_count}
Name: {user_task}
Task Name: {task_name}
Task Description: {task_description}
Date Today: {date_today}
Due Date: {due_date}
Task Completed: {task_complete}             
 """)

    # Calling function if 'vm' selected
    if menu_choice == "vm":
        view_mine('vm')

        # Opening and reading from tasks.txt
        tasks_file = open("tasks.txt", "r")
        task_number_list = []

        # Getting user input for task number
        vm_menu = input(
            "Please enter the number of the task you would like to edit, or enter '-1' to return to the main menu: ")

        # Fetching all the tasks info unpacked as list
        for line in tasks_file:
            task_number = line[0]
            task_number_list.append(task_number)
            line_count, user_task, task_name, task_description, date_today, due_date, task_complete = line.split(", ")


            # Fetching the specific task
            if task_number == vm_menu and user_task == user_name:

                task_stripped = task_complete.strip()
                # User can only edit task if task is not completed
                if task_stripped == 'No':


                    # User can change task completion to 'Yes' or view more options
                    task_edit_input = input(f"""
Would you like to mark Task {line_count} as complete?
Please enter 'Yes' Or type 'No' for more edit options: """).lower()


                    # Asking user if they want to edit task to 'completed'
                    if task_edit_input == 'yes':

                        tasks_file = open("tasks.txt", "r+")
                        vm_menu_int = int(vm_menu)
                        all_tasks_list = []
                        task_complete = 'Yes'

                        for line in tasks_file:
                            all_tasks_list.append(line)
                            line_count, user_task, task_name, task_description, date_today, due_date, task_complete = line.strip().split(
                                ", ")
                        # Replacing line of task with task complete set to 'Yes'
                        all_tasks_list[vm_menu_int - 1] = all_tasks_list[vm_menu_int - 1].replace("No", "Yes")
                        # Revised tasks content as string
                        revised_tasks = "".join(all_tasks_list)

                        # Writing the new tasks
                        tasks_file = open("tasks.txt", "w")
                        tasks_file.write(f"{revised_tasks}")

                        tasks_file.close()

                    # Further edit options for user
                    if task_edit_input == 'no':

                        user_or_date = input("""
Please enter 'User' if you would like to change the name of the user this task is assigned to
Please enter 'Date' if you would like to change the due date for this task: """).lower()
                        # User want sto change the name of the user the task is assigned to
                        if user_or_date == 'user':

                            new_user_name = input("Please enter the user this task should be assigned to: ")

                            tasks_file = open("tasks.txt", "r+")
                            vm_menu_int = int(vm_menu)
                            all_tasks_list = []

                            new_list = []
                            # Creating list of tasks
                            for line in tasks_file:
                                line_count, user_task, task_name, task_description, date_today, due_date, task_complete = line.split(", ")
                                new_list.append(line)
                                if vm_menu in line[0]:
                                    # Changes the name of the task user is assigned to with 'new_user_name' input
                                    new_line = line_count, new_user_name, task_name, task_description, date_today, due_date, task_complete
                                    new_line2 = ", ".join(new_line)
                                    new_list.append(new_line2)
                            # Removes old line
                            new_list.pop(vm_menu_int-1)
                            new_list_string = "".join(new_list)

                            tasks_file = open("tasks.txt", "r+")

                            tasks_file.write(new_list_string)

                            tasks_file.close()

                        # Changing the due date
                        if user_or_date == 'date':

                            new_date_input = input("Please enter the new due date (dd/mm/yyyy): ")

                            tasks_file = open("tasks.txt", "r+")
                            vm_menu_int = int(vm_menu)
                            all_tasks_list = []

                            new_list = []

                            for line in tasks_file:
                                line_count, user_task, task_name, task_description, date_today, due_date, task_complete = line.split(", ")
                                new_list.append(line)
                                if vm_menu in line[0]:
                                    # Line replaced with new due date input
                                    new_line = line_count, user_task, task_name, task_description, date_today, new_date_input, task_complete
                                    new_line2 = ", ".join(new_line)
                                    new_list.append(new_line2)
                            new_list.pop(vm_menu_int-1)
                            new_list_string = "".join(new_list)


                            tasks_file = open("tasks.txt", "r+")

                            tasks_file.write(new_list_string)

                            tasks_file.close()

                # If the task is already completed, they can't edit and are returned to the main menu
                if task_stripped == 'Yes':
                    print("\nThis task is already marked as complete! Only incomplete tasks can be edited. You will now be returned to the main menu")
                    start()



        # Returning to main menu
        if vm_menu == '-1':
            start()

        tasks_file.close()
        tasks_file.close()

    def view_stats(ds):
        #OS module can check if file exists
        os.path.isfile("task_overview.txt")

        if os.path.isfile("task_overview.txt") == True:

            task_overview_file = open("task_overview.txt", "r")
            # Reads all content in the file
            content_to_file = task_overview_file.read()
            print("\n*** TASK OVERVIEW ***\n")
            print(content_to_file)

            task_overview_file.close()
        # If file doesn't exist, then a new file is created
        if os.path.isfile("task_overview.txt") == False:

            print("This file doesn't exist, we have now created it")
            task_overview_file = open("task_overview.txt", "w")


        os.path.isfile("user_overview.txt")

        if os.path.isfile("user_overview.txt") == True:

            user_overview_file = open("user_overview.txt", "r")

            content_uo_file = user_overview_file.read()
            print("\n*** USER OVERVIEW ***\n")
            print(content_uo_file)

            user_overview_file.close()

        if os.path.isfile("user_overview.txt") == False:

            print("\n*** USER_OVERVIEW.TXT file doesn't exist, we have now created it ***")
            user_overview_file = open("user_overview.txt", "w")


    if menu_choice == "ds":
        view_stats('ds')

    # Defining generate_report function
    def generate_report(gr):

        task_overview_file = open("task_overview.txt", "w+")
        # Opening and reading tasks.txt
        tasks_file = open("tasks.txt", "r")
        # Line count starts at zero
        line_count = 0
        line_list = ""
        # When there is a new line, the line count goes up by 1
        for line in tasks_file:
            if line != "\n":
                line_count += 1

        tasks_file.close()

        tasks_file = open("tasks.txt", "r")
        # Counting how many tasks incomplete
        no_count = 0

        for line in tasks_file:
            task_complete_list = line.strip().split(", ")

            for i in task_complete_list:
                if i == 'No':
                    no_count += 1

        task_overview_file.write(f"TOTAL NUMBER OF TASKS: \nThere are currently a total of {line_count} tasks")
        task_overview_file.write(f"\n\nTOTAL NUMBER OF COMPLETED TASKS:\nThere are currently {line_count-no_count} complete tasks")
        task_overview_file.write(f"\n\nTOTAL NUMBER OF INCOMPLETE TASKS:\nThere are currently {no_count} incomplete tasks")
        task_overview_file.write(f"\n\nTOTAL % OF INCOMPLETE TASKS:\n{no_count/line_count*100}% of tasks are incomplete")

        user_overview_file = open("user_overview.txt", "w+")

        tasks_file = open("tasks.txt", "r")
        # Line count starts at zero
        line_count = 0
        # When there is a new line, the line count goes up by 1
        for line in tasks_file:
            if line != "\n":
                line_count += 1


        # Closing the tasks file
        tasks_file.close()

        # Opening and reading the user.txt file
        user_file = open("user.txt", "r")
        # User count starts at zero
        user_count = 0
        # When there is a new line, the line count goes up by 1
        for line in user_file:
            if line != "\n":
                user_count += 1

        # Writing registered users and total tasks to file
        user_overview_file.write(f"TOTAL NUMBER OF REGISTERED USERS:\nThere are currently {user_count - 1} registered users excluding admin user")
        user_overview_file.write(f"\n\nTOTAL NUMBER OF TASKS:\nThere are currently {line_count} tasks")

        tasks_file = open("tasks.txt", "r")
        user_count = 0
        user_list = []
        completed = 0
        success_list =[]
        success_count = 0

        result_list = []
        result_list_percent = []
        result_list_no_percent = []

        for line in tasks_file:

            line_count, user_task, task_name, task_description, date_today, due_date, task_complete = line.strip().split(", ")

            user_list.append(user_task)
            if user_task in user_list:
                user_count += 1

            if task_complete == 'Yes':
                task_completed = 1

            if task_complete == 'No':
                task_completed = 0

            dict = {user_task: task_completed}


            user_list_task_count = []
            user_list_task_percentage = []

            # Created a user list
            for user in user_list:
                # Counts number of times user has a task
                result = user_list.count(user)
                line_count_int = int(line_count)
                # Working out number and % of tasks assigned to specific user
                result_percentage = result / line_count_int * 100
                user_list_task_count.append(f'{user} has {result} tasks assigned to them')
                user_list_task_percentage.append(f'{user} has {result_percentage}% of tasks assigned to them')
            # Iterating through dictionary keys and values to get % tasks complete/incomplete
            for x in dict.keys():
                for y in dict.values():
                    result_list_percent.append(
                        f"{x} has completed {int(y / result * 100)}% of the tasks assigned to them")
                    result_list_no_percent.append(
                        f"{x} still needs to complete {100 - int(y / result * 100)}% of the tasks assigned to them")
                    # result_list.append(f"{x} has completed {y} tasks out of {result}")

        result_list_percent_join = "\n".join(result_list_percent)
        result_list_no_percent_join = "\n".join(result_list_no_percent)

        new_user_task_status_list = []
        new_user_list_task_percentage = []

        for user in user_list_task_count:
            if user not in new_user_task_status_list:
                new_user_task_status_list.append(user)


        for user in user_list_task_percentage:
            if user not in new_user_list_task_percentage:
                new_user_list_task_percentage.append(user)

        new_user_task_status = "\n".join(new_user_task_status_list)
        new_user_list_task_percentage = "\n".join(new_user_list_task_percentage)


        # Overdue Check

        tasks_file = open("tasks.txt", "r")

        task_list_expired = []

        today = date.today()
        date_today_actual = today.strftime('%d%m%Y')
        # Reversed date to get an integer number of the date
        date_today_actual_rev = date_today_actual[4::] + date_today_actual[2:4] + date_today_actual[0:2]

        expired_count = 0

        user_date_list = []
        overdue_list = []
        user_count = []

        for line in tasks_file:

            line_count, user_task, task_name, task_description, date_today, due_date, task_complete = line.split(", ")
            # Removing the slash in the dates
            due_date_no_slash = due_date.replace("/", "")
            due_date_rev = due_date_no_slash[4::] + due_date_no_slash[2:4] + due_date_no_slash[0:2]
            task_complete_stripped = task_complete.strip()
            date_today_actual_rev_int = int(date_today_actual_rev)
            due_date_rev_int = int(due_date_rev)
            user_date_list.append(user_task)

            # Checking if date is overdue
            if date_today_actual_rev_int > due_date_rev_int and task_complete_stripped == 'No':
                expired_count += 1

                overdue_list.append(f"{user_task} has {expired_count} tasks which are incomplete and also overdue")


        if task_complete_stripped == 'No':
            expired_count -= 1

        overdue_list_join = "\n".join(overdue_list)

        task_overview_file = open("task_overview.txt", "a")
        task_overview_file.write(f"\n\nTASKS THAT ARE OVERDUE AND INCOMPLETE:\nThere are {expired_count} tasks that are overdue and have not yet been completed")
        task_overview_file.write(f"\n\nTOTAL % OF TASKS OVERDUE AND INCOMPLETE:\n{expired_count/line_count_int*100}% of tasks are overdue and incomplete")

        task_overview_file.close()


        # Writing user stats to file
        user_overview_file.write(f"\n\nTOTAL TASKS ASSIGNED PER USER:\n{new_user_task_status}")
        user_overview_file.write(f"\n\nTOTAL % OF TASKS ASSIGNED PER USER:\n{new_user_list_task_percentage}")
        user_overview_file.write(f"\n\nPERCENTAGE OF TASKS COMPLETED PER USER\n{result_list_percent_join}")
        user_overview_file.write(f"\n\nPERCENTAGE OF INCOMPLETE TASKS PER USER\n{result_list_no_percent_join}\n")
        user_overview_file.write((f"\nTASKS INCOMPLETE AND OVERDUE\n{overdue_list_join}"))

        tasks_file.close()

        print("Your reports have been generated in the files task_overview.txt and user_overview.txt")

        user_file.close()
        task_overview_file.close()
        user_overview_file.close()

    # Calling function if 'gr' selected
    if menu_choice == 'gr':
        generate_report('gr')
# Calls login function
start()


