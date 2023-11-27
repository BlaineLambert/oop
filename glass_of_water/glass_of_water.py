class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount):
        self.amount = min(self.amount + amount, self.capacity)

    def pour_out(self, amount):
        self.amount = max(self.amount - amount, 0)

