#!/usr/bin/python

import sys
from .contacts_io.google_csv_io import GoogleCsvReader
from .util.contact_utils import ContactUtils
from .solutions.merger import *


contact_reader = GoogleCsvReader('/Users/zhenalexfan/Downloads/contacts.csv')
contacts = contact_reader.read()

duplicates = {}
for i in range(0, len(contacts)):
    for j in range(i + 1, len(contacts)):
        left, right = (contacts[i], contacts[j])
        if is_duplicate(left, right):
            if i not in duplicates:
                duplicates[i] = []
            duplicates[i].append(j)

for leftIndex, rightIndices in duplicates.items():
    leftContact = contacts[leftIndex]
    rightContacts = [contacts[t] for t in rightIndices]
    title = ','.join([str(t) for t in [leftIndex, *rightIndices]])
    print("==={0:{fill}<20}===".format(title, fill='='))
    for c in [leftContact, *rightContacts]:
        print(ContactUtils.to_str(c))
    print(f"==={'=' * 20}===\n")
