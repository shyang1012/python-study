from Chapter5.UpgrateCalculator import UpgrateCalculator
from Chapter5.MaxLimitCalculator import MaxLimitCalculator
import sys
import os
import glob
import time
import random

def add(*args):
    result = 0
    lists = args[0]
    for i in lists:
        result += int(i)
    return result

class Practice:
    def positive(self, args):
        return args > 0

    def q1(self):
        cal = UpgrateCalculator()
        cal.add(10)
        cal.minus(7)
        print(cal.value)

    def q2(self):
        cal = MaxLimitCalculator()
        cal.add(50)
        cal.add(60)
        print(cal.value)

    def q3(self):
        print("1.", all([1, 2, abs(-3) - 3]))
        print("2.", chr(ord('a')) == 'a')

    def q4(self):
        originList = [1, -2, 3, -5, 8, -3]
        result = list(filter(self.positive, originList))
        print(result)

    def q5(self):
        print(hex(234))
        print(int(0xea))

    def q6(self):
        ori_list = [1, 2, 3, 4]
        results = list(map(lambda a: a * 3, ori_list))
        print(results)

    def q7(self):
        myList= [-8, 2, 7, 5, -3, 5, 0, 1]
        print("최소값", min(myList))
        print("최대값", max(myList))

    def q8(self):
        print(round(17/3, 4))

    def q9(self):
        data = sys.argv[1:]
        print(data)
        print(add(data))

    def q10(self):
        path = "/doit"
        os.chdir(path)
        curPath = os.popen("dir")
        print(curPath.read())

    def q11(self):
        path = "/doit"
        os.chdir(path)
        cur_path = os.getcwd()+"\\*.py"
        print(glob.glob(cur_path))

    def q12(self):
        print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))

    def q13(self):
        list = []
        while len(list) < 6:
            num = random.randint(1, 45)
            if num not in list:
                list.append(num)
        print(list)



if __name__ == '__main__':
    practice = Practice()
    practice.q1()
    practice.q2()
    practice.q3()
    practice.q4()
    practice.q5()
    practice.q6()
    practice.q7()
    practice.q8()
    practice.q9()
    practice.q10()
    practice.q11()
    practice.q12()
    practice.q13()
