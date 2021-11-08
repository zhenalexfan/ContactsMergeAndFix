import string
import re


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
