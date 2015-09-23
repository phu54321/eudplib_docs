from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    var = EUDVariable()  # var라는 변수 하나를 만든다.
    var << 15  # var에 15을 넣는다.
    DoActions([
        SetResources(P1, SetTo, var, Ore)
    ])

    var << (var * 30 + 25) // 4  # var에 (var * 30 + 25) // 4 를 넣는다.
    DoActions([
        SetResources(P1, SetTo, var, Gas)
    ])

SaveMap('ex2out.scx', main)
