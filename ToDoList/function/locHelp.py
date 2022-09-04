import os
from rich.console import Console
from rich.table import Table

def Wiki():
    os.system('cls')
    username = os.getlogin()
    console = Console()
    
    print("""Todo Helper

Hey {}! View the help menu below.
\n\n""".format(username))

    table1 = Table(title='Basic Controls')
    table1.add_column('Key', justify="center", style='cyan')
    table1.add_column('Action', justify="center", style='white')
    table1.add_column('Description', justify="left", style='green')
    table1.add_row('A', 'Add', 'Create a new entry for your todos')
    table1.add_row('D', 'Delete', 'Delete a valid entry in the todo app')
    table1.add_row('H', 'Help', 'Bring up Todo Helper')
    table1.add_row('X', 'Exit', 'Close and exit the program')
    console.print(table1)

    print('\n')

    table2 = Table(title='More Features', caption='Enter to Dismiss')
    table2.add_column('Key', justify="center", style='cyan')
    table2.add_column('Action', justify="center", style='white')
    table2.add_column('Description', justify="left", style='green')
    table2.add_row('S', 'Sort', 'Sort the entries on screen via columns')
    table2.add_row('C', 'CSV', 'Export Todos as a CSV File')
    table2.add_row('E', 'Email', 'export entries via email')
    console.print(table2)

    input('')