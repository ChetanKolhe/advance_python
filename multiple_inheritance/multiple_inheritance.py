class A:
    def add(self):
        print("ClassA.add")


class B(A):
    def add(self):
        super().add()
        print("ClassB.add")


class C(A):
    def add(self):
        super().add()
        print("ClassC.add")


class D(B, C):
    def add(self):
        super().add()
        print("ClassC.add")
