import os
import secrets
import datetime

def dateValidate(date):
    try:
        dateCorrrected = datetime.datetime.strptime(date, '%d-%m-%Y').timestamp()
        return dateCorrrected
    except:
        print('\n\n<!> The date format should be in dd-mm-yyyy')
        return False

def now(db):
    os.system('cls')
    title = input('Todo Pen\n\n(An Id will be auto generated)\nTask: ')
    desc = input('Note: ')
    dateDue = 'Never'
    while True:
        dDue = input('Date Due: ')

        if dDue != '0':
            dmy = dateValidate(dDue)
            if  dmy != False:
                dateDue = int(dmy)
                break
            else:
                pass

        else:
            break

    while True:
        dcid = secrets.token_hex(2)
        test = db.find_one({'docID': dcid})
        if test == None:
            break
        else:
            pass

    post = {
            "docID" : dcid,
            "docTitle" : title,
            "docDesc" : desc,
            "docDue": dateDue
        }

    db.insert_one(post)