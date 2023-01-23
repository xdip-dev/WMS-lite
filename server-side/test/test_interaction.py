import pytest
import repackage
repackage.up()
import interaction as i


def test_valide_isExisting():
    data = i.isExisting(toFound='XX001',whichTable='location',whichColumn='barcode_loc')

    assert data['exist'] == True
    assert data['data'] != None
    assert data['table'] == 'location'

def test_invalide_isExisting():
    data = i.isExisting(toFound='',whichTable='location',whichColumn='barcode_loc')

    assert data['exist'] == False
    assert data['data'] == None
    assert data['table'] == 'location'


