import ctypes
class myList:
    def __init__(self):
        self.size =1
        self.n = 0
        self.A = self.createArr(self.size)
    
    def createArr(self, capacity):
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n
    
    def append(self, item):
        # print(self.size)
        # print(self.n)
        if self.n == self.size:
            self.resize()
        self.A[self.n] = item
        self.n += 1

    def resize(self):
        self.size *= 2
        B = self.createArr(self.size) #create the new array
        #copy the content of the array
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    #print we define __str__ function
    def __str__(self):
        res = ''
        for i in range(self.n):
            res = res + str(self.A[i]) + ','
        return '[' + res[:-1] + ']'

    def __getitem__(self, index):
        if 0<= index and index<= self.n:
            return self.A[index]
        else:
            return "index error"
    
    def pop(self):
        if self.n == 0:
            return "empty list"
        else:
            print(self.A[self.n-1])
            self.n = self.n - 1

    def search(self, ip):
        for i in range(self.n):
            if self.A[i] == ip:
                return i
        return "ValueError: Item not in the list"

    def insert(self, index, ip):
        if index > 0 and index <= self.n and self.n < self.size:
            i = self.n
            while i!=index:
                self.A[i] = self.A[i-1]
                i = i-1
            self.A[index] = ip
            self.n += 1
        else:
            self.resize()
            self.insert(index, ip)

    def __delitem__(self, pos):
        if pos >=0 and pos <self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1
        else:
            return "Index Error"
    
    def remove(self, item):
        pos = self.search(item)
        #if not in list then it will return a string
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    

    
    


L = myList()
L.append(9)
print(L.search(8))
print(len(L))  
L.append(10)
print(str(L)) 
L.insert(1,8)
print(L)
print(L.remove(20))
print(L)
del L[2]
print(L)
print(L[0])
L.pop()
print(L)
L.pop()
print(L)


