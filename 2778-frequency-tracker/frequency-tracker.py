class FrequencyTracker(object):

    def __init__(self):
        self.numbers = {}
        self.frequencies = {0: set()}

    def add(self, number):
        freq = self.numbers.get(number, 0)
        if freq > 0:
            self.frequencies[freq].discard(number)
        self.numbers[number] = freq + 1
        self.frequencies[freq + 1] = self.frequencies.get(freq + 1, set())
        self.frequencies[freq + 1].add(number)

    def deleteOne(self, number):
        freq = self.numbers.get(number, 0)
        if freq > 0:
            self.frequencies[freq].discard(number)
            if freq == 1:
                del self.numbers[number]
            else:
                self.numbers[number] = freq - 1
                self.frequencies[freq - 1].add(number)

    def hasFrequency(self, frequency):
        return frequency in self.frequencies and len(self.frequencies[frequency]) > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)