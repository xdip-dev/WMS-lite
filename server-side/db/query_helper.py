import sqlite3
import repackage
repackage.up()
import helper


conn=sqlite3.connect(helper.pathGeneratorMainToFile(['server-side','db','wms.db']), check_same_thread=False)
cursor=conn.cursor()

#to keep in case I need to wrappe fonction if the connections is a problem
# def handleConnection(function):
#     '''Open and close the connection'''
#     def wrap(*args, **kwargs):
#         conn=sqlite3.connect(helper.pathGeneratorMainToFile(['server-side','db','wms.db']), check_same_thread=False)
#         cursor=conn.cursor()
#         execute = function(*args, cursor=cursor,conn=conn)
#         conn.close
#         return execute
#     return wrap


def variableParameter(size):
    param_val="("
    for x in range(size-1):
        param_val+='?,'
    param_val+='?)'
    return param_val

# @handleConnection
def insertIntoTable(tablename,values):
    param=variableParameter(len(values))
    cursor.execute(f"insert into {tablename} values {param}",values)
    conn.commit()


def selectTableFilteredOnAColumn(table,column,data,only_one=False):
    getData = cursor.execute(f"Select * from {table} as t where t.{column}=?",(data,))

    if only_one:
        return getData.fetchone()
    else:
        return getData.fetchall()

def deletedROWID(table,column,filter_deletion):

    query = f'''DELETE FROM {table} WHERE ROWID IN
                    ( SELECT t.ROWID FROM {table} as t WHERE t.{column} = '{filter_deletion}' );
            '''
    cursor.execute(query)
    conn.commit()
    return True



