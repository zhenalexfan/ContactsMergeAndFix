
def command_line(ask, options, resolver):
    while True:
        key = input(ask)
        if key not in options:
            continue
        return resolver(key)