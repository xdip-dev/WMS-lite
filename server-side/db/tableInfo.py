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