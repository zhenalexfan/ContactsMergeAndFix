import pinyin
import copy

from .solution import Solution
from ..util.string_utils import *

class PhoneticNamesSolution(Solution):
    def resolve(self, contacts):
        new_contacts = []
        for contact in contacts:
            if has_phonetic_names(contact):
                new_contacts.append(contact)
                continue
            new_contact = add_phonectic_names(contact)
            new_contacts.append(new_contact)
        return new_contacts


def has_phonetic_names(contact):
    if contact['Given Name Yomi'] and contact['Family Name Yomi']:
        return True
    return False


def add_phonectic_names(contact):
    # Assuming the object is in Google CSV format
    given_name = contact['Given Name']
    family_name = contact['Family Name']
    if has_phonetic_names(contact):
        return contact
    if not is_cjk(given_name) or not is_cjk(family_name):
        return contact
    new_contact = copy.copy(contact)
    new_contact['Given Name Yomi'] = __convert_phonetic_name(given_name)
    new_contact['Family Name Yomi'] = __convert_phonetic_name(family_name)
    return new_contact


def __convert_phonetic_name(name):
    if not is_cjk(name):
        return
    lowercased = pinyin.get(name, format='strip', delimiter='')
    return lowercased.title()
