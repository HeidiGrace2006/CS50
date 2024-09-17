class Jar:
    #initializing the capacity and size of the jar
    def __init__(self, capacity =12, size =0):
        self.capacity = capacity
        self.size = size
        #making sure that capacity is a positive integer
        try:
            if int(capacity) <0:
                raise ValueError("Invalid capacity")
        except:
            raise ValueError("Invalid capacity")

    #making sure that cookies is a string
    def __str__(self):
        self.cookies = ""
        for _ in range(0, self.size):
            self.cookies += "🍪"
        return self.cookies
        #alternatively, delete everything else.. return self.size * "🍪"

    #adding cookies to the jar
    def deposit(self, n):
        for _ in range(0, n):
            self.size += 1
        if self.size > self.capacity:
            raise ValueError("Too many cookies!")

    #taking out cookies from the jar
    def withdraw(self, n):
        for _ in range(0, n):
            self.size -= 1
        if self.size <0:
            raise ValueError("No more cookies to withdraw.")

    #getters and setters
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        self._cookies = cookies

'''
jar = Jar(12, 0)
jar.deposit(5)
jar.withdraw(1)
print(jar)
print(jar.size)
print(jar.capacity)
'''