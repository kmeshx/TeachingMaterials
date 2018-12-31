class Q(object):
    numQs = 0
    def __init__(self):
        
        self.size = 0
        self.elements = []
        Q.numQs += 1
        
    def __repr__(self):
        return "<" + __class__.__name__ + " of size " + str(self.size) + ">"
        
    def __eq__(self, other):
        bool1 = (self.size == other.size)
        if bool1:
            for i in range(len(self.elements)):
                if self.elements[i] != other.elements[i]:
                    return False
            
            return True
        else:
            return False
        
        
    def add(self, num):
        self.elements.append(num)
        self.size += 1
        
    def remove(self):
        ret = self.elements.pop(0)
        self.size -= 1
        return ret
        
    @staticmethod
    def getNumQs():
        return 0
        
class PQ(Q):
    
    def __repr__(self):
        return "<" + __class__.__name__ + " of size " + str(self.size) + ">"
        
    def remove(self):
        minel = min(self.elements)
        self.elements.remove(minel)
        self.size -= 1
        return minel
    
    
    
    
#############OOP THING################

class Q(object):
    #numq
    def __init__(self):
        self.size = 0
        self.l = []
        
    @staticmethod
    def getNumQs():
        return 0
        
    def __repr__(self):
        return  ... __class__.__name__ ...
    
    def add(self, num):
        self.size+=1
        #append
        
    def remove(self):
        r = self.l.pop(0)
        return r
        #-1 size
        
    def __eq__(self, other):
        bool1 = len(self.l) == len(other.l)
        #loop 
    
        
class PQ(Q):
    def __repr__(self):
        return  ... __class__.__name__ ...
        
    def remove(self):
        #remove min
    

assert(Q.getNumQs() == 0)
q = Q()
assert(str(q) == "<Q of size 0>")
q.add(5)
q.add(3)
assert(str(q) == "<Q of size 2>")
assert(q.remove() == 5) # first-in, first-out!
assert(str(q) == "<Q of size 1>")
assert(q.remove() == 3)
assert(str(q) == "<Q of size 0>")
assert(Q.numQs == 1)

q1 = Q()
q1.add(42)
q2 = Q()
q2.add(42)
q3 = Q()
q3.add(99)
assert(q1 == q2)
assert(q1 != q3)
assert(Q.numQs == 4)

pq = PQ()
assert(type(pq) == PQ)
assert(isinstance(pq, Q))

pq.add(4)
pq.add(10)
pq.add(2)
pq.add(3)
pq.add(27)
pq.add(-2)
print(pq)
assert(str(pq) == "<PQ of size 6>")
assert(pq.remove() == -2)
assert(pq.remove() == 2)
assert(str(pq) == "<PQ of size 4>")
assert(pq.remove() == 3)
assert(str(pq) == "<PQ of size 3>")

print("Passed!")