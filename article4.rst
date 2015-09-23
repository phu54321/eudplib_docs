기초 4강. 트리거 실행 순서, 조건문
==================================

.. warning::
    앞으로 강좌에서는 스타를 창모드로 해놓는걸 추천합니다. 이번 강좌부터는
    예제에서 오타를 치면 스타가 멈출 수 있습니다. 전체모드 스타는 강제종료하기
    조금 짜증나므로, 창모드 스타로 테스트할 수 있으면 스타를 창모드로 해두세요.

    사실 이번 강좌엔 별 실행할만한 예제가 없긴 합니다.



eudplib에서의 트리거는 기존 맵에디터에서의 트리거랑은 몇가지 차이점이 있습니다.
조건이 맞으면 액션을 실행한다는 기본적인 개념은 똑같지만, 트리거가 실행되는
순서에 따른 차이점이 좀 있습니다. 이번 강좌에서는

- 트리거 실행 순서에 대해 배웁니다.
- EUDJump, EUDJumpIf, EUDJumpIfNot에 대해 배웁니다.
- EUDIf 에 대해 배워봅니다.




트리거 실행순서?
----------------

뭐 간단합니다. 트리거가 어떤 순서로 실행되는지에요. 예를 들어 기존 트리거가

- 트리거 A가 P1, P2, P3에게서 실행되고
- 트리거 B가 P1, P3에게서 실행되고
- 트리거 C가 P2, P3에게서 실행되고

처럼 있다고 해봅시다. 트리거 실행 순서는

- (P1이 있다면 Current Player가 P1이 되서) A, B
- (P2이 있다면 Current Player가 P2이 되서) A, C
- (P3이 있다면 Current Player가 P3이 되서) A, B, C

처럼 되겠지요. 트리거는 P1~P8 순서대로, 각 플레이어마다는 트리거 순서대로
돌아갑니다. 그런데 eudplib에선 이런 규칙이 잘 적용되지 않습니다.

- 기본적으로 main 함수의 첫번째 트리거부터 순서대로 트리거가 실행됩니다.
- 제어문같은게 있을 때 트리거 실행 순서가 바뀝니다.


.. note::
    트리거 실행순서를 바꾸는걸 프로그래밍 용어로 **제어문** 이라고 합니다. 네.
    if, while, for, goto 같은거에요.




EUDJump
-------

.. note::
    C언어에서 goto에 해당합니다.

트리거 실행순서를 바꾸는 역할을 합니다. 제일 간단한 제어문이에요
예시를 하나 들죠. ::

    A = Trigger()
    B = Trigger()
    C = Trigger()
    EUDJump(B)  # A로 돌아간다.

eudplib 트리거는 기본적으로 첫번째 트리거부터 순서대로(=밑으로) 트리거가
실행된다고 했죠? 그래서 일단은 트리거 A → B → C 순서대로 실행됩니다.
C 다음에 EUDJump가 나왔네요.

EUDJump(X) 는 다음 트리거로 X를 실행시키라는 뜻입니다. 즉, EUDJump(B)를 하면
다음 트리거로 B가 실행이 되죠. 그래서 결국 트리거 실행 순서는 C → (EUDJump
→) B → C (B 다음 트리거가 C니까) → (EUDJump →) B → C → ... 순서대로
트리거가 돌아갑니다. 결국 트리거 순서는 다음과 같습니다.

::

    A → B → C → EUDJump → B → C → EUDJump → B → C → ...

.. note::
    eudplib 트리거에는 Preserve Trigger가 자동으로 적용되기 때문에 A가 한번만
    실행된다 같은 걱정은 안하셔도 됩니다. Preserve Trigger를 끄려면 ::

        Trigger(
            conditions=[~],
            actions=[~],
            preserved=False
        )

    처럼 하면 되긴 해요.


.. note::
    EUDJump도 트리거로 취급하는게 설명하기 더 편한것같아요. EUDJump같은
    제어문이나 나중에 배울 함수 호출문같은 잡다한것도 eudplib 강좌 안에서는
    전부 트리거의 일종으로 취급하겠습니다.


EUDJump를 쓰다보면 이런 식으로 좀 더 나중 트리거로 트리거 실행 순서를 옮기고
싶을때도 있을거에요. ::

    A = Trigger()
    EUDJump(D)  # 아직 D가 뭔지 모르므로 (D = Trigger() 전) 에러가 난다.
    B = Trigger()
    C = Trigger()
    D = Trigger()

이러면 D = Trigger() 전에 EUDJump(D)가 나와가지고 에러가 뜹니다. EUDJump(D)
전에 D에 뭔가를 넣어줘야하는데, 이 때 Forward()를 쓸 수 있어요. ::

    A = Trigger()

    D = Forward()  # EUDJump(D)에서 D가 필요하니까 Forward를 넣어준다.
    # Forward는 '나중에 만들 무언가' 이란 뜻.
    EUDJump(D)  # 에러가 나지 않는다.

    B = Trigger()
    C = Trigger()
    D << Trigger()  # D에 이 트리거를 넣는다. = 대신 <<를 쓴다.
    # D = Trigger()  # 이렇게 하면 나중에 Forwrad 관련 에러가 뜬다. Forward엔 <<로

제어문을 다 배우고 나면 EUDJump나 Forward를 쓸 일은 없을거에요. 하지만
알아둔다고 나쁠건 없죠.




EUDJumpIf
---------

.. note::
    C언어에서는 다음에 해당합니다. ::

        if(조건) goto 레이블;

EUDJumpIf는 조건이 맞으면 EUDJump처럼 점프하고, 아니면 뒤에 트리거를 계속
실행한다는 뜻이에요.
::

    A = Trigger()
    B = Trigger()

    # P1이 마린 30개 이상 갖고 있을 때 A로 점프
    EUDJumpIf(Bring(Player1, AtLeast, 30, 'Terran Marine', 'Anywhere'), A)


자매품으로 EUDJumpIfNot도 있어요. 조건이 만족되지 않으면 점프.




EUDIf
-----

.. note::
    C언어에서 if ~ else if ~ else 에 해당합니다.


확장된 트리거라고 보면 됩니다. 트리거가 원래 이런 구조로 되있죠. ::

    Trigger(
        조건,
        [
            액션1,
            액션2,
        ]
    )


조건이 맞으면 액션들을 실행시킨다는 뜻입니다. 그런데 맵을 만들 때 액션 실행중
다른 조건을 체크해보고싶거나 할 떄도 있을거에요. 상점 비콘 안에 시민을 넣었을
때에 스텟 레벨 돈같은 여러 조건들을 채크해보고싶을수도 있죠. 그럴 떄에 EUDIf를
쓰면 됩니다. ::

    if EUDIf(조건AAA):
        # 조건 AAA가 만족하면 이렇게 들여쓰기된 부분이 모두 실행된다.
        # 이 안에서 또 EUDIf나 EUDJump나 같은것도 들어갈 수 있다.

        Trigger(
            조건,
            액션
        )
        
        Trigger(
            조건,
            액션
        )
        
    EUDEndIf()  # EUDIf랑 대응됨.

EUDElseIf나 EUDElse까지 합쳐서 일반적인 문법은 다음과 같습니다. ::


    if EUDIf( 조건1 ):

        # 조건1이 맞을때 실행할 코드

    # 이 이후로는 생략 가능

    if EUDElseIf( 조건2 ):

        # 조건1은 안맞는데 조건2가 맞을 때 실행할 코드

    if EUDElseIf( 조건3 ):

        # 조건1, 2는 안맞는데 조건3이 맞을 때 실행할 코드

    ...

    if EUDElseIf( 조건n ):
    
        # 조건 1, 2, ... n-1는 안맞는데 조건n이 맞을 때 실행할 코드

    if EUDElse():

        # 조건 1~n이 싹 다 안맞을때 실행할 코드.

    EUDEndIf()


.. note:: :code:`if EUDIf` 부분에서 if는 들여쓰기용으로 있는겁니다. 원칙적으로는
    if나 들여쓰기 없이도 EUDIf를 쓸 수 있습니다. ::

        EUDIf( 조건 )

        코드

        EUDEndIf()

    하지만 들여쓰기하는게 코드가 보기 훨씬 좋아요. 전 들여쓰기를 할거니다.
    EUDElseIf나 EUDElse 앞에도 if를 붙여서 들여쓰기를 할껀데 앞에 있는 if는
    신경쓰지 않으셔도 됩니다.

예시로 간단한 상점을 생각해봅시다. 시민을 비콘에 올려놓았을 때

- 미네랄이 50 이하면 '돈이 없어요' 라는 텍스트를 띄웁니다.
- 가스가 30 이하면 '가스가 없어요' 라고 텍스트를 띄웁니다.
- 둘 다 만족한다면 마린 하나를 뽑습니다.

EUDIf를 써서 이걸 표현한다면 이렇게 됩니다. ::

    # Current Player는 이미 적당히 설정되어있다 가정합시다.

    if EUDIf(Bring(CurrentPlayer, AtLeast, 1, 'Terran Civilian', 'Beacon')):

        if EUDIf(Accumulate(CurrentPlayer, AtMost, 49, Ore)):
            # 미네랄이 49 이하일 때
            DoActions(DisplayText('돈이 없어요.'))

        # EUDIfNot, EUDElseIfNot 을 쓰면 '해당 조건이 만족 안할때' 를 인식할 수 있어요.
        if EUDElseIfNot(Accumulate(CurrentPlayer, AtLeast, 30, Gas)):
            # (미네랄이 49 이하일 때)가 아니고 (가스다 30 이상일 때)가 아닐 떄
            DoActions(DisplayText('가스가 없어요.'))

        if EUDElse():
            # 나머지 경우 : 돈도 있고 가스도 있고
            DoActions([
                SetResource(CurrentPlayer, Subtract, 50, Ore),
                SetResource(CurrentPlayer, Subtract, 30, Gas),
                CreateUnit(1, 'Terran Marine', 'Anywhere', CurrentPlayer),
                DisplayText('마린을 뽑았습니다.')
            ])

        EUDEndIf()

    EUDEndIf()

코드 생김새가 기존 트리거랑은 많이 다르죠. 원래 eudplib 코드가 이래요.
EUDVariable을 본격적으로 활용하게 되면 정말 EUDIf를 미친듯이 쓰게 될겁니다.


.. note::
    EUDIf틑 EUDJumpIf로 만들 수 있습니다. 예를 들어 다음 코드는 ::

        if EUDIf(A):
            B
        EUDEndIf()

    다음과 같습니다. ::

        ife = Forward()
        EUDJumpIf(A, ife)
        B
        ife << NextTrigger()  # NextTrigger는 '바로 뒤에 트리거'를 나타낸다.

    EUDIf나 EUDWhile같은걸 잘 쓰면 Forward() 같은걸 쓰지 않고도 Forward()
    효과를 쉽게 낼 수 있어요.


연습문제
--------

1. 다음 코드에서 출력되는 메세지는? ::

    v = EUDVariable()
    v << 30

    if EUDIf(v < 30):
        if EUDIf(v < 15):
            DoActions(DisplayText('A'))
        if EUDElse():
            DoActions(DisplayText('B'))
        EUDEndIf()
        DoActions(DisplayText('C'))

    if EUDElseIf(v < 60):
        if EUDIf(v == 30):
            DoActions(DisplayText('30'))
        if EUDElseIf(v < 50):
            DoActions(DisplayText('50'))
        if EUDElse():
            DoActions(DisplayText('70'))
        EUDEndIf()
        DoActions(DisplayText('90'))

    EUDEndIf()
    DoActions(DisplayText('110'))
