class A:
    def __init__(self):
        print("Class A init")


class B(A):
    def __init__(self):
        print("Class B init")
        super().__init__()


class C(B):
    def __init__(self):
        print("Class C init")
        super(C, self).__init__()


if __name__ == '__main__':
    c = C()

