import re


def regex_match(regex, check_str, group_name, method_type="group"):
    """
    match 메서드는 문자열의 처음부터 정규식과 매치되는지 조사한다.
    match 객체의 메소드
    group(): 매치된 문자열을 돌려준다.
    start(): 매치된 문자열의 시작위치를 알려준다.
    end(): 매치된 문자열의 끝 위치를 알려준다.
    span(): 매치된 문자열의 (시작,끝)에 해당하는 튜플을 돌려준다.
    :param group_name: 정규식에서 (?P<name>\w+)와 같이 그룹명을 지정한 경우의 그룹명
    :param method_type: group, start, end, span 네가지 메소드, 기본은 group
    :param regex: 정규식
    :param check_str: 테스트 문자열
    :return:
    """
    print("regex_match 실행", "[정규식:", regex, "테스트 문자열:", check_str, "그룹명:", group_name, "출력메소드타입", method_type, "]")
    p = re.compile(regex)
    m = p.match(check_str)
    if m:
        if method_type == 'group':
            if group_name != "":
                print("Match found:", m.group(group_name))
                return m.group(group_name)
            else:
                print("Match found:", m.group())
                return m.group()
        elif method_type == 'start':
            if group_name != "":
                print("Match found:", m.start(group_name))
                return m.start(group_name)
            else:
                print("Match found:", m.start())
                return m.start()
        elif method_type == 'end':
            if group_name != "":
                print("Match found:", m.end(group_name))
                return m.end(group_name)
            else:
                print("Match found:", m.end())
                return m.end()
        elif method_type == 'span':
            if group_name != "":
                print("Match found:", m.span(group_name))
                return m.span(group_name)
            else:
                print("Match found:", m.span())
                return m.span()
    else:
        print("No match")
        return None


def regex_search(regex, check_str, group_name, method_type="group"):
    """
    search 메서드는 문자열 전체가 정규식과 매치되는지 조사한다.
    :param group_name: 정규식에서 (?P<name>\w+)와 같이 그룹명을 지정한 경우의 그룹명
    :param method_type: group, start, end, span 네가지 메소드, 기본은 group
    :param regex: 정규식
    :param check_str: 테스트 문자열
    :return:
    """
    print("regex_search 실행", "[정규식:", regex, "테스트 문자열:", check_str, "그룹명:", group_name, "출력메소드타입", method_type, "]")
    p = re.compile(regex)
    m = p.search(check_str)
    if m:
        if method_type == 'group':
            if group_name != "":
                print("Match found:", m.group(group_name))
                return m.group(group_name)
            else:
                print("Match found:", m.group())
                return m.group()
        elif method_type == 'start':
            if group_name != "":
                print("Match found:", m.start(group_name))
                return m.start(group_name)
            else:
                print("Match found:", m.start())
                return m.start()
        elif method_type == 'end':
            if group_name != "":
                print("Match found:", m.end(group_name))
                return m.end(group_name)
            else:
                print("Match found:", m.end())
                return m.end()
        elif method_type == 'span':
            if group_name != "":
                print("Match found:", m.span(group_name))
                return m.span(group_name)
            else:
                print("Match found:", m.span())
                return m.span()
    else:
        print("No match")
        return None


def regex_findall(regex, check_str):
    """
    findall 메서드는 check_str의 단어를 reg의 정규식과 매칭해서 리스트로 돌려준다.
    :param regex:
    :param check_str:
    :return:
    """
    print("regex_findall 실행", "정규식:", regex, "테스트 문자열:", check_str)
    p = re.compile(regex)
    result = p.findall(check_str)
    print(result)
    return result


def regex_finditer(regex, check_str):
    """
    finditer 메서드는 findall과 동일하지만 그 결과로 반복 가능한 객체를 돌려준다..
    반복가능한 객체가 포함하는 각각의 요소는 match객체이다.
    :param regex:
    :param check_str:
    :return:
    """
    print("regex_finditer 실행", "정규식:", regex, "테스트 문자열:", check_str)
    p = re.compile(regex)
    result = p.finditer(check_str)
    return result


def hexrepl(match):
    value = int(match.group())
    return hex(value)


if __name__ == '__main__':
    """ 
    https://regex101.com/ 에서 기본적인 정규식은 테스트 가능하다.
    """
    reg = r"[a-z]+"
    chk_str = "python"
    chk_str2 = "3 python"
    chk_str3 = "life is too short"
    regex_match(reg, chk_str, "")
    regex_match(reg, chk_str2, "")
    regex_search(reg, chk_str, "")
    regex_search(reg, chk_str2, "")
    regex_findall(reg, chk_str3)
    result = regex_finditer(reg, chk_str3)
    for r in result:
        print(r)

    print("regex_match 메소드별 출력값 확인")
    regex_match(reg, chk_str, "", "group")
    regex_match(reg, chk_str, "", "start")
    regex_match(reg, chk_str, "", "end")
    regex_match(reg, chk_str, "", "span")

    print("\n 모듈단위 수행 확인")
    m = re.match(reg, chk_str)
    print(m)

    print("\n 전화번호 정규식 테스트")
    phone_reg = r"(?P<name>\w+)(?P<phone>\s+\d+[-]\d+[-]\d+)"
    test_str = "홍길동 010-1234-5678"
    regex_search(phone_reg, test_str, "")
    regex_search(phone_reg, test_str, "name")
    regex_search(phone_reg, test_str, "phone")

    print("그루핑")
    reg = r"(ABC)+"
    test_str = "ABCABCABC OK?"
    regex_match(reg, test_str, "")


    print("문자열바꾸기")
    p = re.compile(r'(blue|white|red)')
    data = p.sub("colour", 'blue socks and red shoes', count=1)
    print(data)

    data = p.subn("colour", 'blue socks and red shoes', count=1)
    print(data)

    print("sub 메서드를 사용할 때 참조 구문 사용하기")
    p = re.compile(phone_reg)
    test_str = "홍길동 010-1234-5678"
    print(p.sub("\g<phone>\g<name>", test_str))

    p = re.compile(r"\d+")
    result = p.sub(hexrepl, 'Call 65490 for printing 49152 for user code.')
    print(result)

    print("Greedy vs Non-Greedy")
    s = """<html><head><title>제목</title></head><body></body></html>
    """
    print("len(s)=", s)
    print(re.match(r'<.*>', s).span())
    print(re.match(r'<.*>', s).group())

    print(re.match(r'<.*?>', s).span())
    print(re.match(r'<.*?>', s).group())
