PATH = 'resources/'
FILE = 'player_stats.txt'


def read_stats():
    with open(PATH + FILE, 'r') as file:
        stats = [int(line) for line in file.readlines()]
    return stats[:-1]


def read_coins():
    with open(PATH + FILE, 'r') as file:
        lines = file.readlines()
    return int(lines[-1])


def save(stats, coins):
    with open(PATH + FILE, 'w') as file:
        for stat in stats:
            file.write(str(stat) + '\n')
        file.write(str(coins) + '\n')