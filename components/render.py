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


class SceneCls:
    def __init__(self, width: int, height: int):
        self.xy = [
            [Tile.EMPTY for _ in range(width)] for _ in range(height)
        ]

def render(world: WorldCls, player: PlayerCls) -> list[list[Tile]]:
    scene = SceneCls(world.width, world.height)
    scene.score = {"aliens":  len(world.aliens), "bullets": len(world.bullets)}

    for a in world.aliens:
        if 0 <= a["y"] < world.height:
            scene.xy[a["y"]][a["x"]] = Tile.ENEMY
    for b in world.bullets:
        if 0 <= b["y"] < world.height:
            scene.xy[b["y"]][b["x"]] = Tile.BULLET
    scene.xy[player.y][player.x] = Tile.PLAYER
    return scene

def draw(scene: list[list[Tile]]):
    clear()
    lines = []
    for row in scene.xy:
        line = ''.join(Tile.map[t] for t in row)
        lines.append(line)
    print("\n SCORE: aliens left", scene.score.get("aliens"), ", bullets ",  scene.score.get("bullets"))
    print('\n'.join(lines))
    print("\n 'WASD' to move, 'space' to shoot, 'q/ctr+c' to quit")
