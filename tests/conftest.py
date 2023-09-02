import os

from openpyxl import load_workbook
import pytest

@pytest.fixture
def abadata():
    return f'{os.getcwd()}\\instance\\ABA_Numbers_Donors_List.xlsx'
    

@pytest.fixture
def ws(abadata):
    wb = load_workbook(filename = abadata)
    return wb.active