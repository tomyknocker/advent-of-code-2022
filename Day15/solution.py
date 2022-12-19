import parse
from time import perf_counter


def calc_manh_dist(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open('input', mode='r') as f:
    sensors = []
    while line := f.readline().strip():
        data = parse.parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)
        sensors.append({"sensor": data.fixed[0:2], "beacon": data.fixed[2:4]})



part1_y_row = 2_000_000
no_beacon_count = 0
x_min, x_max = 0, 0

# add manhattan distance value to each sensor (calculated from distance to the beacon)
# add distance in y axis (row) to the row for PART 1 calculations
# calculate x_min and x_max to have boundaries for PART 1 calculations
for item in sensors:
    m_dist = calc_manh_dist(item['sensor'], item['beacon'])
    item.update({"distance": m_dist})
    item.update({"distance_y": abs(item['sensor'][1] - part1_y_row)})
    x_min = min(x_min, item['sensor'][0] - m_dist)
    x_max = max(x_max, item['sensor'][0] + m_dist)

# optimizations
# - remove sensors that are too far (sensor range do not overlap with PART1 row)
# - sort sensors by farthest left sensor range
sensors_filtered = [sensor for sensor in sensors if (abs(part1_y_row - sensor['sensor'][1])) < sensor['distance']]
sensors_filtered.sort(key=lambda x: x['sensor'][0] - x['distance'])

t1 = perf_counter()

for x in range(x_min, x_max + 1):
    for item in sensors_filtered:
        if x == item['beacon'][0] and part1_y_row == item['beacon'][1]:
            # field is beacon
            break
        if abs(x - item['sensor'][0]) + item['distance_y'] <= item['distance']:
            no_beacon_count += 1
            break

t2 = perf_counter()

print(f"calc time:{t2 - t1}\nPART 1: {no_beacon_count=}")


# ============== PART 2 ================ #

no_beacon_count = 0
becons_x = []

# area for PART 2
part2x = 4_000_001
part2y0 = 0
part2y1 = 4_000_001

print("PART2")
t1 = perf_counter()
becon_found = -1, -1

for y in range(part2y0, part2y1):
    found = False
    x = 0
    # iter = 0
    # optimise sensor list for each row of the search area
    sensors_filtered = [sensor for sensor in sensors if (abs(y - sensor['sensor'][1])) < sensor['distance']]
    for sensor in sensors_filtered:
        sensor["distance_y"] = abs(sensor['sensor'][1] - y)

    # not needed - faster without sorting:
    # sensors_filtered.sort(key=lambda x: x['sensor'][0] - x['distance'])

    while x < part2x:
        found = False
        # iter += 1
        # only x part of manhattan distance is calculated and y part is added (because it is constant for a set row)
        while item := next((item for item in sensors_filtered
                            if abs(x - item['sensor'][0]) + item['distance_y'] <= item['distance']), None):
            found = True
            # for x found in sensor range, set x to far right point of sensor range +1
            x = item['sensor'][0] + item['distance'] - item['distance_y'] +1

        # if x not found in any sensor range - this is our result
        if not found:
            becon_found = x, y
            # print(f'{becon_found=}')
            x += 1
            break
    if not found:
        break
    if (y+1) % 400000 == 0:
        print('...10%', end='')
t2 = perf_counter()


print(f"\ncalc time:{t2 - t1}\nPART 2: {becon_found=} freq:{becon_found[0] * 4000000 + becon_found[1]}")

