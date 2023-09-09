import pytest

bag_number='Fill_in'

         #  name          present
counters=[('James Bowing',True)
         ,('Chris Rizzo' ,True)
         ,('Chris Smith' ,False)]

cash={  1:0
     ,  5:0
     , 10:0
     , 20:0
     , 50:0
     ,100:0}

def prep_counters():
    pres=filter(lambda x:x[1]==True,counters)
    return ', '.join([x[0] for x in pres])

def prep_data(ABA_Numbers):
    out=[]
    for i, row in enumerate(ABA_Numbers.iter_rows()):
        if i > 0:
            out.append(f'"{row[1].value}":"{row[0].value}"')
    return 'data={%s}' % ','.join(out)

@pytest.mark.skip
def test_counters():
    assert prep_counters()!='James Bowing, Chris Rizzo, Chris Smith'


def test_prepare_data(ABA_Numbers):
    with open('deposit_data.py','w') as dd:
        dd.write(f'{bag_number=}\n')
        dd.write(f'{cash=}\n')
        dd.write(prep_data(ABA_Numbers))
