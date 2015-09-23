from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    userpl = f_getuserplayerid()  # 내가 몇플레이어인지 알아낸다.

    Trigger(
        conditions=[
            Always(),
        ],
        actions=[
            SetCurrentPlayer(userpl),  # Current player를 '나'로 설정.
            DisplayText('Hello World!'),  # '나'에게만 Display Text하면 된다.
        ]
    )


SaveMap('ex1out_fixed.scx', main)
