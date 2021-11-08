import csv
from .common_io import ContactsReader, ContactsWriter


class GoogleCsvReader(ContactsReader):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.field_names = None

    def read_field_names(self): 
        if self.field_names == None:
            self.read()
        return self.field_names

    def read(self):
        rows = []
        with open(self.filepath) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rows.append(row)
        self.field_names = rows[0]
        contacts = [GoogleCsvReader.__transform_to_contact(
            row, self.field_names) for row in rows[1:]]
        return contacts

    @staticmethod
    def __transform_to_contact(record, field_names):
        contact = {}
        for index, field_name in enumerate(field_names):
            contact[field_name] = record[index]
        return contact


class GoogleCsvWriter(ContactsWriter):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def write(self, field_names, contacts):
        with open(self.filepath, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for contact in contacts:
                csv_record = GoogleCsvWriter.__transform_to_csv_record(
                    contact, field_names)
                writer.writerow(csv_record)

    @staticmethod
    def __transform_to_csv_record(contact, field_names):
        return [contact(key) for key in field_names]
