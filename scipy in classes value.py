from scipy import constants


class Mike:
    def __init__(self, npi, li):
        self.npi = npi
        self.li = li


class Seek(Mike):
    def __init__(self, npi, li):
        self.npi = npi
        self.li = li

    def silk(self):
        print("It's Seek value")


class Milk(Mike):
    def __init__(self, npi, li):
        self.npi = npi
        self.li = li

    def silk(self):
        print("it's Milk value")


# p0 = Mike(f"the minute is {constants.degree}", f"the minute is {constants.minute}")
p1 = Seek(f"the value of pi is {constants.pi}", f"the liter is {constants.liter}")
p2 = Milk(f"the yotta is {constants.yotta}", f"the metric ton is {constants.metric_ton}")

for i in (p1, p2):
    print(i.npi)
    print(i.li)
    i.silk()