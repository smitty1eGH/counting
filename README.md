# counting

Scripts for converting PlanningCenter batch .csv to .xlsx deposit

The goal is to support having this script available on a computer with common access in a way that does not leak PII.

Operation will be done by having data entries made on the PlanningCenter site, and then pulling down the batch files for processing.

Future refinements: 
A password-protected machine credential that could obtain the batch files and do the merge without saving anything locally.
Move the ABA data into an .xlsx for easier maintenance

## Setup

### python
https://www.python.org/downloads/

### git
https://git-scm.com/download/

### initialize

```bash
C:\\Users\\csmith\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -m venv counting
  or 
python -m venv counting

cd    counting
.\Scripts\activate.ps1
  or
. bin/activate
python -m pip install --upgrade pip

git     clone https://github.com/smitty1eGH/counting.git
python -m pip install -r requirements.txt

cd      counting
mkdir   instance
mkdir   tests
```

## configure

### instance/
There is an instance/ directory in the repo and .gitignore that could contain PII, and are thus inappropriate for storage in the git repo proper.

# CONOPS
## 0. Edit deposit_data.py to reflect
- counters
- cash received
## 1. Do regular and cash batches in PlanningCenter
## 2. Drop .csv exports regular and cash batches into instance/
## 3. Run this script to merge: 
###    3.1 cash: just summarize the amount and validate against the currency total
###    3.2 checks: do a real merge
###    3.3 (remove the cash/check .csv files)
###    3.3 deposit_data--bag_number, counters, ABA
###    3.4 Deposit_Ticket_Blank.xltx template


## notes

https://openpyxl.readthedocs.io

aba number | donor name