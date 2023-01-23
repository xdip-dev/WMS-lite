import pytest
import repackage
repackage.up()
import db.query_helper as d

def test_variableParameter():
    output = d.variableParameter(5)
    should='(?,?,?,?,?)'
    assert output == should