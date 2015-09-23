from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    i = EUDVariable()
    i << 0

    if EUDWhile(i < 7):
        mod3 = i % 3

        # Trigger(a, b)는 a가 조건이고 b가 액션인 트리거
        # ex) Trigger(Always(), CreateUnit(~))
        # ex) Trigger(
        #         # 조건
        #         [
        #             Bring(P1, AtLeast, 30, 'Men', 'Anywhere'),
        #             Deaths(P1, Exactly, 0, 'Terran Marine')
        #         ],
        #         # 액션
        #         DisplayText('AAAAAAAAAAAAAAA')
        #     )

        Trigger(
            mod3 == 0,  # 조건
            DisplayText('*******')  # 액션
        )

        Trigger(
            mod3 >= 1,
            DisplayText('*  *  *')
        )

        # 반복문을 1번 돌때마다 i에 1씩 더합니다.
        i += 1

    EUDEndWhile()

SaveMap('ex4out.scx', main)
