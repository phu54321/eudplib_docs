from eudplib import *

LoadMap('basemap_s2z.scx')


@EUDFunc
def main():
    if EUDWhile(Bring(P1, AtLeast, 1, 'Protoss Scout', 'Anywhere')):
        DoActions([
            MoveLocation('loc', 'Protoss Scout', P1, 'Anywhere'),
            RemoveUnitAt(All, 'Protoss Scout', 'loc', P1),
            CreateUnit(1, 'Zerg Zergling', 'loc', P1),
        ])
    EUDEndWhile()

SaveMap('ex4out.scx', main)
