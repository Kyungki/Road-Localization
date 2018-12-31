class DataPoint:
    def __init__(self, time, anchor, power, distance):
        self.time = time
        self.anchor = anchor
        self.power = power
        self.distance = distance


class GetDp:
    def datapoint1(self):
        DataPoint()
        dplist = []
        dp = [self.time, self.anchor, self.power, self.distance]
        dplist.append(dp)
        print(dplist)

