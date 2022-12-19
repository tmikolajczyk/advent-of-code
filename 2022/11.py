
import math
from itertools import combinations
from tqdm import tqdm
from aocd import get_data, submit


day = 11
year = 2022
raw_data = get_data(day=day, year=year)

def parse_monkey_data(raw_data):
    data = {}
    monkeys = raw_data.split("\n\n")
    for monkey in monkeys:
        lines = monkey.split('\n')
        for line in lines:
            line = line.strip()
            if 'Monkey' in line:
                monkey = line.replace(':', "")
                data[monkey] = {}
                continue
            if 'Starting items' in line:
                data[monkey]['items'] = line.split(': ')[-1].split(', ')
                continue
            if 'Operation' in line:
                data[monkey]['operation'] = line.split('= ')[-1]
                continue
            if 'Test' in line:
                data[monkey]['test'] = int(line.split('by ')[-1])
                continue
            if 'If true' in line:
                data[monkey]['if_true'] = int(line.split(' ')[-1])
                continue
            if 'If false' in line:
                data[monkey]['if_false'] = int(line.split(' ')[-1])
                continue
        data[monkey]['output'] = []
        data[monkey]['result'] = 0
    return data


def monkey_runs(data, rounds):
    if rounds > 20:
        lcm = math.lcm(*[a.get('test') for a in data.values()])
    for _ in tqdm(range(rounds)):
        for k in data:
            if len(data.get(k).get('output')) > 0:
                data.get(k).get('items').extend(data.get(k).get('output'))
            for org_value in data.get(k).get('items'):
                old = int(org_value)
                operation = data.get(k).get('operation')
                new = eval(operation)
                if rounds == 20:
                    new //= 3
                else:
                    new %= lcm
                if new % data.get(k).get('test') == 0:
                    id = data.get(k).get('if_true')
                    data[f'Monkey {id}'].get('output').append(new)
                else:
                    id = data.get(k).get('if_false')
                    data[f'Monkey {id}'].get('output').append(new)
                
                for el in data.get(k).get('output'):
                    if el in data.get(k).get('items'):
                        data.get(k).get('output').remove(el)

        for k in data:
            data.get(k)['result'] += len(data.get(k)['items'])
            data.get(k)['items'] = data.get(k).get('output')
            data.get(k)['output'] = []

    results = [data[k]['result'] for k in data]
    return max([x[0]*x[1] for x in combinations(results, 2)])


# part1
data = parse_monkey_data(raw_data)
result1 = monkey_runs(data, 20)
submit(result1)

# part2
data = parse_monkey_data(raw_data)
result2 = monkey_runs(data, 10000)
submit(result2)
