import pytest

def gen_donor_aba_values(ws):
    '''Skip the headers and return one aba value and related
    donor name from the input data worksheet.
    '''
    for i,row in enumerate(ws.iter_rows()):
        if i>0:
            aba, donor = row[0], row[1]
            yield aba.value, donor.value

def test_read_xlsx(ws):
    for aba_val, donor_name in gen_donor_aba_values(ws):
        print(f'{aba_val=}\t{donor_name=}')
