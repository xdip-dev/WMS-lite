import pandas as pd
import db.query_helper as d

def isExisting(toFound,whichTable,whichColumn):
    data = d.selectTableFilteredOnAColumn(whichTable,whichColumn,toFound,only_one=True)
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

def linkBoxToLocation(_barcode_box:str,barcode_location:str):

    isLocationExist = isExisting(toFound=barcode_location,whichTable='location',whichColumn='barcode_loc')
    isBoxArticleExist = isExisting(toFound=_barcode_box,whichTable='box_article',whichColumn='barcode_boxe')

    for check in [isBoxArticleExist,isLocationExist]:
        if not check['exist']:
            return f"missing data in the table {check['table']} "
    
    isBoxAlreadyRegistred = isExisting(toFound=_barcode_box,whichTable='box_location',whichColumn='barcode_boxe')

    if not isBoxAlreadyRegistred['exist']:
        d.insertIntoTable('box_location',(None,_barcode_box,barcode_location,'actif'))
        return f'data insterted {_barcode_box} <=> {barcode_location}'
    else : 
        return f'boxe already link to : {isBoxAlreadyRegistred["data"][2]}'


def getLocationArticle(reference_article):
    getlistBoxes =d.selectTableFilteredOnAColumn('box_article','ref_article',reference_article)
 
    listeToFilterTable = [elm[0] for elm in getlistBoxes]
    listeToTuple= tuple(listeToFilterTable) if len(listeToFilterTable)!=1 else f"('{listeToFilterTable[0]}')"
    query = f"""SELECT l.rack_name,l.row_shelf,l.colonne FROM box_location as bl
        left join location as l on l.barcode_loc=bl.barcode_loc
        WHERE bl.barcode_boxe IN {format(listeToTuple)}"""
    data=d.cursor.execute(query)
    df = pd.DataFrame(data.fetchall(),
        columns=['rack','shelf','col'])
    df['nbBoxes']=1
    df=df.groupby(by=['rack','shelf','col'],as_index=False).sum(numeric_only=True)

    return df

def getQuantityStored(reference_article):
    frame = getLocationArticle(reference_article)
    numberOfBoxes = frame['nbBoxes'].sum()
    qtyPerBoxe = d.selectTableFilteredOnAColumn('box_article','ref_article',reference_article,only_one=True)[2]
    return f'{reference_article} has {str(numberOfBoxes*qtyPerBoxe)} unit in stock'

def removeBoxeFromLocation(_barcode_boxe):
    table='box_location'
    col = 'barcode_boxe'
    isBoxAlreadyRegistred = isExisting(toFound=_barcode_boxe,whichTable=table,whichColumn=col)

    if isBoxAlreadyRegistred['exist']:
        d.deletedROWID(table=table,column=col,filter_deletion=_barcode_boxe)
        return f'{_barcode_boxe} is out of stock'

    else:
        return f'{_barcode_boxe} not found to be removed from the stock'


def logActivitiesBoxes():
    pass


