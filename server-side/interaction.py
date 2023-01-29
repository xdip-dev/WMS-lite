import pandas as pd
import db.query_helper as h
from db.tableInfo import Tableinformation as t



def isExisting(toFound,whichTable,whichColumn):
    data = h.selectTableFilteredOnAColumn(table=whichTable,column=whichColumn,filter=toFound,only_one=True)
    output = {
        'exist':False,
        'data':None,
        'table':whichTable
        }
    if data== None : 
        return output
    else:
        output['exist']=True
        output['data']=data
        return output

def linkBoxToLocation(_barcode_box,barcode_location):

    isLocationExist = isExisting(toFound=barcode_location,
                            whichTable=t.t_location['name'],
                            whichColumn=t.t_location['barecodeLocation'])
    isBoxArticleExist = isExisting(toFound=_barcode_box,
                            whichTable=t.t_boxe_link_article['name'],
                            whichColumn=t.t_boxe_link_article['barecodeBoxe'])

    for check in [isBoxArticleExist,isLocationExist]:
        if not check['exist']:
            return f"missing data in the table {check['table']} "
    
    isBoxAlreadyRegistred = isExisting(toFound=_barcode_box,
                            whichTable=t.t_link_boxe_loc['name'],
                            whichColumn=t.t_link_boxe_loc['barecodeBoxe'])

    if not isBoxAlreadyRegistred['exist']:
        h.insertIntoTable(table=t.t_link_boxe_loc,values=[[_barcode_box,barcode_location,'actif']])
        return f'data insterted {_barcode_box} <=> {barcode_location}'
    else : 
        return f'boxe already link to : {isBoxAlreadyRegistred["data"][2]}'

def getLocationArticle(reference_article):
    df_art_loc=h.getTableData(table_name=t.v_article_loc['name'])
    df_art_loc=df_art_loc[df_art_loc[t.v_article_loc['reference']]==reference_article]
    df_art_loc['nbBoxes']=1
    df_art_loc=df_art_loc.groupby(by=list(df_art_loc.columns)[:-1],as_index=False).sum(numeric_only=True)
    return df_art_loc

def getQuantityStored(reference_article):
    frame = getLocationArticle(reference_article)
    numberOfBoxes = frame['nbBoxes'].sum()
    qtyPerBoxe = h.selectTableFilteredOnAColumn('box_article','ref_article',reference_article,only_one=True)[2]
    return f'{reference_article} has {str(numberOfBoxes*qtyPerBoxe)} unit in stock'

def removeBoxeFromLocation(_barcode_boxe):
    isBoxAlreadyRegistred = isExisting(toFound=_barcode_boxe,
                            whichTable=t.t_link_boxe_loc['name'],
                            whichColumn=t.t_link_boxe_loc['barecodeBoxe'])

    if isBoxAlreadyRegistred['exist']:
        return h.deletedROWID(table=t.t_link_boxe_loc['name'],column=t.t_link_boxe_loc['barecodeBoxe'],filter_deletion=_barcode_boxe)
    else:
        return f'{_barcode_boxe} not found to be removed from the stock'


def logActivitiesBoxes():
    pass



