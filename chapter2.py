from math import pi


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def remainder(num1, num2):
    return num1 % num2


def squared(num, indices):
    return num ** indices


def quotient(num1, num2):
    return num1 // num2


myString = """Life is to short, You need python"""

upper_string = "HI ALL"

under_string = "hi all"

greeting = " Hi "

odd = [1, 3, 5, 7, 9]

even = [2, 4, 6, 8, 10]

strings = [1, 2, 3, ['self', 'b', 'c', 'd', 'e']]

set_a = set([1, 2, 3, 4, 5])
set_b = set([4, 5, 6, 7, 8, 9, 10])
finalList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

is_day = False
is_light_on = not is_day

if __name__ == '__main__':
    print("타입 확인 시작".center(20, '#'))
    integer = 1
    print(type(integer), integer)
    a = 1.2
    print(type(a), a)
    print(type(myString), myString)
    data = {
        '시스템유틸리티제작': True
        , 'GUI 프로그래밍': True
        , 'C/C++와의결합': True
        , '웹 프로그래밍': True
        , '수치연산프로그래밍': True
        , '데이터베이스프로그래밍': True
        , '데이터분석_IoT': True
        , '시스템프로그래밍': False
        , '모바일프로그래밍': False
    }
    print(type(data), data)
    myList = range(0, 10)
    print(type(myList), myList)
    myList2 = []
    for i in myList:
        myList2.insert(i, i)
    print(type(myList2), myList2)
    print(type(set_a), set_a)
    print(type(finalList), finalList)
    print(type(is_day), is_day)
    print(type(is_light_on), is_light_on)
    print("타입 확인 끝".center(20, '#'))
    print("숫자 사칙연산시작".center(20, '#'))
    print(f"""더하기: 1+1 = {add(1, 1)}""")
    print(f"""빼기: 15-12 = {subtract(15, 12)}""")
    print(f"""곱하기: 3*7 = {multiply(3, 7)}""")
    print(f"""나누기: 3/4 = {division(3, 4)}""")
    print(f"""몫: 3/4 = {quotient(3, 4)}""")
    print(f"""나머지: 3/4 = {remainder(3, 4)}""")
    print(f"""제곱: 2**3 = {squared(2, 3)}""")
    print("숫자사칙연산시작끝".center(20, '#'))
    print("문제풀이 시작".center(20, '#'))
    print("숫자 14를 3으로 나누었을 때 몫과 나머지")
    print(f"""몫: 14/3 = {quotient(14, 3)}""")
    print(f"""나머지: 14/3 = {remainder(14, 3)}""")
    print("문제풀이 끝".center(20, '#'))
    print("문자열 연산".center(20, '#'))
    head = "Python"
    tail = " is fun"
    print("문자열 더하기:", add(head, tail))
    print("문자열 곱하기:", multiply(head, 3))
    print("문자열 길이:", len(myString.split(',')[0].strip()))
    print("문자열 연산끝".center(20, '#'))
    print("문제풀이 시작".center(20, '#'))
    print("You need python 문장을 문자열로 만들고 길이를 구해 보자")
    print(myString.split(',')[1].strip() + " 길이:", len(myString.split(',')[1].strip()))
    print("문제풀이 끝".center(20, '#'))
    print("문자열슬라이싱".center(20, '#'))
    print("myString[0:4]:", myString[0:4])
    print("myString[0:4:2]:", myString[0:4:2])
    print("myString[:8]:", myString[:8])
    print("myString[8:]:", myString[8:])
    print("문자열슬라이싱끝".center(20, '#'))
    print("문자열인덱싱".center(20, '#'))
    print("myString[3]:", myString[3])
    print("myString[-3]:", myString[-3])
    print("문자열인덱싱끝".center(20, '#'))
    print("문자열치환".center(20, '#'))
    print("python -> Python", myString.replace("python", "Python"))
    print("문자열치환끝".center(20, '#'))
    print("문자열 포맷팅".center(20, '#'))
    number = 10
    day = "삼"
    print("저는 사과 %d개를 먹었습니다. 그래서 저는 %s일동안 아팠습니다." % (number, day))
    print(f"""시스템유틸리티제작: {data['시스템유틸리티제작']}""")
    print("정렬과 공백:", "%10smy crews" % upper_string)
    print("정렬과 공백:", "%-10smy crews" % upper_string)
    print("소수점 표현하기", "%0.4f" % pi)
    print("문자열 포맷팅 끝".center(20, '#'))
    print("문제풀이".center(20, '#'))
    print("""format 함수 또는 f문자열 포매팅을 사용해 '!!!python!!!'문자열을 출력해보자""")
    print(f"""{'python':!^12}""")
    print("문제풀이 끝".center(20, '#'))
    print("문자열 관련 함수".center(20, '#'))
    words = myString.split(" ")
    print("문자 개수 세기(myString): ", myString.count('i'))
    print("문자위치 알려주기(find):", myString.find('You'))
    print("문자위치 알려주기(index):", myString.index('o'))
    a = 'abcd'
    print("','.join('abcd') =>", ','.join(a))
    print("소문자를 대문자로 바꾸기", under_string.upper())
    print("대문자를 소문자로 바꾸기", upper_string.lower())
    print("왼쪽공백 지우기", greeting.lstrip())
    print("오른쪽공백 지우기", greeting.rstrip())
    print("양쪽공백 지우기", greeting.strip())
    print("문자열 치환", myString.replace("Life", "Your reg"))
    print("문자열나누기", myString.split(" "))
    print("문자열 관련 함수 끝".center(20, '#'))
    print("리스트".center(20, '#'))
    print("리스트 인덱싱:", odd[2])
    print("리스트 내 값 더하기", add(odd[0], odd[1]))
    print("리스트 even 내 마지막 요소", even[-1])
    print("리스트 strings에 포함된 'self' 값을 인덱싱을 사용해 출력", strings[-1][0])
    print("리스트 슬라이싱 odd[0:2]:", odd[0:2])
    A = list(range(1, 6))
    print(f"""A={A} 리스트에서 슬라이싱 기법을 사용하여 리스트 [2,3]을 만들어보자""")
    print("정답:", A[1:3])
    print("리스트더하기: ", odd + even)
    print("리스트반복하기: ", odd * 3)
    print("리스트길이구하기", len(odd))
    print("리스트 값 수정, A[4] =", A[4])
    A[4] = 7
    print("리스트 값 수정, A[4] =", A[4])
    A = list(range(1, 6))
    print("del 함수 사용해 리스트 요소 삭제, 원래는", A)
    del A[2]
    print("삭제후", A)
    A = list(range(1, 6))
    del A[2:]
    print("슬라이싱으로 한꺼번에 삭제", A[:2])
    A.append(3)
    A.append(4)
    A.append(5)
    print("리스트 요소 추가", A)
    A.append([6, 7])
    print("리스트 요소 추가", A)
    C = odd + even
    print("C=", C)
    C.sort()
    print("리스트 정렬", C)
    C.reverse()
    print("리스트 뒤집기", C)
    C.insert(0, 11)
    print("리스트요소삽입 ", C)
    C.remove(3)
    print("리스트 요소 삭제", C)
    print("리스트 요소 끄집어내기", C.pop())
    print("리스트 요소 끄집어내기", C.pop(1))
    print("끄집어낸 요소는 삭제됨", C)
    print("리스트 요소 갯수 세기", C.count(7))
    C.extend([1, 0])
    print("리스트확장", C)
    print("리스트 끝".center(20, '#'))
    print("튜플".center(20, '#'))
    print("리스트는 저장된 항목의 변경이 가능하지만, 튜플은 불가능하다.")
    print("튜플 슬라이싱", finalList[:3])
    t2 = (11, 12)
    print("튜플더하기", finalList + t2)
    print("튜플 곱하기", multiply(finalList, 3))
    print("튜플 길이구하기", len(finalList))
    print("튜플 끝".center(20, '#'))
    print("딕셔너리".center(20, '#'))
    print("딕셔너리", data)
    print("딕셔너리 Key만 출력", data.keys())
    keys = data.keys()
    print("딕셔너리 내용 출력")
    for name in keys:
        print(name + ":", data.get(name))
    data2 = data
    print(data.items())
    print("데이터2 확인", data2)
    data2.clear()
    print("데이터2 clear", data2)
    print("딕셔너리 끝".center(20, '#'))
    print("집합 자료형".center(20, '#'))
    print("집합 자료형", set_a)
    str_set = set("Hello")
    print("문자 집합", str_set)
    print("집합 self=", set_a, "집합 b=", set_b, "교집합=", set_a & set_b)
    print("집합 self=", set_a, "집합 b=", set_b, "교집합=", set_a.intersection(set_b))
    print("집합 self=", set_a, "집합 b=", set_b, "합집합=", set_a.union(set_b))
    print("집합 self=", set_a, "집합 b=", set_b, "차집합=", set_a.difference(set_b))
    set_c = set([1, 2, 3])
    set_c.add(4)
    print("집합 c에 4를 추가", set_c)
    set_c.update([5, 6])
    print("집합 c에 5,6를 추가", set_c)
    print("집합 자료형 끝".center(20, '#'))
