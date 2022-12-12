import igraph as ig


def parse_map(mapa):
    graf_input = {}
    new_map = []
    y_max = len(mapa) - 1
    for y, map_line in enumerate(mapa):
        new_map.append([])
        x_max = len(map_line) - 1
        for x, char in enumerate(map_line):
            edges = []
            if y > 0:
                if (mapa[y - 1][x] - char) <= 1:
                    edges.append(f'{chr(mapa[y - 1][x])}{x}_{y - 1}')
            if y < y_max:
                if (mapa[y + 1][x] - char) <= 1:
                    edges.append(f'{chr(mapa[y + 1][x])}{x}_{y + 1}')
            if x > 0:
                if (map_line[x - 1] - char) <= 1:
                    edges.append(f'{chr(map_line[x - 1])}{x - 1}_{y}')
            if x < x_max:
                if (map_line[x + 1] - char) <= 1:
                    edges.append(f'{chr(map_line[x + 1])}{x + 1}_{y}')
            vertice = f'{chr(char)}{x}_{y}'
            # print(f"{vertice=} {edges=}")
            graf_input.update({vertice: edges})
    return graf_input


start_pos = ''
target_pos = ''
my_map = []
with open('input', mode='rb') as f:
    for y, line in enumerate(f.readlines()):
        line = line.strip()
        if (idx := line.find(b'S')) >= 0:
            start_pos = f'a{idx}_{y}'
            line = line.replace(b'S', b'a')
        if (idx := line.find(b'E')) >= 0:
            target_pos = f'z{idx}_{y}'
            line = line.replace(b'E', b'z')
        my_map.append(line)

new_map = parse_map(my_map)

g: ig.Graph = ig.Graph.ListDict(new_map, directed=True)

result = g.get_shortest_paths(start_pos, target_pos, mode='out', output='vpath')
# for x in result[0]:
#     print(g.vs[x]['name'], end=' -> ')
print('PART1:')
print(len(result[0]) - 1)

part2_start_positions = []
for x in g.vs:
    if x['name'].startswith('a'):
        part2_start_positions.append(x['name'])

part2_paths = []
for start_pos2 in part2_start_positions:
    # print(start_pos2, end=' -->')
    result = g.get_shortest_paths(start_pos2, target_pos, mode='out', output='vpath')
    try:
        # print(len(result[0]))
        if len(result[0]) > 0:
            part2_paths.append(len(result[0]) - 1)
    except:
        print("NOPE")

print('PART2:')
print(sorted(part2_paths)[0])
