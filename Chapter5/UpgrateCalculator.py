from Chapter5.Calculator import Calculator


class UpgrateCalculator(Calculator):
    def minus(self, val):
        self.value -= val
