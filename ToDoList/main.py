print('Program Booting..')
import pymongo
import dotenv, os
import function.portal as tp
FirstBoot = True

os.system('cls')
print("Welcome! We're getting things ready for you..")

dotenv.load_dotenv()
mongoConnect = os.getenv('MONGOSTRING')
def ConnectDB():
    try:
        #print('<?> Connecting to MongoDB')
        cluster = pymongo.MongoClient(mongoConnect)
        dbTable = cluster['Python']
        db = dbTable['ToDo']
        #print('<i> Connection established')
        return db
    except:
        #print('<!> Error while connecting to MongoDB')
        return False

iteration = 0
while True:
    db = ConnectDB()
    if iteration == 3:
        exit('<_!_> Connection to MongoDB failed after 3 attemps')
    if db == False:
        iteration += 1
        #print('<?> Retrying to connect to MongoDB')
        pass
    else:
        break
os.system('cls')

def Selector():
    global FirstBoot
    if FirstBoot:
        FirstBoot = False
        tp.Portal('v', db)
    else:
        choice = input('')
        tp.Portal(choice, db)

while True:
    Selector()