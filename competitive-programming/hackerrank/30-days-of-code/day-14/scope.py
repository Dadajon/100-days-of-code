class Difference:
    def __init__(self, a):
        self.maximumDifference = 0
        self.__elements = a

    def computeDifference(self):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                difference = abs(a[i] - a[j])
                self.maximumDifference = max(difference, self.maximumDifference)


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)