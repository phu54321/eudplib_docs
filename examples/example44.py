from eudplib import *

LoadMap('basemap.scx')


@EUDFunc
def main():
    v = EUDVariable()
    v << 0

    # ------- 반복문 시작

    # 반복문의 시작지점
    ls = NextTrigger()
    # 유닛번호 v 유닛을 (2v + 1)개 만든다.
    DoActions(CreateUnit(2 * v + 1, v, "Anywhere", P1))
    v += 1  # v에 1을 더한다
    EUDJumpIfNot(v == 6, ls)  # v가 5가 아니면 다시 ls로 점프

    # ------- 반복문 끝


SaveMap('ex4out.scx', main)
