class A:
    def feature1(self):
        print('Feature 1 working')

    def feature2(self):
        print('Feature 2 working')

class B:
    def feature3(self):
        print('Feature 3 working')

    def feature4(self):
        print('Feature 4 working')

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()

#child class from A. So features 1-2 (A), 5-6(own) are available
#SINGLE LEVEL INHERITANCE
class C(A):
    def feature5(self):
        print('Feature 5 working')

    def feature6(self):
        print('Feature 6 working')
c1 = C()
c1.feature1()
c1.feature2()
c1.feature5()
c1.feature6()

#MULTILEVEL INHERITANCE: D child from C child from A
#available features: 7-8 (own), 5-6 (from C) and 1-2 (from A)
class D(C):
    def feature7(self):
        print('Feature 7 working')

    def feature8(self):
        print('Feature 8 is working')
d1 = D()
d1.feature1()
d1.feature2()
d1.feature5()
d1.feature6()
d1.feature7()
d1.feature8()

#MULTIPLE INHERITANCE: E child from A and B
#available features: 9-10 (own), 1-2 (A) and 3-4 (B)
class E(A, B):
    def feature9(self):
        print('Feature 9 is working')

    def feature10(self):
        print('Feature 10 is working')

e1 = E()
e1.feature9()
e1.feature10()
e1.feature1()
e1.feature2()
e1.feature3()
e1.feature4()

