from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    Trigger(
        conditions=[
            Always(),
        ],
        actions=[
            SetCurrentPlayer(P2),  # Current player를 P2로 설정
            DisplayText('Hello World!'),
        ]
    )


SaveMap('ex1out_fixed.scx', main)
