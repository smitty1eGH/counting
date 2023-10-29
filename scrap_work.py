import csv
from dataclasses import dataclass,field
from datetime import datetime
from pathlib import Path

# Goal:
#  Refresh the mapping from pers_id to ABA value in the data
#
# Steps:
#  1. Load all of the DepositEntry data
#  2. Load all of the batch entry data as a dictionary of {date|check_number|amount:donor_id} from the BatchEntry data
# => donor_id	donor_first_name	donor_last_name	donor_name_suffix	donor_email	check_number	amount
#  3. Do a loop in the batch entries to query the DepositEntry data, and generate a usable dictionary for processing.
#  4. The only extra maintenance should be when adding a new ABA number.

START_HERE='C:/users/csmith/proj/counting/counting/'

@dataclass
class DepositEntry():
  date: field(default_factory=datetime)
  ABA_number: str
  check_number: float
  amount: float


def gen_directories():
  '''Get a list of directories to inspect for data
  that match ./instance/deposit_XXXXYYZZ  
  '''
  p = Path(f'{START_HERE}instance/')
  for x in p.iterdir():
    if x.is_dir() and x.name.startswith('deposit'):
      yield x


def load_data():
  '''Load up the deposit entries and the batch entries
  1. get directory iterator
  2. load deposit entries
  3. load batch entries
  '''
  deposit_entry_data=[]
  batch_entry_data={}
  
  # 0.
  for x in gen_directories():
    print(f'working on {x}')
    y=x.name.split('_')
    d=datetime(int(y[1][:4]), int(y[1][4:6]), int(y[1][6:]))
    
    # 1.
    with open(f'{x}/data_{y[1]}.txt','r') as f:
      dr = csv.reader(f, delimiter=' ')
      for i,r in enumerate(dr):
        if i>0:
          deposit_entry_data.append(DepositEntry(d,r[0],r[1],r[2]))
          
    # 2.
    with open(f'{x}/batch-checks.csv','r') as f:
      dr = csv.reader(f)
      for i,r in enumerate(dr):
        if i>0:
          #{date|check_number|amount:donor_id} elide the dollar sign
          batch_entry_data[f'{d}|{r[5]}|{r[6][1:].strip()}']=r[0]
    
  return deposit_entry_data, batch_entry_data


entries, donors=load_data()
output=set()
for x in entries:
  key=f'{x.date}|{x.check_number}|{x.amount}'
  if key in donors:
    output.add(f'"{donors[key]}":"{x.ABA_number}"')
  else:
    print(f'missed {key=}')

print('aba_data={%s}' % ','.join(output))