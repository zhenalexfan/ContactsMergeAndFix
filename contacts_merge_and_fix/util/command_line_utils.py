
def command_line(ask, options, resolver):
    while True:
        key = input(ask + '\n')
        if key not in options:
            continue
        return resolver(key)