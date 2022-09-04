import csv
import os
from time import sleep

preDir = ''

def Write_To_CSV(db):
    global preDir
    os.system('cls')
    AllTasks = [['Id', 'Task', 'Note', 'Due (Unix Timestamp)']]
    tasks = db.find({})

    for document in tasks:
        dID = str(document['docID'])
        dTitle = document['docTitle']
        dDesc = document['docDesc']
        dDue = document['docDue']
        listAppend = [dID, dTitle, dDesc, dDue]
        AllTasks.append(listAppend)

    if preDir == '':
        print("""Todo CSV

Please enter the FULL directory path of where to save the file.
->  Ex. C:\\Users\\JohnD\\Documents
---""")

        preDir = input('\n\nDirectory: ')
    
    else:
        print("""Todo CSV
        
It seems like you already have a last used directory:
->  {}

Press enter to use the directory shown above or enter a new one to use.
---""".format(preDir))

        checkDir = input('\n\nDirectory: ')
        if checkDir != '':
            preDir = checkDir
        
    #Now we save the entries into a CSV file

    saveToDir = str(preDir) + '/Dynamic-Todo.csv'
    
    try:
        with open(saveToDir, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(AllTasks)
            print('\n(i) Data saved to CSV')
    except:
        print('\n(!) An error occured while writing and saving data to the csv file.')
    
    sleep(1.3)