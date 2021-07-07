class FourCal:
    def __init__(self):
        self.first = 0
        self.second = 0

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second

    def mul(self):
        return self.first * self.second
