class A: # Base Class
    def add(self):
        print("ClassA.add")


class B(A): # Sub Class
    def add(self):
        print("ClassB.add")
        super().add()


class C(A): # Sub Class
    def add(self):
        print("ClassC.add")
        super().add()


class D(B,C): # Sub Class
    def add(self):
        print("ClassD.add")
        super().add()


if __name__ == '__main__':
    b_obj = D()
    b_obj.add()


    from pprint import pprint  as pp
    print("MRO of class D")
    pp(D.__mro__)


