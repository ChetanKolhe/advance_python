class A:
    def add(self):
        print("ClassA.add")

    @staticmethod
    def static_method():
        print("Class A static method ")


class B(A):
    def add(self):
        super(B, self).add()
        print("ClassB.add")


class C(A):  # C --> A --> Object
    def add(self):
        super(C, self).add()
        print("ClassC.add")

    @staticmethod
    def static_method():
        super().static_method()
        super(C, C).static_method()


class D(B, C):

    def add(self):
        super(D, self).add()
        print("ClassD.add")


if __name__ == '__main__':
    d_obj = D()
    d_obj.add()
