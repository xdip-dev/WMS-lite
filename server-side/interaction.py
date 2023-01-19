from db.setup_db import connection
import pandas as pd


# df=pd.read_sql("select * from location_table",connection)

# print(df)

def addingToStock(barcode_box,barcode_loc):
    dataLocBarcode=pd.read_sql(
        f"select barcode_loc from location_table",
        connection
    )
    dataArticleBarcode=pd.read_sql(
    f"select barcode_boxe from box_article_table",
    connection
    )




