import psycopg2
import os
from dotenv import load_dotenv, find_dotenv
import repackage

repackage.up()
import helper

load_dotenv(find_dotenv(helper.pathGeneratorMainToFile(["server-side", ".env"])))


class Tableinformation:
    t_article = {
        "name": "article",
        "reference": "ref_article",
        "description": "des_article",
        "status": "status",
    }

    t_boxe_link_article = {
        "name": "boxe_article",
        "barecodeBoxe": "barcode_boxe",
        "refArticle": "ref_article",
        "qtyMin": "qty_min_box",
    }

    t_location = {
        "name": "location",
        "barecodeLocation": "barcode_loc",
        "rack": "rack_name",
        "row": "row_shelf",
        "col": "col",
    }

    t_link_boxe_loc = {
        "name": "boxe_location",
        "barecodeBoxe": "barcode_boxe",
        "barecodeLocation": "barcode_loc",
        "status": "status",
    }


class SetupDB(Tableinformation):
    def __init__(self) -> None:
        super().__init__()
        self.password = os.getenv("password")
        self.connectionString = f"dbname=wms user=postgres password={self.password}"

    def creationAllTables(self) -> None:
        with psycopg2.connect(self.connectionString) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"""CREATE TABLE {self.t_article['name']} ( 
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
                    """
                )
            conn.commit()
