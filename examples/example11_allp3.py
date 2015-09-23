from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    Trigger(
        conditions=[
            Always(),
        ],
        actions=[
            [
                SetCurrentPlayer(player),
                DisplayText('Hello World!'),
            ] for player in range(8)
        ]
    )


SaveMap('ex1out_fixed.scx', main)
