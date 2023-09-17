from openpyxl import load_workbook

from deposit_data import bag_number, cash, aba_data, people

# CONOPS
# 0. Edit deposit_data.py to reflect
#    - counters
#    - cash received
# 1. Do regular and cash batches in PlanningCenter
# 2. Drop .csv exports regular and cash batches into instance/
# 3. Run this script to merge: 
#    - regular and cash batch data
#    - deposit_data
#    - Deposit_Ticket_Blank.xltx
#    into a deposit slip .xlsx for review 

cash_total=sum([k*v for k,v in cash.items()])
counters=', '.join([q[0] for q in [p for p in filter(lambda x:x[1]==True,people)]])

def main():

if __name__=='__main__':
    main()