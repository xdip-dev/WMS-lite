from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy_utils import database_exists
# import sys
# sys.path.append("..")
from .. import helper


engine = create_engine(f"sqlite:///{helper.pathGeneratorMainToFile(['server-side','db','wms.db'])}",echo = True)
connection = engine.connect()


if __name__=="__main__":
    if database_exists(engine.url):

        meta = MetaData()

        location_table = Table(
        'location_table', meta, 
        Column('barcode_loc', String, primary_key = True), 
        Column('rack_name', String), 
        Column('row_shelf', Integer),
        Column('colonne',Integer)
        )

        box_article_table = Table(
        'box_article_table', meta, 
        Column('barcode_boxe', String, primary_key = True), 
        Column('ref_article', String), 
        Column('qty_min_box', Integer)
        )

        box_location_table = Table(
            'box_location_table', meta, 
        Column('barcode_boxe',String ), 
        Column('barcode_loc',String), 
        Column('status', String)
        )
        # without ForeignKey("box_article_table.barcode_boxe") to keep it simple, here the code if needed

        article = Table(
        "article",meta,
        Column('ref_article', String, primary_key = True ), 
        Column('des_article', String), 
        Column('status', String)
        )

        stock = Table(
            "stock",meta,
        Column('ref_article',String), 
        Column('qty', Integer), 
        Column('location', String)#note can be another table location link by id
        )


        meta.create_all(engine)
