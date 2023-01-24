import sqlite3
import repackage
repackage.up()
import helper

class SqlDataBase():
    def __init__(self) -> None:
        
        self.conn=sqlite3.connect(helper.pathGeneratorMainToFile(['server-side','db','wms.db']), check_same_thread=False)
        self.cursor=self.conn.cursor()

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


    def variableParameter(self,size):
        param_val="("
        for x in range(size-1):
            param_val+='?,'
        param_val+='?)'
        return param_val

    # @handleConnection
    def insertIntoTable(self,tablename,values):
        param=self.variableParameter(len(values))
        self.cursor.execute(f"insert into {tablename} values {param}",values)
        self.conn.commit()


    def selectTableFilteredOnAColumn(self,table,column,data,only_one=False):
        getData = self.cursor.execute(f"Select * from {table} as t where t.{column}=?",(data,))

        if only_one:
            return getData.fetchone()
        else:
            return getData.fetchall()

    def deletedROWID(self,table,column,filter_deletion):

        query = f'''DELETE FROM {table} WHERE ROWID IN
                        ( SELECT t.ROWID FROM {table} as t WHERE t.{column} = '{filter_deletion}' );
                '''
        self.cursor.execute(query)
        self.conn.commit()
        return True
    
    def closeConnection(self):
        self.conn.close()




