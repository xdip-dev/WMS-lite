import pandas as pd 
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv, find_dotenv
import repackage
repackage.up()
import helper

load_dotenv(find_dotenv(helper.pathGeneratorMainToFile(["server-side", ".env"])))

def handleConnection(function,commit=True):
    '''Open and close the connection'''
    def wrap(*args, **kwargs):
        pwd=os.getenv("password")
        conn = create_engine(f"postgresql+psycopg2://postgres:{pwd}@localhost/wms")
        with conn.connect():        
                res = function(conn=conn,**kwargs)    
        return res
    return wrap

@handleConnection
def insertIntoTable(table,values,conn):
    ''' insert data in the table, the values needed with a nested list [[...]]'''
    col=list(table.values())[1:]
    df=pd.DataFrame(values,columns=col)
    df.to_sql(table['name'],conn,if_exists='append',index=False)

@handleConnection
def deletedROWID(table,column,filter_deletion,conn):
    query = f'''DELETE FROM {table} WHERE {column} = '{filter_deletion}';'''
    conn.execute(query)
    return f'{filter_deletion} removed from {table}'

@handleConnection
def selectTableFilteredOnAColumn(table,column,filter,conn,only_one=False):
    getData = conn.execute(f"Select * from {table} as t where t.{column}='{filter}'")

    if only_one:
        return getData.fetchone()
    else:
        return getData.fetchall()

@handleConnection
def getTableData(table_name,conn):
    df=pd.read_sql(f'SELECT * from {table_name}',conn)
    return df


# selectTableFilteredOnAColumn(table='boxe_article',column='ref_article',filter='J301')


# class SqlDataBase():
#     def __init__(self) -> None:

#         self.password= os.getenv("password")
#         self.conn=psycopg2.connect(f"dbname=wms user=postgres password={self.password}")
#         self.cursor=self.conn.cursor()

#     # to keep in case I need to wrappe fonction if the connections is a problem
#     def handleConnection(function):
#         '''Open and close the connection'''
#         def wrap(*args, **kwargs):
#             conn=sqlite3.connect(helper.pathGeneratorMainToFile(['server-side','db','wms.db']), check_same_thread=False)
#             cursor=conn.cursor()
#             execute = function(*args, cursor=cursor,conn=conn)
#             conn.close
#             return execute
#         return wrap


#     def variableParameter(self,size):
#         param_val="("
#         for x in range(size-1):
#             param_val+='?,'
#         param_val+='?)'
#         return param_val

#     # @handleConnection
#     def insertIntoTable(self,table,values):
#         param=self.variableParameter(len(values))
#         self.cursor.execute(f"insert into {table} values {param}",values)
#         self.conn.commit()


#     def selectTableFilteredOnAColumn(self,table,column,data,only_one=False):
#         getData = self.cursor.execute(f"Select * from {table} as t where t.{column}=?",(data,))

#         if only_one:
#             return getData.fetchone()
#         else:
#             return getData.fetchall()

#     def deletedROWID(self,table,column,filter_deletion):

#         query = f'''DELETE FROM {table} WHERE ROWID IN
#                         ( SELECT t.ROWID FROM {table} as t WHERE t.{column} = '{filter_deletion}' );
#                 '''
#         self.cursor.execute(query)
#         self.conn.commit()
#         return True
    
#     def closeConnection(self):
#         self.conn.close()




