import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from enum import Enum, auto

class Tile(Enum):
    EMPTY = auto()
    WALL = auto()
    PLAYER = auto()
    ENEMY = auto()
    BULLET = auto()

from collections import defaultdict

Tile.map = defaultdict(
    lambda: '?', {
        Tile.EMPTY:  ' ',
        Tile.WALL:   'H',
        Tile.BULLET: '|',
        Tile.PLAYER: 'Å',
        Tile.ENEMY:  '¤',
    })

from components.player import PlayerCls
from components.world import WorldCls

def render(world: WorldCls, player: PlayerCls) -> list[list[Tile]]:
    scene = [
        [Tile.EMPTY for _ in range(world.width)] for _ in range(world.height)
    ]
    for a in world.aliens:
        if 0 <= a["y"] < world.height:
            scene[a["y"]][a["x"]] = Tile.ENEMY
    bullets = world.bullets
    for b in bullets:
        if 0 <= b["y"] < world.height:
            scene[b["y"]][b["x"]] = Tile.BULLET

    scene[player.y][player.x] = Tile.PLAYER
    return scene

def draw(scene: list[list[Tile]]):
    clear()
    lines = []
    for row in scene:
        line = ''.join(Tile.map[t] for t in row)
        lines.append(line)
    print('\n'.join(lines))
    print("\n 'WASD' to move, 'space' to shoot, 'q/ctr+c' to quit")
