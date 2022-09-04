from datetime import date
import os
import time

def now(db):
    os.system('cls')
    Id = input('Todo Erase\n\n(To Clear list, type PURGE in caps.)\nID: ')

    if Id == 'PURGE':
        db.delete_many({})
    else:
        test = db.find_one({'docID': Id})
        if test == None:
            print('\n\nNo such entry found in todo list?')
            time.sleep(2.3)
        else:
            db.find_one_and_delete({'docID': Id})
