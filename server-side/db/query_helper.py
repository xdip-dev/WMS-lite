import sqlite3
import repackage
repackage.up()
import helper

conn=sqlite3.connect(helper.pathGeneratorMainToFile(['server-side','db','wms.db']))
cursor=conn.cursor()

def variableParameter(size):
    param_val="("
    for x in range(size-1):
        param_val+='?,'
    param_val+='?)'
    return param_val

def insertIntoTable(tablename,values):
    param=variableParameter(len(values))
    cursor.execute(f"insert into {tablename} values {param}",values)
    conn.commit()
    conn.close()

def selectTableFilteredOnAColumn(table,column,data,only_one=False):
    getData = cursor.execute(f"Select * from {table} as t where t.{column}=?",(data,))

    if only_one:
        return getData.fetchone()
    else:
        return getData.fetchall()



