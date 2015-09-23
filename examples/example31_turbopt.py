from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    if EUDInfLoop():
        DoActions(DisplayText('Hello World!'))
    EUDEndInfLoop()

    DoActions(DisplayText('After EUDLoopN'))


SaveMap('ex3out.scx', main)
