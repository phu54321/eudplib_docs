from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    v = EUDVariable()
    v << 0

    if EUDWhileNot(v == 6):
        DoActions(
            CreateUnit(2 * v + 1, v, "Anywhere", P1)
        )
        v += 1
    EUDEndWhile()


SaveMap('ex4out.scx', main)
