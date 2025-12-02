import os, sys

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


class SceneCls:
    def __init__(self, width: int, height: int):
        self.xy = [
            [Tile.EMPTY for _ in range(width)] for _ in range(height)
        ]

def render(world: WorldCls, player: PlayerCls) -> list[list[Tile]]:
    scene = SceneCls(world.width, world.height)
    scene.score = {"aliens":  len(world.aliens), "bullets": len(world.bullets)}
    scene.game_over = len(world.aliens) == 0

    for a in world.aliens:
        if 0 <= a["y"] < world.height:
            scene.xy[a["y"]][a["x"]] = Tile.ENEMY
    for b in world.bullets:
        if 0 <= b["y"] < world.height:
            scene.xy[b["y"]][b["x"]] = Tile.BULLET
    scene.xy[player.y][player.x] = Tile.PLAYER
    return scene

def overlay_message(scene: list[list[Tile]], msg: str):
    height, width = len(scene), len(scene[0])
    y, x = ((height - 1) // 2), (width - len(msg)) // 2
    for i, ch in enumerate(msg):
        if 0 <= x + i < width:
            scene[y][x + i] = ch

def draw(scene: list[list[Tile]]):
    rows = [[Tile.map[t] for t in row] for row in scene.xy]
    if scene.game_over:
        overlay_message(rows, "!!! GAME OVER !!!")
    lines = []
    for row in rows:
        line = ''.join(row)
        lines.append(line)
    if scene.game_over:
        lines.append(f"All aliens defeated! press 'R' to restart.")
    else:
        lines.append("'WASD' to move, 'space' to shoot")
    lines.append("'q/ctr+c' to quit")

    clear()
    print('\n'.join(lines))
    sys.stdout.flush()
