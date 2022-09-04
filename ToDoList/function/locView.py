from rich.console import Console
from rich.table import Table
import os
import function.calDate as calDate
import function.calSort as calSort

def now(db):
    AllTasks = []
    os.system('cls')
    print('<ProcMonitior> Getting Data..')
    tasks = None
    sortType = calSort.Get_Sort_Type()
    if sortType[0] == None:
        tasks = db.find({})
    else:
        tasks = db.find({}).sort(sortType[0], sortType[1])

    for document in tasks:
        dID = str(document['docID'])
        dTitle = document['docTitle']
        dDesc = document['docDesc']
        dDue = document['docDue']
        dDue = calDate.display_time(dDue)
        listAppend = (dID, dTitle, dDesc, dDue)
        AllTasks.append(listAppend)
    
    print('<ProcMonitior> Creating List..')
    table = Table(title='Todo Tasks', caption='Use control keys To <A>DD or <D>ELETE an entry. X to exit.\n<H>elp')
    table.add_column('ID', justify="center", style='green')
    table.add_column('Task', justify="center", style='cyan')
    table.add_column('Note', justify="left")
    table.add_column('Due', justify="left", style="#E4961E")

    print('<ProcMonitor> Formatting View')
    for task in AllTasks:
        table.add_row(task[0], task[1], task[2], task[3])
    
    print('<ProcMonitor> Rendering Data..')
    os.system('cls')
    console = Console()
    console.print(table)