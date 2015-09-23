기초 1강. eudplib
============================================

eudplib란?
----------

eudplib는 EUD 트리거를 이용해서 기존에 있던 트리거보다 더 많은 일을 하는
트리거를 더 쉽게 짤 수 있도록 해주는 툴입니다. eudplib로 만든 트리거로는

- 모든 유닛들 각각의 구조오프셋을 다룰 수 있습니다.
- 커스텀 GRP나 버튼셋 등을 쉽게 만들 수 있습니다.
- 기존 트리거들도 모두 호환이 됩니다.
- 시간에 따라, 플레이어에 따라 서로 다른 트리거가 발동되도록 할 수 있습니다.
- 드래프트로 할 수 있는 많은 일들이 가능합니다.

eudplib를 익히다보면 금방 여러 예제들을 짤 수 있을거에요.




eudplib 설치
------------

eudplib 설치부터 해봅시다. eudplib는 파이썬에서 돌아가는 프로그램이기 때문에,
파이썬을 깔아야 합니다.


1. 파이썬과 pip 설치

   1. 파이썬 홈페이지(http://python.org)에 접속합니다.
   2. Download → Download Python 3.x.x 버튼을 클릭해서 설치 파일을 받습니다.

      .. only:: html
          .. image:: ar1_p1.png

          |

   3. 지시에 따라서 설치합니다.

      .. image:: ar1_p2.png

      .. note::
          설치할 구성 요소를 고를 때 위 그림처럼 "pip"와 "Add python.exe to
          Path" 를 꼭 체크하세요. (텍스트 왼쪽의 아이콘이 위 그림처럼 되도록)

   .. note::
       Python 3.4 버젼 이후로는 파이썬을 설치하면 pip가 같이 설치됩니다.
       만약 파이썬 3.3 버젼 이전 버젼을 이미 쓰고 계시다면
       https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
       를 get-pip.py라는 이름으로 저장해서 실행시키면 pip를 따로 설치할 수
       있습니다.


2. eudplib 설치

   1. 시작 → 보조프로그램 → 명령 프롬프트  (또는 실행 → cmd)
   2. :literal:`pip install eudplib` [엔터] 로 eudplib를 설치합니다.

      .. only:: html
          .. image:: ar1_p3.png

          |

3. 설치 확인

   1. 시작 → 보조프로그램 → 명령 프롬프트  (또는 실행 → cmd)
   2. :literal:`python` [엔터] 로 파이썬 인터프리터를 실행시킵니다.
   3. :code:`import eudplib` [엔터] 후 아래 그림처럼 아무 에러도 뜨지 않으면
      설치가 성공한겁니다.

      .. only:: html
      
          .. image:: ar1_p4.png

          |



eudplib 트리거는 코드로 짠다
----------------------------

이렇게 eudplib를 설치했습니다. 그런데 eudplib를 설치했다고는 하는데 사실 뭐가
어떻게 되가는건지 감이 잘 안잡히실것같습니다. eudplib는 파이썬용
라이브러리입니다. SCMDraft2에서 트리거 에디터를 써서 맵 트리거를 수정할 수
있잖아요? 파이썬에서 eudplib를 써서 맵 트리거를 넣을 수 있습니다. eudplib는
그냥 이런 종류의 맵을 만들 때 쓰는 부품 정도로 생각하시면 되요. 

eudplib 트리거는 SCMDraft2의 Trigger Editor (Classic이 붙지 않는것) 처럼
**코드로** 만듭니다. 밑의 코드는 eudplib 프로그램의 예시 코드입니다. ::

    from eudplib import *


    LoadMap('basemap.scx')

    @EUDFunc
    def main():
        Trigger(
            actions=[
                DisplayText('Hello, World!')
            ]
        )

    SaveMap('out.scx', main)


eudplib를 설치했다는것은 위에 나온 :code:`from eudplib import *` 를 사용할 수
있다는 의미입니다. eudplib에서는 코드를 이용해서 트리거를 짠다는걸 기억하세요.


.. note::

    위 예제 코드를 TrigEditPlus 형식으로 표현하자면 아래와 같습니다.

    .. code-block:: lua

        Trigger {
            players = {P1},
            actions = {
                DisplayText('Hello, World!', 4);
            }
        }

    비슷하지만 eudplib 코드에는 :code:`players = {P1}` 이 없는 차이점이 있죠.
    앞으로 이런 차이점들이 왜 나는지, 이 차이점이 어떤 의미를 가지는지 차차
    0설명하겠습니다.

