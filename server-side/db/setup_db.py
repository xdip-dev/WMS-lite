from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import repackage
repackage.up()
import helper


engine = create_engine(f"sqlite:///{helper.pathGeneratorMainToFile(['server-side','db','wms.db'])}")
connection = engine.connect()
session = Session(engine)
Base = declarative_base()

class Location(Base):
    __tablename__="location"

    barcode_loc=Column(String, primary_key = True)
    rack_name=Column(String)
    row_shelf=Column(Integer)
    colonne=Column(Integer)
 
class BoxArticle(Base):
    __tablename__="box_article"

    
    barcode_boxe=Column(String, primary_key = True)
    ref_article=Column(String)
    qty_min_box=Column(Integer)

class LinkBoxLocation(Base):
    __tablename__="box_location"

    id=Column(Integer, primary_key = True) 
    barcode_boxe=Column(String)
    barcode_loc=Column(String)
    status=Column(String)

class Article(Base):
    __tablename__="article"

    id=Column(Integer, primary_key = True) 
    ref_article=Column(String ) 
    des_article=Column(String) 
    status=Column(String)

class Stock(Base):
    __tablename__="stock"

    id=Column(Integer, primary_key = True) 
    ref_article=Column(String ) 
    qty=Column(String) 
    physique_loc=Column(String)


if __name__=="__main__":
    Base.metadata.create_all(engine)

