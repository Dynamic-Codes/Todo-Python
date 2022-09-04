import os

persistent_sort = [None, None]
sortby = 'defualt'
def Get_Sort_Type(edit_mode=False):
    os.system('cls')
    global persistent_sort
    filterby_types = ['A', 'B', 'C', 'D']
    sortby_types = [1, 2]
    
    if edit_mode == True:
        while True:
            print("""Todo Filter
Please choose what you want to filter the tasks by:

    <A> Default
    <B> Order by 'Due Date'
    <C> Order by 'Task Name'
    <D> Order by 'Note'
    ---
    (!) You will be given an option to sort by Ascending/Descending later unless you option A.
    ---
    """)
            sortby = input('Choice: ').upper()
            if sortby not in filterby_types:
                os.system('cls')
                print('Invalid Option: Choose ONE from [A, B, C, D].')
            else:
                break
        
        os.system('cls')

        while True:
            if sortby == 'A':
                break

            print("""Todo Filter

Select either to sort by Ascending order or Descending order.

    <1> Sort by Ascending Order
    <2> Sort by Decending Order
    ---
""")

            altitude = int(input('Choice: '))
            if altitude not in sortby_types:
                os.system('cls')
                print('Invalid Option: choose either 1 or 2.')
            else:
                break

        #Now we return the correct sort types using dict and keys

        orderDic = {
            'B': 'docDue',
            'C': 'docTitle',
            'D': 'docDesc',
            #This is for the altitude
            1: 1,
            2: -1
        }

        if sortby == 'A':
            persistent_sort = [None, None]
            return persistent_sort
        else:
            arg1 = orderDic.get(sortby)
            arg2 = orderDic.get(altitude)
            persistent_sort = [arg1, arg2]
            return persistent_sort
    else:
        return persistent_sort
