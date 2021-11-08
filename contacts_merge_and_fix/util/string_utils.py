import string
import re

def to_str(contact: object, verbose=False):
    string = str()
    keys = contact.keys()
    for index, key in enumerate(keys):
        value = contact[key]
        if not verbose and not value.strip():
            continue
        string += "{0:<20} {1}".format(key + ': ', value)
        if index != len(keys) - 1:
            string += '\n'
    return string

# Print contacts as a block with a title
def to_str_block(title, contacts):
    string = "==={0:{fill}^40}===\n".format(title, fill='=')
    for index, c in enumerate(contacts):
        if index > 0:
            string += '\n'
            string += f"---{'-' * 40}---\n"
        string += to_str(c)
    string += f"==={'=' * 40}===\n"
    return string

def no_space(string):
    return string.replace(' ', '')


def contains_cjk(string):
    return len(re.findall(r'[\u4e00-\u9fff]+', string)) > 0


def is_cjk(string, ignore_space=True):
    t_string = no_space(string) if ignore_space else string
    kanji_parts = re.findall(r'[\u4e00-\u9fff]+', t_string)
    return ''.join(kanji_parts) == t_string


def reindent(s, num_spaces):
    s = string.split(s, '\n')
    s = [(num_spaces * ' ') + string.lstrip(line) for line in s]
    s = string.join(s, '\n')
    return s
