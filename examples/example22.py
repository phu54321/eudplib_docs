from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    a = EUDVariable()
    b = EUDVariable()

    a << 10
    b << 20

    Trigger(
        conditions=[
            a == b  # ＝
        ],
        actions=[
            DisplayText("1")
        ]
    )

    Trigger(
        conditions=[
            a >= b  # ≥
        ],
        actions=[
            DisplayText("2")
        ]
    )

    Trigger(
        conditions=[
            a < b  # <
        ],
        actions=[
            DisplayText("3")
        ]
    )

    Trigger(
        conditions=[
            a != b  # ≠
        ],
        actions=[
            DisplayText("4")
        ]
    )


SaveMap('ex2out.scx', main)
