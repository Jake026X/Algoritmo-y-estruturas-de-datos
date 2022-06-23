from cola import Cola

class Cola():
    def __init__(self):
        self.cola = []
        self.size = 0
    def empty(self):
        return len(self.cola) == 0
    def push(self,dato):
        self.cola +=[dato]
        #self.cola = self.cola + [dato]
        self.size += 1
    def pop(self):
        if self.empty():
            print ("No hay pacientes")
        else:
            self.cola = [self.cola[i] for i in range (1, self.size)]
            self.size -= 1
        
    def shoe(self):
        n = self.size - 1
        while n > -1:
            print("[%d] => %d"%(n,self.cola[n]))
            n -= 1
    def front (self):
        if self.empty():
            print ("Sin pacientes")
        else:
            print ("Primer dato: %d"% (self.cola[0]))