import pygame


with open('resources/skins/skins_info.txt', 'r', encoding="utf8") as file:
    curr_skin = int(file.readline())

    skins = []

    for line in file:
        string, boolean = line.strip().split()

        boolean = boolean == 'True'
        skins.append((string, boolean))

def can_load(skin):
    try:
        pygame.image.load('resources/skins/' + skin)
    except:
        return False
    else:
        return True

def valid_curr_skin():
    assert 0 <= curr_skin <= len(skins) - 1


def test_skins():
    for skin in skins:
        assert can_load(skin[0])

def test_stats():
    with open('resources/player_stats.txt', 'r', encoding="utf8") as file:
        stats = [int(line) for line in file.readlines()]
    assert len(stats) == 4

    for stat in stats[:-1]:
        assert 0 <= stat <= 20
