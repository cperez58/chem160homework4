class point:
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum
    def add(self,bpoint):
        add1=0
        for i in range(self.dim):
            add1=self.data[i]+bpoint.data[i]
        ##return add1 #Do not want program to print out or return any output
    def sqmag(self,cpoint):
        mag=0
        for i in range(self.dim):
            mag=(self.data[i])**2+(cpoint.data[i])**2
        return mag
    

