class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if(self.a < other.a):
            return "Object 1 is less than Object 2"
        else:
            return "Object 1 is greater than Object 2"
    def __eq__(self,other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "They are not equal"
        
ob1 = A(2)
ob_2 =A(3)
print("The Passed Values:",ob1.a, ob_2.a)
print(ob1 < ob_2)

ob3 = A(4)
ob4 = A(4)
print("Passed Values:", ob3.a, ob4.a)
print(ob3 == ob4)