# 이렇게 # 로 시작되는건 주석이라고 해가지고
# 설명같은거 적을때 쓰는거에요.

from eudplib import *

# 트리거를 제외한 모든 정보가 있는 basemap을 불러온다.
LoadMap('basemap.scx')  # basemap의 이름이 basemap.scx


# 모든 eudplib 트리거는 def main(): 다음에 들여쓰기되어있습니다.
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


# 위에 LoadMap으로 불러온 basemap.scx랑 eudplib 트리거가 들어있는 main 함수를
# 합쳐서 ex1out.scx를 만듭니다.
SaveMap('ex1out.scx', main)
