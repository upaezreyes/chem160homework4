class point:   # the class name is piont
    def __init__(self, dim, data):  #initialization function
        self.dim = dim   #dimenssion
        self.data = []   # added list

        for i in range(dim):  # loop for dim
            self.data.append(float(data[i]))  # add values to list(self.data=[])
    def __repr__(self):
        output=""   # empty output string

        for i in self.data:
            output += str(i)+" "  # combert digits to strings
        return output
    def scale(self,x):
        for i in range(self.dim):
            self.data[i]*=x
    def add(self, apoint):    # calculates the dot product of self point and apoint(2nd point)
        sum = 0
        for i in range(self.dim):
            sum += self.data[i]+apoint.data[i]
        return sum 
    def sqmag(self, apoint):
        sum = 0
        for i in range(self.dim):
            sum += self.data[i]**2 + apoint.data[i]**2
            
        return sum
