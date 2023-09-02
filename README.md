# counting

Scripts for converting PlanningCenter batch .csv to .xlsx deposit

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

## running

### pytest

configtest.py declares fixtures for use in all test_*.py files

> python -m pytest -s tests/ 


## notes

https://openpyxl.readthedocs.io

aba number | donor name