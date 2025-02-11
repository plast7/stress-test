stress-test 사용법 (only in mac)

1. 사용 목적

자신의 코드의 틀린 부분을 찾기 어려울 때, 반례를 찾아주기 위한 도구입니다.
(1) 테스트 케이스를 생성하고, (2) 자신의 코드와, (3) 조금 더 느리지만 정답을 출력하는 코드를 작성하는 방식으로 구성되어 있습니다.

2. 사용 방법

a. gen.py (testcase generate)

![스크린샷 2024-05-10 오전 10 32 18](https://github.com/plast7/stress-test/assets/92560356/9b48ad3f-73df-48c6-a338-d422b9dc33ef)

랜덤하게 테스트케이스를 생성합니다. 테스트케이스를 생성할 때에는 제한을 너무 크게 설정하지 않아서, 느린 코드에서도 충분히 시간 안에 돌아갈 수 있도록 함에 유의합니다.

python을 이용해 테스트케이스 생성하는 방법은 이런 블로그들을 참고해서 사용해 보세요.

https://veggie-garden.tistory.com/37

b. program1.cpp (real code)

![스크린샷 2024-05-10 오전 10 33 50](https://github.com/plast7/stress-test/assets/92560356/f28049f4-da3b-404f-8e1d-cd53a030a6ac)

틀리고 있는 여러분의 코드를 그대로 복사합니다.

c. program2.cpp (slow, but accurate code)

![스크린샷 2024-05-10 오전 10 34 48](https://github.com/plast7/stress-test/assets/92560356/d86b724d-1f38-48fe-8fa2-6df0569a4ca5)

시간복잡도를 신경쓰지 않고, 확실하게 답을 맞출 수 있는 쉬운 코드를 만들어 작성합니다.

d. 해당 디렉토리로 이동해, python3 test.py를 실행합니다.

사용예시

```
python3 stress_test.py program1.cpp program2.cpp
```

```
python3 stress_test.py program1.cpp program2.py
```

