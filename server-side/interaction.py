import pandas as pd
from db.query_helper import cursor,insertIntoTable,selectTableFilteredOnAColumn


def linkBoxToLocation(_barcode_box:str,barcode_location:str):
    isLocationExist=selectTableFilteredOnAColumn('location','barcode_loc',barcode_location,only_one=True)
    isBoxArticleExist =selectTableFilteredOnAColumn('box_article','barcode_boxe',_barcode_box,only_one=True)
 
    for check in [isBoxArticleExist,isLocationExist]:
        if check == None:
            return "missing data "
    
    insertIntoTable('box_location',(None,_barcode_box,barcode_location,'actif'))
    return 'data insterted'


def getLocationArticle(reference_article):
    getlistBoxes =selectTableFilteredOnAColumn('box_article','ref_article',reference_article)
 
    listeToFilterTable = [elm[0] for elm in getlistBoxes]
    listeToTuple= tuple(listeToFilterTable) if len(listeToFilterTable)!=1 else f"('{listeToFilterTable[0]}')"
    query = f"""SELECT l.rack_name,l.row_shelf,l.colonne FROM box_location as bl
        left join location as l on l.barcode_loc=bl.barcode_loc
        WHERE bl.barcode_boxe IN {format(listeToTuple)}"""
    data=cursor.execute(query)
    df = pd.DataFrame(data.fetchall(),
        columns=['rack','shelf','col'])

    return df

def getQuantityStored(reference_article):
    frame = getLocationArticle(reference_article)
    numberOfBoxes = len(frame.index)
    qtyPerBoxe = selectTableFilteredOnAColumn('box_article','ref_article',reference_article,only_one=True)[2]
    return numberOfBoxes*qtyPerBoxe




