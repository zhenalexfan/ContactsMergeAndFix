#!/usr/bin/python

import argparse

from contacts_merge_and_fix.solutions.deduplicate_solution import DeduplicateSolution
from .contacts_io.google_csv_io import GoogleCsvReader, GoogleCsvWriter
from .solutions.deduplicate_solution import *
from .solutions.phonetic_names_solution import *

parser = argparse.ArgumentParser()
parser.add_argument('-input', type=str, help='path of input contacts file')
parser.add_argument('-output', type=str, help='path of output contacts file')
args = parser.parse_args()

contact_reader = GoogleCsvReader(args.input)
contacts = contact_reader.read()
new_contacts = contacts
solutions = [DeduplicateSolution(), PhoneticNamesSolution()]
for solution in solutions:
    new_contacts = solution.resolve(new_contacts)
contact_writer = GoogleCsvWriter(args.output)
contact_writer.write(contact_reader.read_field_names(), new_contacts)
