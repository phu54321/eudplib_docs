from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    DoActions(DisplayText('Before'))
    if EUDLoopN(5):
        DoActions(DisplayText('EUDLoopN'))
    EUDEndLoopN()
    DoActions(DisplayText('After'))


SaveMap('ex3out.scx', main)

