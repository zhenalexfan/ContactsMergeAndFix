import copy
from ..util.command_line_utils import *
from ..util.string_utils import *


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

    # Interactively run conflict resolver
    ask = (f"""Which value do you choose for field '{field_name}? [l/r]'
    [l] {left_value}
    [r] {right_value}
    """)

    def resolver(key):
        if key == 'l':
            return left_value
        if key == 'r':
            return right_value
        return None
    return command_line(ask, ['l', 'r'], resolver)
