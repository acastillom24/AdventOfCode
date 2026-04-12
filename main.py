from sources import read_input_txt as read_input


def transformer(line):
    s, e = line.split(" -> ")
    return (s, e)


connections = read_input(15, 7, transformer)
print(connections)
