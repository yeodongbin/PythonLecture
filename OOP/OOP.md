
#접근자
variable   # public  
__variable # private

#self 매개변수
this 와 유사 -> 객체를 가르킨다.

#객체 생성 매서드, 초기화 매서드
__name__
__init__

#정적매서드, 클래스 매서드
@staticmethod
@classmethod

#상속
부모 클래스의 init매서드를 꼭 설정해줘야 한다.

#오버라이딩

#다중상속

#추상 클래스
from abc import ABCMeta
from abc import abstractmethod

class Calculator(metaclass = ABCMeta):

@abstractmethod

#super()