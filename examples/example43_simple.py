from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    DoActions(DisplayText('''\
*******
*  *  *
*  *  *
*******
*  *  *
*  *  *
*******'''))

SaveMap('ex4out.scx', main)
