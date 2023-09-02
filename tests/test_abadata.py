import csv
from dataclasses import make_dataclass

import pytest


# sanitize .csv field names
flds = [
    "Person_ID",
    "Name_Prefix",
    "Given_Name",
    "First_Name",
    "Nickname",
    "Middle_Name",
    "Last_Name",
    "Name_Suffix",
    "Birthdate",
    "Anniversary",
    "Gender",
    "Grade",
    "School",
    "Medical_Notes",
    "Child",
    "Marital_Status",
    "Status",
    "Membership",
    "Inactive_Reason",
    "Inactive_Date",
    "Services_User",
    "Calendar_User",
    "Check_Ins_User",
    "Registrations_User",
    "Giving_User",
    "Groups_User",
    "Publishing_User",
    "Home_Address_Street_Line_1",
    "Home_Address_Street_Line_2",
    "Home_Address_City",
    "Home_Address_State",
    "Home_Address_Zip_Code",
    "Work_Address_Street_Line_1",
    "Work_Address_Street_Line_2",
    "Work_Address_City",
    "Work_Address_State",
    "Work_Address_Zip_Code",
    "Other_Address_Street_Line_1",
    "Other_Address_Street_Line_2",
    "Other_Address_City",
    "Other_Address_State",
    "Other_Address_Zip_Code",
    "Mobile_Phone_Number",
    "Home_Phone_Number",
    "Work_Phone_Number",
    "Pager_Phone_Number",
    "Fax_Phone_Number",
    "Skype_Phone_Number",
    "Other_Phone_Number",
    "Home_Email",
    "Work_Email",
    "Other_Email",
    "Household_ID",
    "Household_Name",
    "Household_Primary_Contact",
    "Ministry_Affiliation",
    "Background_Check_Cleared",
    "Background_Check_Created_At",
    "Background_Check_Expires_On",
    "Background_Check_Note",
    "Created_At",
    "Updated_At",
]
Pers = make_dataclass("Pers", flds)


def gen_donor_aba_values(ws):
    """Skip the headers and return one aba value and related
    donor name from the input data worksheet.
    """
    for i, row in enumerate(ws.iter_rows()):
        if i > 0:
            aba, donor = row[0], row[1]
            yield aba.value, donor.value


def gen_pers_csv_entry(peopledata):
    with open(peopledata, "r") as data:
        dr = csv.DictReader(data, fieldnames=flds)
        for i, row in enumerate(dr):
            if i > 0:
                yield Pers(**row)


def test_read_xlsx(ws):
    for aba_val, donor_name in gen_donor_aba_values(ws):
        print(f"{aba_val=}\t{donor_name=}")


def test_read_csv(peopledata):
    for p in gen_pers_csv_entry(peopledata):
        print(f"{p.Person_ID=}\t{p.First_Name=}\t{p.Last_Name=}")


def test_build_lookups(ws, peopledata):
    """We want to get to two products:

    {"People":"ID" }
    {"ID"    :"ABA"}
    """
    located = 0
    i = 0
    people_to_id = {
        f"{p.First_Name} {p.Last_Name}": p.Person_ID
        for p in gen_pers_csv_entry(peopledata)
    }
    for aba_val, donor_name in gen_donor_aba_values(ws):
        i += 1
        if donor_name in people_to_id:
            print(f"found {aba_val=} for {donor_name=}")
            located += 1
    print(f"found {located} out of {i}")
