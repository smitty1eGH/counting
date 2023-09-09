from openpyxl import load_workbook

from deposit_data import bag_number, cash, data

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