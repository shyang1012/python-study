def check_contains_number(num):
    numeric_arr = range(1, 4 + 1)
    result = f"""{num}이(가) 없습니다."""
    if num in numeric_arr:
        result = f"""{num}이(가) 있습니다."""
    return result


def possible_python(title):
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
    return data.pop(title)


if __name__ == '__main__':
    print("hello world")
    print('Life is too short, You need Python')
    for i in range(1, 11, 2):
        print(check_contains_number(i))
    print(possible_python('시스템유틸리티제작'))
