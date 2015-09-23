from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    Trigger(
        conditions=[
            Always(),
        ],
        actions=[
            SetCurrentPlayer(P1), DisplayText('Hello World!'),
            SetCurrentPlayer(P2), DisplayText('Hello World!'),
            SetCurrentPlayer(P3), DisplayText('Hello World!'),
            SetCurrentPlayer(P4), DisplayText('Hello World!'),
            SetCurrentPlayer(P5), DisplayText('Hello World!'),
            SetCurrentPlayer(P6), DisplayText('Hello World!'),
            SetCurrentPlayer(P7), DisplayText('Hello World!'),
            SetCurrentPlayer(P8), DisplayText('Hello World!'),
        ]
    )


SaveMap('ex1out_fixed.scx', main)
