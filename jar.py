class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        self.capacity = capacity

    def __str__(self):
        cookies = []
        for _ in range(self._size):
            cookies.append("🍪")
        cookies = "".join(cookies)
        return cookies

    def deposit(self, n):
        if (self._size + n) > self.capacity or n < 0:
            raise ValueError
        self._size += n


    def withdraw(self, n):
        if self._size - n < 0 or n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity


    @property
    def size(self):
        return self._size


def main():
    jar = Jar(-4)
    print(jar)

if __name__=="__main__":
    main()
