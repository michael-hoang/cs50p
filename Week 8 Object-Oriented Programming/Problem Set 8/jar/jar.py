class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit failed. Too much cookies in the cookie jar.")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Withdraw failed. Not enough cookies in the cookie jar.")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
             raise ValueError("Capacity cannot be less than 0.")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size