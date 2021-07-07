from Chapter4.chapter4_class import Chapter4

if __name__ == '__main__':
    Chapter4.set_numbers()
    print(Chapter4.add(1, 2))
    print("I was say %s" % Chapter4.say())
    print(Chapter4.add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(Chapter4.add_mul("mul", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(Chapter4.add_and_num(5, 6))
    Chapter4.say_nick("강아지")
    Chapter4.say_myself("홍길동", 30)
    fileName = "/dev/test.txt"
    Chapter4.createNewFile(fileName)
    Chapter4.appendFile(fileName, "안녕하세요")
    Chapter4.appendFile(fileName, "반갑습니다.")
    Chapter4.readFile(fileName)

