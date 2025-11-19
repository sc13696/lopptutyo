import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from enum import Enum, auto

class Tile(Enum):
    EMPTY = auto()
    WALL = auto()
    PLAYER = auto()
    ENEMY = auto()

from collections import defaultdict

Tile.map = defaultdict(
    lambda: '?', {
        Tile.EMPTY:  ' ',
        Tile.WALL:   '|',
        Tile.PLAYER: 'Å',
        Tile.ENEMY:  '¤',
    })

from components.player import PlayerCls
from components.world import WorldCls

def render(world: WorldCls, player: PlayerCls):
    scene = [
        [Tile.EMPTY for _ in range(world.width)] for _ in range(world.height)
    ]
    scene[player.y][player.x] = Tile.PLAYER
    return scene

def draw(scene: list[list[Tile]]):
    Tile.map
    clear()
    lines = []
    for row in scene:
        line = ''.join(Tile.map[t] for t in row)
        lines.append(line)
    print('\n'.join(lines))
    print("\n WASD to move (q to quit)")
