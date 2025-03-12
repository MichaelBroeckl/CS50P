class Jar:

    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError('There can only be a positive integer of coocies in the jar.')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError('Not enough room for that many cookies in the jar.')
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError('There are less cookies in the jar than you try to withdraw :(')
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(5)
    print(jar)

if __name__ == "__main__":
    main()
