class DataUsage:

    def __init__(self, used, remaining):
        self.used = used
        self.remaining = remaining
        self.total = remaining + used
        self.percentage = (used / self.total) * 100

    def getDataUsed(self):
        return "%.2f" % self.used

    def getDataRemaining(self):
        return "%.2f" % self.remaining

    def getTotalData(self):
        return "%.2f" % self.total

    def getPercentageUsed(self):
        return "%.2f" % self.percentage

    def formatUsageMessage(self):
        return "You have used {0:.2f}% of your data. You have {1:.2f}GB remaining.".format(self.percentage, self.remaining)