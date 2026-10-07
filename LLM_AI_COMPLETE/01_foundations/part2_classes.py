class TinyCounter:
    def __init__(self):
        self.counts = {}

    def update(self, text):
        for w in text.split():
            self.counts[w] = self.counts.get(w, 0) + 1

    def most_common(self):
        return max(self.counts, key=self.counts.get)


c = TinyCounter()
c.update("the cat sat on the mat")
print(c.counts)
print(c.most_common())

c.update("the dog ate the bone")
print(c.counts)
print(c.most_common())