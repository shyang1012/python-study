from copy import *


def is_odd(num):
    if num % 2 == 1:
        return "홀수"
    else:
        return "짝수"


def get_sex(cd):
    return {1: "남",
            2: "여",
            3: "남",
            4: "여",
            5: "남",
            6: "여",
            7: "남",
            8: "여",
            9: "남",
            0: "여"}.get(cd)


def q1():
    data = {
        "국어": 80,
        "영어": 75,
        "수학": 55
    }
    result = 0
    keys = data.keys()
    print("q1. 홍길동씨의 과목별 점수는 다음과 같다 홍길동씨의 평균점수를 구해보자")
    print("과목", "점수")
    for name in keys:
        print(name, data.get(name))

    for name in keys:
        result += data.get(name)
    print("평균: %2d" % (result / len(keys)))


def q2():
    print("q2.자연수 13이 홀수인지 짝수인지 판별하는 방법에 대해 말해보자")
    print(is_odd(13))


def q3():
    print("""q3.홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 
    주민등록번호를 연월일 부분과 그 뒤의 숫자부분으로 나누어 출력해보자.
    """)
    pin = "881120-1068234"
    yyyymmdd = pin.split("-")[0]
    num = pin.split("-")[1]
    print("연월일부분:", yyyymmdd)  # 연월일부분 출력
    print("숫자부분:", num)  # 숫자부분 출력


def q4():
    print("q4.주민등록번호 뒷자리의 맨 첫번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자")
    pin = "881120-1068234"
    sex_cd = int(pin.split("-")[1][0])
    print("주민등록번호:", pin, "성별구분코드:", sex_cd, "성별판독결과:", get_sex(sex_cd))


def q5():
    print("""q5.다음과 같음 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꾸어서 출력해보자""")
    a = "a:b:c:d"
    b = a.replace(":", "#")
    print(b)


def q6():
    print("""q6.[1,3,5,4,2]리스트를 [5,4,3,2,1]로 만들어보자""")
    a = [1, 3, 5, 4, 2]
    a.sort()
    a.reverse()
    print(a)


def q7():
    print("q7.['Life','is','too','short']리스트를 Life is to short 문자열로 만들어 출력해보자")
    a = ['Life', 'is', 'too', 'short']
    result = " ".join(a)
    print(result)


def q8():
    print("q8.(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어서 출력해보자")
    a = (1, 2, 3)
    a += (4,)
    print(a)


def q9():
    print("""q9.다음과 같은 딕셔너리 a가 있다
    >>> a = dict()
    >>> a
    {}
    다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해보자.
    1) a['name']='python'
    2) a[('a',)]='python'
    3) a[[1]]='python'
    4) a[250]='python'
    """)
    print("정답: 3번, 이유: TypeError: unhashable type: 'list'")
    print("실행결과")
    a = dict()
    a[250] = 'python'
    print(a)


def q10():
    print("q10. 딕셔너리 a에서 'B'에 해당하는 값을 추출해 보자")
    a = {
        'A': 90
        , 'B': 80
        , 'C': 70
    }
    result = a.get('B')
    print(a)
    print(result)


def q11():
    print("q11. a 리스트에서 중복 숫자를 제거해보자")
    a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
    aSet = set(a)
    b = list(aSet)
    print(b)


def q12():
    print("""q12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a,b 변수를
    선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 나오는 이유에 대해 설명해보자.
    """)
    a = b = [1, 2, 3]
    a[1] = 4
    print(b)
    print("""이유: 파이썬은  passed by assignment 방식으로 변수값의 메모리를 참조한다.
    가변(mutable) 타입인지, 불변(imnutable)타입인지에 따라서 변수 값 전달방식이 바뀐다.
    불변 타입인 경우는 본래 변수 값이 변할 위험이 있기 때문에 call by value로 값이 전달되는 것처럼 보이고
    (실제로 주소를 가르킴에도)
    가변 타입인 경우는 call by Reference 로 전달되는 것으로 보인다.
    
    따라서 리스트는 가변타입이므로  call by Reference 로 값이 전달되므로 a[1] = 4를 대입하면 같은 
    메모리 주소를 바라보는 b[1]의 값도 4로 변경된다.이를 변경되지 않기 위해서는 다음과 같이 한다.
    """)
    a = [1, 2, 3]
    b = deepcopy(a)
    a[1] = 4
    print("a=", a)
    print("b=", b)


if __name__ == '__main__':
    print("02장 연습문제-힘내세요")
    q1()
    print("===================")
    q2()
    print("===================")
    q3()
    print("===================")
    q4()
    print("===================")
    q5()
    print("===================")
    q6()
    print("===================")
    q7()
    print("===================")
    q8()
    print("===================")
    q9()
    print("===================")
    q10()
    print("===================")
    q11()
    print("===================")
    q12()
