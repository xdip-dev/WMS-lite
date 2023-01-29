class Tableinformation:
    ''' regroupe all the information of the table name and column 
    t_ for table and v_ for view'''
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

    t_test={
        "name":'test',
        'num':'num',
        'data':'data'
    }

    v_article_loc={
        'name':'article_loc ',
        "reference": "ref_article",
        "description": "des_article"
    }