class Calulator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calulator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(10)

print(cal.value)