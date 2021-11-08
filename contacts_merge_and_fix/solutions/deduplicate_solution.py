import copy
from .solution import Solution
from ..util.command_line_utils import *
from ..util.string_utils import *


class DeduplicateSolution(Solution):
    def resolve(self, contacts):
        duplicates = {}
        for i in range(0, len(contacts)):
            for j in range(i + 1, len(contacts)):
                left, right = (contacts[i], contacts[j])
                if is_duplicate(left, right):
                    if i not in duplicates:
                        duplicates[i] = []
                    duplicates[i].append(j)

        duplicate_index_set = set()
        for left_index, right_indices in duplicates.items():
            duplicate_index_set = duplicate_index_set.union(
                set([left_index, *right_indices]))
        new_contacts = []

        for left_index, right_indices in duplicates.items():
            left_contact = contacts[left_index]
            right_contacts = [contacts[t] for t in right_indices]
            new_contact = left_contact
            for right_contact in right_contacts:
                new_contact = merge_contacts(new_contact, right_contact)
            new_contacts.append(new_contact)

        for i, original_contact in enumerate(contacts):
            if i not in duplicate_index_set:
                new_contacts.append(original_contact)

        return new_contacts


def is_duplicate(left: object, right: object) -> bool:
    # Assuming the object is in Google CSV format
    left_name = left['Name']
    right_name = right['Name']
    if left_name == right_name:
        return True
    if is_cjk(left_name) and is_cjk(right_name):
        return no_space(left_name) == no_space(right_name)
    return False


def merge_contacts(left: object, right: object) -> object:
    print(to_str_block('Merging contacts', [left, right]))
    merged_contact = copy.copy(left)
    for key, right_value in right.items():
        left_value = merged_contact[key]
        merged_value = __merged_value(key, left_value, right_value)
        merged_contact[key] = merged_value
    return merged_contact


def __merged_value(field_name, left_value, right_value):
    if not left_value.strip():
        return right_value
    if not right_value.strip():
        return left_value
    if left_value == right_value:
        return left_value

    # Interactively run conflict resolver
    ask = (f"""Which value will you use for field '{field_name}'? [l/r]
    [l] {left_value}
    [r] {right_value}""")

    def resolver(key):
        if key == 'l':
            return left_value
        if key == 'r':
            return right_value
        return None
    return command_line(ask, ['l', 'r'], resolver)
