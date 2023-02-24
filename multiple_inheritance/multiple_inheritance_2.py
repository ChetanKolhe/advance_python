from pprint import pprint


class A:
    def add(self):
        print("A")


class B: pass


class C: pass


class D(A, B):
    def add(self):
        print("D")


class E(B, C): pass


class F(D, E): pass


pprint(F.mro())
pprint(F.__mro__)
