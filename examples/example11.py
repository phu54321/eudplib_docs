from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    Trigger(
        conditions=[
            Always(),
        ],
        actions=[
            DisplayText('Hello World!'),
        ]
    )


SaveMap('ex1out.scx', main)
