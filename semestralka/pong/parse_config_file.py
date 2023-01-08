#path to resources directory
PATH = 'resources/'
#path to file with player statitics
STATS_FILE = 'player_stats.txt'
#path to file with skins
SKINS_FILE = 'skins/skins_info.txt'


def read_stats():
    """reads the file and returns player stats as [size, speed, stamina]"""

    with open(PATH + STATS_FILE, 'r') as file:
        stats = [int(line) for line in file.readlines()]

    #last number represents number of coins so we avoid it
    return stats[:-1]


def read_coins():
    """reads the file and return number of players coins"""
    with open(PATH + STATS_FILE, 'r') as file:
        lines = file.readlines()
    
    #is on the last line of the file
    return int(lines[-1])


def add_money(amount):
    stats = read_stats()
    coins = read_coins() + amount

    save_stats(stats, coins)



def save_stats(stats, coins):
    with open(PATH + STATS_FILE, 'w') as file:
        for stat in stats:
            file.write(str(stat) + '\n')
        file.write(str(coins) + '\n')


def save_skins(skins, curr_skin):
    with open(PATH + SKINS_FILE, 'w') as file:
        file.write(str(curr_skin) + '\n')
        for skin in skins:
            file.write(skin[0] + ' ' + str(skin[1]) + '\n')


def save(stats, coins, skins, curr_skin):
    save_stats(stats, coins)
    save_skins(skins, curr_skin)


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
