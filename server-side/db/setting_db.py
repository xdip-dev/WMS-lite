import psycopg2
import os
from dotenv import load_dotenv, find_dotenv
from tableInfo import Tableinformation
import repackage

repackage.up()
import helper

load_dotenv(find_dotenv(helper.pathGeneratorMainToFile(["server-side", ".env"])))



class SetupDB(Tableinformation):
    def __init__(self) -> None:
        super().__init__()
        self.password = os.getenv("password")
        self.connectionString = f"dbname=wms user=postgres password={self.password}"

    def creationAllTables(self) -> None:
        with psycopg2.connect(self.connectionString) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"""
                    CREATE TABLE {self.t_article['name']} ( 
                            {self.t_article['reference']} TEXT NOT NULL, 
                            {self.t_article['description']} TEXT, 
                            {self.t_article['status']} TEXT, 
                            PRIMARY KEY ({self.t_article['reference']})
                        );
                        CREATE TABLE {self.t_boxe_link_article['name']} (
                            {self.t_boxe_link_article['barecodeBoxe']} TEXT NOT NULL, 
                            {self.t_boxe_link_article['refArticle']} TEXT, 
                            {self.t_boxe_link_article['qtyMin']} INTEGER, 
                            PRIMARY KEY ({self.t_boxe_link_article['barecodeBoxe']})
                        );
                        CREATE TABLE {self.t_location['name']} (
                            {self.t_location['barecodeLocation']} TEXT NOT NULL, 
                            {self.t_location['rack']} TEXT, 
                            {self.t_location['row']} INTEGER, 
                            {self.t_location['col']} INTEGER, 
                            PRIMARY KEY ({self.t_location['barecodeLocation']})                        
                        );
                        CREATE TABLE {self.t_link_boxe_loc['name']} (
                            id SERIAL NOT NULL,
                            {self.t_link_boxe_loc['barecodeBoxe']} TEXT,
                            {self.t_link_boxe_loc['barecodeLocation']} TEXT,
                            {self.t_link_boxe_loc['status']}	TEXT,
                            PRIMARY KEY(id)
                        );
                        CREATE or REPLACE view article_loc as
                            SELECT 
                                a.{self.t_article['reference']},
                                a.{self.t_article['description']},
                                l.{self.t_location['rack']} ,
                                l.{self.t_location['row']} ,
                                l.{self.t_location['col']}
                            FROM {self.t_article['name']} as a
                            LEFT JOIN {self.t_boxe_link_article['name']} as b on
                                 b.{self.t_boxe_link_article['refArticle']}=a.{self.t_article['reference']}
                            LEFT JOIN {self.t_link_boxe_loc['name']} as bl on
                                 bl.{self.t_link_boxe_loc['barecodeBoxe']} =b.{self.t_boxe_link_article['barecodeBoxe']} 
                            LEFT JOIN {self.t_location['name']} as l on
                                 l.{self.t_location['barecodeLocation']} =bl.{self.t_link_boxe_loc['barecodeLocation']} 
                            WHERE l.{self.t_location['rack']} <>'';
                    """
                )
            conn.commit()


if __name__=='__main__':
    setup=SetupDB()
    setup.creationAllTables()
