import json

with open('muggle_repellent.json') as input_file:
    output = []
    loader = json.load(input_file)
    for i in loader:
        creature = i['creature']
        size = i['size']
        danger = i['danger']
        magic = i['magic']
        additional = 100 - size * magic // danger
        if additional < 0:
            additional = 0
        output.append([creature, size, danger, magic, additional])
    output.sort(key=lambda x: (-x[4], x[0]))

with open('muggle_magic.csv', 'w') as output_file:
    output_file.write('name,size,danger,magic,additional\n')
    print('', file=output_file)
    for i in output:
        print(*i, sep=',', file=output_file)