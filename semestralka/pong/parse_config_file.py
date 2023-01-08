"""parses config files"""

# path to resources directory
PATH = 'resources/'
# path to file with player statitics
STATS_FILE = 'player_stats.txt'
# path to file with skins
SKINS_FILE = 'skins/skins_info.txt'


def read_stats():
    """reads the file and returns player stats as [size, speed, stamina]"""

    with open(PATH + STATS_FILE, 'r', encoding="utf8") as file:
        stats = [int(line) for line in file.readlines()]

    # last number represents number of coins so we avoid it
    return stats[:-1]


def read_coins():
    """reads the file and return number of players coins"""

    with open(PATH + STATS_FILE, 'r', encoding="utf8") as file:
        lines = file.readlines()

    # is on the last line of the file
    return int(lines[-1])


def add_money(amount):
    """adds money to player after winning"""

    # read stats for easier manipulation
    stats = read_stats()
    # adds won money
    coins = read_coins() + amount

    # saves stats
    save_stats(stats, coins)


def save_stats(stats, coins):
    """writes stats into the player stats file"""

    with open(PATH + STATS_FILE, 'w', encoding="utf8") as file:
        # stats are [size, speed, stamina]
        for stat in stats:
            file.write(str(stat) + '\n')
        file.write(str(coins) + '\n')


def save_skins(skins, curr_skin):
    """writes skins into the skins stats file"""

    with open(PATH + SKINS_FILE, 'w', encoding="utf8") as file:
        # writes the curr_skin on the first line
        file.write(str(curr_skin) + '\n')
        for skin in skins:
            # skin[0] is name of the skin and skin[1] is boolean (if player
            # owns the skin)
            file.write(skin[0] + ' ' + str(skin[1]) + '\n')


def save(stats, coins, skins, curr_skin):
    """saves everything into files"""

    save_stats(stats, coins)
    save_skins(skins, curr_skin)


def read_skins():
    """reads the skins and returns currently picked skin and list of tuples (skin_name, is_owned)"""

    with open(PATH + SKINS_FILE, 'r', encoding="utf8") as file:
        curr_skin = int(file.readline())

        skins = []

        for line in file:
            # Split the line into two parts: the string and the bool
            string, boolean = line.strip().split()

            # Convert the boolean string to a bool
            boolean = boolean == 'True'
            skins.append((string, boolean))

    return (curr_skin, skins)
