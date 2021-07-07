class Chapter4(Exception):
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def say():
        return "Hi"

    @staticmethod
    def add_many(*args):
        result = 0
        for i in args:
            result += i
        return result

    @staticmethod
    def add_mul(choice, *args):
        if choice == "add":
            result = 0
            for i in args:
                result += i
        elif choice == "mul":
            result = 1
            for i in args:
                result *= i
        return result

    @staticmethod
    def add_and_num(a, b):
        return a + b, a * b

    @staticmethod
    def say_nick(nick):
        if nick == "바보":
            return
        print("나의 별명은 %s입니다" % nick)

    @staticmethod
    def say_myself(name, old, man=True):
        print(f"""나의 이름은 {name}입니다.""")
        print(f"""나의 나이는 {old}입니다.""")
        if man:
            print("남자입니다.")
        else:
            print("여자입니다.")

    @staticmethod
    def set_numbers():
        number = input("숫자를 입력하세요: ")
        print(number)

    @staticmethod
    def createNewFile(name):
        f = open(name, 'w')
        f.close()

    @staticmethod
    def readFile(name):
        f = open(name, "r")
        while True:
            line = f.readline()
            print(line)
            if not line: break
        f.close()

    @staticmethod
    def appendFile(name, content):
        try:
            f = open(name, 'a')
            f.write(content + "\n")
            f.close()
        except Exception as e:
            print(e)
