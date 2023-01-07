PATH = 'resources/'
STATS_FILE = 'player_stats.txt'
SKINS_FILE = 'skins/skins_info.txt'


def read_stats():
    with open(PATH + STATS_FILE, 'r') as file:
        stats = [int(line) for line in file.readlines()]
    return stats[:-1]


def read_coins():
    with open(PATH + STATS_FILE, 'r') as file:
        lines = file.readlines()
    return int(lines[-1])


def save(stats, coins):
    with open(PATH + STATS_FILE, 'w') as file:
        for stat in stats:
            file.write(str(stat) + '\n')
        file.write(str(coins) + '\n')


def add_money(amount):
    stats = read_stats()
    coins = read_coins() + amount

    save(stats, coins)


def read_skins():
    with open(PATH + SKINS_FILE, 'r') as file:
        curr_skin = int(file.readline())

        skins = []

        for line in file:
            # Split the line into two parts: the string and the bool
            
            string, boolean = line.strip().split()
            
            # Convert the boolean string to a bool
            boolean = boolean == 'True'
            skins.append((string, boolean))
    
    return (curr_skin, skins)
