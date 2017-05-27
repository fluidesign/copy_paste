#! python

try:
    import os, sqlite3, logging, sys
    from _pickle import loads, dumps
except ModuleNotFoundError:
    print("We were not able to load the required module when running : " + __name__)
    exit()

DB_NAME = "akvifn"
TABLE_NAME = "clipboard_data"
COL_ID = "id"
COL_ID_TYPE = "INTEGER"
COL_DATA = "data"
COL_DATA_TYPE = "DATA"

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(DB_INSTANCE=0)
def create_new_db():
    try:
        conn = sqlite3.connect(":memory:") ## create a single connection to DB and use only it
        conn.isolation_level = None
        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS {tn} ({colid} {colidtype} PRIMARY KEY AUTOINCREMENT, {coldata} {coldatatype} )'
                  .format(tn=TABLE_NAME, colid=COL_ID, colidtype=COL_ID_TYPE, coldata=COL_DATA, coldatatype=COL_DATA_TYPE))
        conn.commit()
    except SyntaxError as err:
        print ("We have a syntax error: {err}".format(err=err))
        exit(1)
    except:
        e = sys.exc_info()
        print ("Unexpected error: {err}".format(err=e))
        exit(1)

    #debug purpose at this moment to verify that only a single instance of db is running, in the future, few instances ?!
    create_new_db.DB_INSTANCE += 1
    print ("Number of instance: {inst_num}".format(inst_num=create_new_db.DB_INSTANCE))
    return conn

    # Connection kept open till the class dies conn.close()

class DBManager:

    conn = create_new_db()

    def __init__(self):
        #Check if DB is alive
        cur = DBManager.conn.cursor()
        if cur.connection != DBManager.conn :
            print("Seems like the connection is down")
            print("Creating a new one...")
            create_new_db()

    _iterate = ('SELECT {id}, {data} FROM {tb}'.format(id=COL_ID,data=COL_DATA,tb=TABLE_NAME))
    _append = 'INSERT INTO {tb} ({data}) VALUES (?)'.format(tb=TABLE_NAME,data=COL_DATA)

    @staticmethod
    def get_all_clipboard_data(self,):
        print ("Print all clipboard data")
        for id, obj_buffer in DBManager.conn.execute(self._iterate):
            yield loads(str(obj_buffer))


    @staticmethod
    def add_clipboard_data_to_db(self, _data): #In our case the data is a simple text string
        print ("Saving received the following data : {data}".format(data=_data))
        try:
            obj_buffer = memoryview(dumps(_data, 2))
            DBManager.conn.execute(self._append, (obj_buffer,))
            DBManager.conn.commit()
        except sqlite3.IntegrityError as commit_error:
            print ("An error identified, we were not able to commit to DB due to:{err}".format(err=commit_error))



