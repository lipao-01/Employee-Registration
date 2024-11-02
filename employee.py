# importing the tabulate library to format the data into a table
from tabulate import tabulate

# library to interact with the operating system
import os 


# initializing our employee class
class Employee:
    def __init__(self, name, area, wage):
        # Initializes the properties of the employee: name, area, and wage
        self.name = name
        self.area = area
        self.wage = wage

# initializing our system class
class System:
    def __init__(self, data):
        # Stores the employee data
        self.data = data
        # Defines the file path where the employee data will be saved
        self.file_patch = 'Employee.txt'
        # Creates the file if it does not exist
        self.creat_file_if_not_exists()
        # Loads existing data from the file
        self.load_data()

    def creat_file_if_not_exists(self):
        # Checks if the file already exists
        if not os.path.exists(self.file_patch):
            # If it does not exist, creates a new empty file
            open(self.file_patch, 'w').close()

    def load_data(self):
        # Loads data from the text file
        with open(self.file_patch, 'r') as file:
            # Reads each line from the file
            for line in file:
                # Strips whitespace and splits the line into parts using the '|' character
                parts = line.strip().split('|')
                # Checks if the line has the correct number of parts
                if len(parts) == 4:
                    id = int(parts[0])  # Converts the first part to an integer (ID)
                    name = parts[1]      # Retrieves the name
                    area = parts[2]      # Retrieves the area
                    wage = parts[3]      # Retrieves the wage
                    # Appends the parsed data to the employee data list
                    self.data.append([id, name, area, wage])

    def save_data(self):
        # Saves the current employee data to the text file
        with open(self.file_patch, 'w') as file:
            # Iterates over each employee in the data list
            for employee in self.data:
                # Joins the employee data into a single line separated by '|'
                line = '|'.join(map(str, employee))
                # Writes the line to the file
                file.write(line + '\n')

    def home(self):
        # Main loop for the program interface
        while True:
            head = ['ID', 'NAME', 'AREA', 'WAGE']  # Header for the employee table
            # Prints the employee data in a table format
            print(tabulate(self.data, headers=head, tablefmt='grid'))
            print('\n[1] Register Employee [2] Edit Employee [3] Delete Employee [4] Exit program')
            # Prompts user to select an option
            self.option_home = int(input('Enter your option: '))

            # Calls the appropriate method based on user input
            if self.option_home == 1:
                self.register()
            elif self.option_home == 2:
                self.edit()
            elif self.option_home == 3:
                self.delete()
            elif self.option_home == 4:
                print('Exiting the program...')
                break
            else:
                print(f'\033[31mInvalid option. Please try again.\033[m')

    def register(self):
        # Registration method for adding a new employee
        if self.option_home == 1:
            while True:
                id = len(self.data) + 1  # Incremental ID based on current data length
                # Prompts user for employee name, area, and wage
                name = str(input('\nEnter the employee name: ').title())
                area = input('Enter the employee area: ').upper()
                wage = float(input('Enter the employee wage: '))
                print('-' * 40)
                
                # Appends new employee data to the list
                self.data.append([id, name, area, f'R$ {wage:,.2f}'])
                self.save_data()  # Saves data after registration

                # Asks the user if they want to edit any employee
                option = ''
                while option not in ['S', 'N']:
                    option = input('\033[31mDo you wish to edit any employee? [S/N] \033[0m').upper()
                print('-' * 40)
                if option == 'N':
                    break

    def edit(self):
        # Editing method for modifying existing employee data
        if self.option_home == 2:
            edit = int(input('Enter the ID of the employee you want to edit: '))
            # Checks if the entered ID is valid
            if 1 <= edit <= len(self.data):
                print(f'Current data: {self.data[edit - 1]}')

                # Prompts user for new employee data
                name = str(input('Enter the new employee name: ')).title()
                area = str(input('Enter the new employee area: ')).upper()
                wage = float(input('Enter the new employee wage: '))

                # Updates the employee data in the list
                self.data[edit - 1] = [edit, name, area, f'R$ {wage:,.2f}']
                self.save_data()  # Saves data after editing
                print('\033[32mEmployee data updated successfully!\033[m')
            else:
                print('Invalid ID. Please enter a valid ID.')

    def delete(self):
        # Deleting method for removing an employee from the data
        delete_id = int(input('Enter the ID of the employee you want to delete: '))
        # Checks if the entered ID is valid
        if 1 <= delete_id <= len(self.data):
            remove_employee = self.data[delete_id - 1]  # Stores the employee data to be removed
            confirm = input(f'Are you sure you want to delete employee {remove_employee}? [Y/N] ').upper()

            # Confirms deletion
            if confirm == 'Y':
                self.data.pop(delete_id - 1)  # Removes the employee from the list
                self.save_data()  # Saves data after deletion
                print(f'Employee {remove_employee} has been removed.')
            else:
                print('Employee deletion canceled.')
        else:
            print('Invalid ID. Please enter a valid ID.')


# Initializes an empty list for employee data
data = []
# Creates an instance of the System class with the empty data list
system = System(data)
# Starts the program's home interface
system.home()