#! python
# config manager module use to :
# 1. Save clipboard
# 2. Load value from memory [Previously saved clipboard]
#TODO add global logger
try:
    import pyperclip, db_manager, logging, logger
except ModuleNotFoundError:
    print("We were not able to load the required module when running : " + __name__)
    exit()

def retreive_values_from_db():
    print("Collecting data stored in the DB")
    DBManager = db_manager.DBManager()
    db_values = db_manager.DBManager.get_all_clipboard_data(DBManager)
    for id in range(10):    #TODO limit range by reading actual limiter from the user's config file
        print('Value ID: {id}'.format(id=id))
        next(db_values)


def catch_clipboard():

    try:
        DBManager = db_manager.DBManager()
    except:
        print("We were not able to establish a connection to the db")
    clipboard_catch = pyperclip.paste()
    print("We captured the following value from the clipboard " + clipboard_catch)
    print("Saving value to DB")
    DBManager = db_manager.DBManager()
    db_manager.DBManager.add_clipboard_data_to_db(DBManager,clipboard_catch)

