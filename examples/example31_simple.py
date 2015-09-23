from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    DoActions(DisplayText('Before EUDLoopN'))

    if EUDLoopN(5):
        DoActions(DisplayText('Hello World!'))
    EUDEndLoopN()

    DoActions(DisplayText('After EUDLoopN'))


SaveMap('ex3out.scx', main)
